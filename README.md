# pdf-to-csv
## Converting tabulated data from pdf file to csv

J'ai réalisé ce projet personnel afin de rendre plus accessibles au public certaines données de la Banque de la République d'Haïti (BRH). La BRH publie les taux de change dans des tableaux en format pdf. Ce format ne favorise pas l'utilisation de ces données aux fins d'études et de recherche. Mon travail consiste à concevoir un algorithme pour extraire ces données en toute intégrité et les sauvegarder en format csv. Je pourrai étendre le projet plus tard à d'autres données de la BRH ainsi qu'à certaines données du Ministère de l'Agriculture (MARNDR).

### Instructions
Le script se trouve dans le fichier `main_brh.py`. Pour convertir les données de taux de change de la BRH, suivre les étapes suivantes :
1. Télécharger les fichiers pdf des taux de change publiés par la BRH à l'adresse [BRH Evolution Taux de Change](https://www.brh.ht/politique-monetaire/evolution-du-taux-de-change/) et stocker les fichiers dans un répertoire.
2. Ouvrir le script `main_brh.py` dans votre environnement de travail. Le programme est conçu pour Python.
3. Assurez-vous d'installer les dépendances suivantes (si ce n'est déjà fait) avant de lancer le programme :
   * `camelot` : Svp, installer la dernière version disponible, actuellement la 0.11.0. Peut être installé avec la commande `pip install camelot-py`. Il faut aussi installer les dépendances de camelot (suivre les indications à la page suivante : [Installation dépendances camelot](https://camelot-py.readthedocs.io/en/master/user/install-deps.html).
   * `datetime`
   * `re`
   * `pandas`
4. Changer la valeur de la variable `startRep` (ligne 59) dans le Script. Vous mettrez l'adresse du répertoire sur votre ordinateur où se trouvent les fichiers pdf téléchargés depuis le site de la BRH.
5. Changer la valeur de la variable `destRep` (ligne 60) dans le Script. Vous mettrez l'adresse du répertoire sur votre ordinateur où vous vouler exporter le fichier csv contenant les données de taux de change.
6. Exécuter le script _one-shot_. Les données seront stockées dans un fichier nommé __taux_brh.csv__ situé dans le répertoire désigné à l'étape 1.

### Résultats
Voici un aperçu du résultat obtenu dans Excel :
* Un extrait du tableau de taux de change

![tab_view](https://github.com/frantz93/pdf-to-csv/assets/105858731/07fc9200-f297-4792-8b0b-461feb2f86ad)

* Et aussi pour ceux qui s'intéresse à l'économie haïtienne, voici l'évolution du taux de change observée au cours des 20 dernières années

![graph_view](https://github.com/frantz93/pdf-to-csv/assets/105858731/8c8fedf6-3e16-40ae-a1f1-b0d0f71e9d7f)
