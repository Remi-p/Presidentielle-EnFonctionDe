# Présidentielle 2017 : En fonction de...

Ces scripts sont livrés comme tels, sans AUCUNE GARANTIE.

Il existe de nombreux biais dans le code.
Il faut prendre en compte que le nombre de villes d'une certaine taille peut varier très fortement, rendant l'erreur statistique importante pour certains points des courbes.
Par ailleurs toutes les villes > 100 000 habitants sont regroupées, il est intéressant de les séparer pour remarquer des disparités (Nice, Marseille).

Par ailleurs, les communes d'outre-mer ne sont parfois pas pris en compte.

Le script a été majoritairement fait pour le fun pour mettre en vis-à-vis des valeurs pas directement liées.

## Exemples

Les points les moins foncés sont les moins fiables (en terme d'occurrences).

```python
candidats = {"MACRON"}
en_fonction_de = "INSCRITS"
abscisse = "Nombre d'inscrits dans la commune (échelle log.)"
x_start = 10
x_end = 100000
x_scale_log = True
precision = 50
```
![Pourcentage Macron en fonction du nombre d'inscrits dans la commune](Exemples-PNG/Nb-Inscrits-Macron.png)

---

```python
candidats = {"LE PEN"}
en_fonction_de = "INSCRITS"
abscisse = "Nombre d'inscrits dans la commune (échelle log.)"
x_start = 10
x_end = 100000
x_scale_log = True
precision = 50
```
![Pourcentage Le Pen en fonction du nombre d'inscrits dans la commune](Exemples-PNG/Nb-Inscrits-Le-Pen.png)

---

```python
candidats = {"FILLON"}
en_fonction_de = "PHARMACIES"
abscisse = "Nombre de pharmacies dans la commune"
x_start = 0
x_end = 8
x_scale_log = False
precision = 4
```
![Pourcentage Fillon en fonction du nombre de pharmacies dans la commune](Exemples-PNG/Nb-Pharmacies-Fillon.png)

---

```python
candidats = {"MÉLENCHON"}
en_fonction_de = "PROPRIETAIRES"
abscisse = "Pourcentage de propriétaires dans la commune"
x_start = 10
x_end = 50
x_scale_log = False
precision = 30
```
![Pourcentage Mélenchon en fonction du pourcentage de propriétaires dans la commune](Exemples-PNG/Nb-Proprietaires-Mélenchon.png)

---

```python
candidats = {"DUPONT-AIGNAN"}
en_fonction_de = "MEDIANE"
abscisse = "Médiane du niveau de vie dans la commune"
x_start = 12500
x_end = 35000
x_scale_log = False
precision = 50
```
![Pourcentage Dupont-Aignan en fonction de la médiane du niveau de vie dans la commune](Exemples-PNG/Mediane-Dupont-Aignan.png)

---

```python
candidats = {"POUTOU"}
en_fonction_de = "CAPACITE_FISCALE"
abscisse = "Capacité fiscale moyenne de la commune"
x_start = 50
x_end = 300
x_scale_log = False
precision = 50
```
![Pourcentage Poutou en fonction de la capacité fiscale moyenne de la commune](Exemples-PNG/Capacite-Fiscale-Poutou.png)

---

```python
candidats = {"ASSELINEAU"}
en_fonction_de = "IMMIGRATION"
abscisse = "Pourcentage d'immigration par commune"
x_start = 0
x_end = 30
x_scale_log = False
precision = 50
```
![Pourcentage Asselineau en fonction du pourcentage d'immigration dans la commune](Exemples-PNG/Immigration-Asselineau.png)

## Système requis

Le script est écrit en Python 3.

Les modules utilisés :

* matplotlib 1.5.1
* numpy 1.11.0
* (scipy) 0.17.0

Sous Debian :
```
sudo apt-get install python3 python3-numpy python3-matplotlib python3-scipy
```

## TODO

* Calculer le pourcentage en fonction du nombre d'inscrits plutôt que d'occurrences
	* Sur l'échelle logarithmique ? (pour la fonction `find_nearest_idx`)
* Rajouter des corrélations possibles
* Interpoler les courbes

## Références

Les références techniques sont au sein du code.

Jeux de données utilisés :

* [Résultats élections présidentielle 2017](https://www.data.gouv.fr/fr/datasets/election-presidentielle-des-23-avril-et-7-mai-2017-resultats-du-1er-tour-1/) : nombre d'inscrits, pourcentage de vote par candidats, etc. - INSEE, 2017
* [Data INSEE sur les communes](http://www.data.gouv.fr/fr/datasets/data-insee-sur-les-communes/) : nombre de dentistes, de propriétaires, etc. - INSEE, 2014
	* (Semble contenir des erreurs, et dater d'avant 2014)
* [Revenus et pauvreté des ménages en 2013](https://www.insee.fr/fr/statistiques/2388572) : Médiane des salaires, taux de pauvreté, etc. - INSEE, 2013
* [Nationalité et immigration en 2013](https://www.insee.fr/fr/statistiques/2044955) : Immigration par commune - INSEE, 2013
