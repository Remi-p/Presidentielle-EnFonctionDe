# Présidentielle 2017 : En fonction de...

Ces scripts sont livrés comme tels, sans AUCUNE GARANTIE.

Il existe de nombreux biais dans le code.
Il faut prendre en compte que le nombre de villes d'une certaine taille peut varier très fortement, rendant l'erreur statistique importante pour certains points des courbes.
Par ailleurs toutes les villes > 100 000 habitants sont regroupées, il est intéressant de les séparer pour remarquer des disparités (Nice, Marseille).

L'échelle par défaut est logarithmique.

Le script a été majoritairement fait pour le fun pour mettre en vis-à-vis des valeurs pas directement liées.

## Exemples

![Pourcentage Macron en fonction du nombre d'inscrits dans la commune](Exemples-PNG/Nb-Inscrits-Macron.png)

![Pourcentage Le Pen en fonction du nombre d'inscrits dans la commune](Exemples-PNG/Nb-Inscrits-Le-Pen.png)

![Pourcentage Fillon en fonction du nombre de pharmacies dans la commune](Exemples-PNG/Nb-Pharmacies-Fillon.png)

![Pourcentage Mélenchon en fonction du pourcentage de propriétaires dans la commune](Exemples-PNG/Nb-Proprietaires-Mélenchon.png)

## Système requis

Le script est écrit en Python 3.

Les modules utilisés :

* matplotlib 1.5.1
* numpy 1.11.0
* (scipy) 0.17.0

Sous Debian :
```
sudo apt-get install python python-numpy python-matplotlib python-scipy
```

## TODO

* Mettre le nombre d'occurrences pour la fiabilité des résultats.
* Calculer le pourcentage en fonction du nombre d'inscrits plutôt que d'occurrences
	* Sur l'échelle logarithmique ? (pour la fonction `find_nearest_idx`)
* Gérer plusieurs candidats sur un même graphique
* Rajouter des corrélations possibles
* Interpoler les courbes

## Références

Les références techniques sont au sein du code.

Jeux de données utilisés :

* [Résultats élections présidentielle 2017](https://www.data.gouv.fr/fr/datasets/election-presidentielle-des-23-avril-et-7-mai-2017-resultats-du-1er-tour-1/) : nombre d'inscrits, pourcentage de vote par candidats, etc. - INSEE
* [Data INSEE sur les communes](http://www.data.gouv.fr/fr/datasets/data-insee-sur-les-communes/) : nombre de dentistes, de propriétaires, etc. - INSEE
