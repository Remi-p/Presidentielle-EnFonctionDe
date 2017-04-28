#-*- coding: utf-8 -*-

# Pour Mélenchon qui a un accent
# Cf. http://stackoverflow.com/questions/21129020/how-to-fix-unicodedecodeerror-ascii-codec-cant-decode-byte
import sys

# Parsing CSV
# Cf. https://docs.python.org/3/library/csv.html
import csv

# Playing with numbers
import numpy as np

# Plotting numbers
# https://matplotlib.org/users/pyplot_tutorial.html
import matplotlib.pyplot as plt

# Converting logarithm
import math

# Interpolating stuffs
# https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html
#~ from scipy.interpolate import interp1d

####################################################### VARIABLES ######

# Candidat
candidat = "MACRON"
# Possibilités : MACRON / LE PEN / FILLON / MÉLENCHON / HAMON /
#                DUPONT-AIGNAN / LASSALLE / POUTOU / ASSELINEAU /
#                ARTHAUD / CHEMINADE

abscisse = "Nombre d'inscrits dans la commune (échelle log.)"
en_fonction_de = "INSCRITS"
# Possibilités : INSCRITS : Nombre d'inscrits par commune
#                PHARMACIES : Nombre de pharmacies dans la commune
#                PROPRIETAIRES : Pourcentage de propriétaire dans la population
#                CAPACITE_FISCALE : Capacite fiscale moyenne de la commune
#                MEDIANE : Médiane du niveau de vie dans la commune
#  / \ 
# / ! \ You should change x_start & x_end correspondingly

# Graphic informations
x_start = 10
x_end = 100000 # (englobe toutes les villes > 100 000)
x_scale_log = True
precision = 50

# Nombre minimum d'occurrences pour qu'un point apparaisse sur le graph :
min_occ = 15

########################################################################

# Résultats élection présidentielle 2017 - Column numbers
DEPARTEMENT = 0
CODE_COMMUNE = 2
COMMUNE = 3
INSCRITS = 4
DECALAGE_POURCENTAGE = 4
# RESULTATS_IGNORE_LINES = 4

IDX_GEOCODE = 0
# Data INSEE sur les communes
DATAINSEE_IGNORE_LINES = 1
NB_DENTISTES = 18
NB_PHARMACIES = 1
NB_PROPRIETAIRES = 31
CAPACITE_FISCALE = 78
POPULATION = 26
MAX_SEARCH_LOOP = 10

# INSEE - Revenus et pauvreté
REVENUS_IGNORE_LINES = 6
MEDIANE = 4

# Generating x axis :

if (x_scale_log):
    x_start = math.log10(x_start)
    x_end   = math.log10(x_end)
    x_axis  = np.logspace(x_start, x_end, precision)
else:
    x_axis  = np.linspace(x_start, x_end, precision)

# Rq : Peut-être diviser par nb d'inscrits plutôt que par occurrence
#      Rapport au fait que c'est mieux statistiquement parlant, tout ça.
calculs = { 'x_axis' : [], 'occurrences' : [], 'total' : [] }

# Creating arrays
for i in range(0, len(x_axis)):
    calculs['x_axis'].append(x_axis[i])
    calculs['occurrences'].append(0)
    calculs['total'].append(0.00)

# Initializing files
insee = {}
if (en_fonction_de in ["PHARMACIES", "PROPRIETAIRES", "CAPACITE_FISCALE"]):
    insee['communes'] = {}
    insee['communes']['data'] = open("INSEE-DataCommunes.csv")
    insee['communes']['reader'] = csv.reader(insee['communes']['data'], delimiter = ';')
    insee['communes']['row'] = next(insee['communes']['reader'])
if (en_fonction_de == "MEDIANE"):
    insee['revenus'] = {}
    insee['revenus']['data'] = open("INSEE-Revenus-Pauvrete.csv")
    insee['revenus']['reader'] = csv.reader(insee['revenus']['data'], delimiter = ';')
    insee['revenus']['row'] = next(insee['revenus']['reader'])

def from_comma_to_float(toconvert):
    return float(toconvert.replace(',', '.'))

# These functions compute the abscisse where the vote percent should be added
# -- Nombre d'inscrits
def nombre_inscrits(array):
    return int(array[INSCRITS])

# -- Global function for INSEE Données communes // Revenus & pauvreté
def find_commune_get_row(array, dataname):

    dep = array[DEPARTEMENT]
    com = array[CODE_COMMUNE]
    
    # Département absent du jeu de données
    if (dep in ["ZA", "ZB", "ZC", "ZD", "ZM", "ZN", "ZP", "ZS", "ZW", "ZX"]):
        return None
    
    geocode = dep.zfill(2) + com.zfill(3)
    
    # Communes absentes du jeu de données
    if (geocode in ["31300", "35317", "51201", "52033", "52124", "52266", "52278", "52465", "55138", "62847", "67057", "76601", "89326"]):
        return None

    global insee
    
    for i in range(1, MAX_SEARCH_LOOP):
        if (insee[dataname]['row'][IDX_GEOCODE] == geocode):
            return insee[dataname]['row']
        else:
            insee[dataname]['row'] = next(insee[dataname]['reader'])
    
    # On emploi les grands moyens // Recherche dans tout le fichier
    
    insee[dataname]['data'].seek(0)
    for insee[dataname]['row'] in insee[dataname]['reader']:
        if (insee[dataname]['row'][IDX_GEOCODE] == geocode):
            return insee[dataname]['row']
    
    print("/!\ La commune "+geocode+" n'a pas pu être trouvée")
    insee[dataname]['data'].seek(0)
    return None
# --
# -- Nombre de pharmacies
def nombre_pharmacies(array):
    row = find_commune_get_row(array, "communes")
    
    if (row == None):
        return None;
    elif (row[NB_PHARMACIES] == ""):
        return 0
    else:
        return int(row[NB_PHARMACIES])
# --
# -- Pourcentage de propriétaires
def pourcent_proprio(array):
    row = find_commune_get_row(array, "communes")
    
    if (row == None):
        return None;
    else:
        return int( float(row[NB_PROPRIETAIRES]) / float(row[POPULATION]) * 100)
# --
# -- Capacité fiscale
def capacite_fiscale(array):
    row = find_commune_get_row(array, "communes")
    
    if (row == None):
        return None;
    else:
        return int(row[CAPACITE_FISCALE])
# --
# -- Médiane
def mediane(array):
    row = find_commune_get_row(array, "revenus")
    
    if (row == None):
        return None
    elif (row[MEDIANE] == ""):
        return None
    else:
        return from_comma_to_float(row[MEDIANE])
# --

# Oui je n'ai pas réfléchi 1 seconde : http://stackoverflow.com/a/2566508
def find_nearest_idx(array,value):
    idx = (np.abs( np.subtract(array, value) )).argmin()
    return idx

# Récupération du pourcentage associé à un nom
def find_y_value(array, candidat_name):
    index = array.index(candidat_name)
    percent_idx = index + DECALAGE_POURCENTAGE
    return from_comma_to_float(array[percent_idx])

# ------------------- Traitement des données ---------------------------
with open('INSEE-Resultats2017.csv') as csvfile:
    
     rowreader = csv.reader(csvfile, delimiter=';', quotechar='|')
     
     for row in rowreader:
         
         # Should we replace that by a ~switch ? http://stackoverflow.com/a/60211
         if (en_fonction_de == "PHARMACIES"):
             value = nombre_pharmacies(row)
         elif (en_fonction_de == "PROPRIETAIRES"):
             value = pourcent_proprio(row)
         elif (en_fonction_de == "CAPACITE_FISCALE"):
             value = capacite_fiscale(row)
         elif (en_fonction_de == "MEDIANE"):
             value = mediane(row)
         else:
             value = nombre_inscrits(row)
         
         # Ignoring errors :D
         if (value == None):
             continue
         
         nearest = find_nearest_idx(calculs['x_axis'], value)
         
         calculs['occurrences'][nearest] += 1
         calculs['total'][nearest]       += find_y_value(row, candidat)
         
         # print(row[COMMUNE], row[INSCRITS])

# ----------------------------------------------------------------------

print(calculs)

results = {'x_axis' : [], 'y_axis' : [] }

for i in range(0, len(x_axis)):
    if (calculs['occurrences'][i] != 0 and calculs['occurrences'][i] > min_occ):
        results['x_axis'].append(calculs['x_axis'][i])
        results['y_axis'].append( calculs['total'][i] / float(calculs['occurrences'][i]) )

print(len(results['x_axis']))

#~ smooth_result = interp1d(results['nb_inscrits'], results['percent'], kind='slinear')
#~ nb_inscrits_new = np.logspace(1, 5, precision*3)

if (x_scale_log):
    plt.semilogx(results['x_axis'], results['y_axis'], 'o')
else:
    plt.plot(results['x_axis'], results['y_axis'], 'o')

plt.xlabel(abscisse)
plt.ylabel('Pourcentage ' + candidat + ' 2017')
plt.show()
