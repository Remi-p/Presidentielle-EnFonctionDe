#-*- coding: utf-8 -*-

# Pour Mélenchon qui a un accent
# Cf. http://stackoverflow.com/questions/21129020/how-to-fix-unicodedecodeerror-ascii-codec-cant-decode-byte
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Parsing CSV
# Cf. https://docs.python.org/3/library/csv.html
import csv

# Playing with numbers
import numpy as np

# Plotting numbers
# https://matplotlib.org/users/pyplot_tutorial.html
import matplotlib.pyplot as plt

# Interpolating stuffs
# https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html
#~ from scipy.interpolate import interp1d

####################################################### VARIABLES ######

# Column numbers
COMMUNE = 3
INSCRITS = 4

# Candidat
candidat = "MACRON"
# Possibilités : MACRON / LE PEN / FILLON / MÉLENCHON / HAMON /
#                DUPONT-AIGNAN / LASSALLE / POUTOU / ASSELINEAU /
#                ARTHAUD / CHEMINADE

# Graphic precision
precision = 50

# Nombre minimum d'occurrences pour qu'un point apparaisse sur le graph :
min_occ = 20

# Rq : Nice et Marseille se distinguent clairement des autres grdes villes
x_axis = np.logspace(1, 5, precision) # From 10 to 100 000 (englobe toutes les villes > 100 000)
#~ x_axis = np.linspace(10, 100000, precision)

########################################################################

# Rq : Peut-être plutôt faire par nb d'inscrits plutôt que par occurrence
#      Rapport au fait que c'est mieux statistiquement parlant, tout ça.
calculs = { 'x_axis' : [], 'occurrences' : [], 'total' : [] }

# Creating arrays
for i in range(0, len(x_axis)):
    calculs['x_axis'].append(x_axis[i])
    calculs['occurrences'].append(0)
    calculs['total'].append(0.00)

# For histogram purposes
# Oui je n'ai pas réfléchi 1 seconde : http://stackoverflow.com/a/2566508
def find_nearest_idx(array,value):
    idx = (np.abs( np.subtract(array, value) )).argmin()
    return idx

# Récupération du pourcentage associé à un nom
def find_y_value(array, candidat_name):
	index = array.index(candidat_name)
	percent_idx = index + 4
	return float(array[percent_idx].replace(',', '.'))

# ------------------- Traitement des données ---------------------------
with open('Resultats2017.csv') as csvfile:
	
     rowreader = csv.reader(csvfile, delimiter=';', quotechar='|')
     
     for row in rowreader:
		 
         nearest = find_nearest_idx(calculs['x_axis'], int(row[INSCRITS]))
         
         calculs['occurrences'][nearest] += 1
         
         calculs['total'][nearest] += find_y_value(row, candidat)
         
         # print(row[COMMUNE], row[INSCRITS])

# ----------------------------------------------------------------------

#~ print(calculs)

results = {'x_axis' : [], 'y_axis' : [] }

for i in range(0, len(x_axis)):
    if (calculs['occurrences'][i] != 0 and calculs['occurrences'][i] > min_occ):
        results['x_axis'].append(calculs['x_axis'][i])
        results['y_axis'].append( calculs['total'][i] / float(calculs['occurrences'][i]) )

print(len(results['x_axis']))

#~ smooth_result = interp1d(results['nb_inscrits'], results['percent'], kind='slinear')
#~ nb_inscrits_new = np.logspace(1, 5, precision*3)

plt.semilogx(results['x_axis'], results['y_axis'], 'o') #, nb_inscrits_new, smooth_result(nb_inscrits_new), '-')
plt.xlabel('Nombre d\'inscrits (echelle log.)')
plt.ylabel('Pourcentage ' + candidat + ' 2017')
plt.show()
