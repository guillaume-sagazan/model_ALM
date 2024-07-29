Setup de VS Code
================

Installation de VS Code, Git & Python
-------------------------------------

Installation de VS Code
^^^^^^^^^^^^^^^^^^^^^^^

Si non installé, downloader VS Code sur internet 

Ouvrir l'installer avec "Run as administrator" 

Installation de Git
^^^^^^^^^^^^^^^^^^^

Si non installé, downloader Git sur git-scm.com 

Ouvrir l'installer avec "Run as administrator" 

Installation de Python
^^^^^^^^^^^^^^^^^^^^^^

Si non installé, downloader python 3.12 

Ouvrir l'installer avec "Run as administrator" 

Gitlab & import des sources du projet
-------------------------------------

Ouverture d'un compte gitlab
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Allez sur GitLab.com et ouvrir un compte gratuit avec son adresse accenture 

Informer Lionel A que le compte a été créé et attendre qu'il vous donne accès aux différents repositories 

 
Clone du repo git sur votre poste
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dans votre répertoire c:\\users\\prenom.nom, créer un répertoire "repositories" 

Ouvrir un terminal 

Lancer la commande : cd c:\\users\\prenom.nom\\repositories 

Lancer la commande : git clone https://gitlab.com/accenture_france_actuariat/modele-alm-polars-v2.git 

 
Lancement de VS code et finalisation du set up 
----------------------------------------------

Installation de l'extension Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Si non réalisé, installer l'extension VS Code Python 

Création environnement virtuel Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dans VS Code:

* CTRL + Shift + P 
* puis "Python : Create Environment..." 
* puis "Venv" 
* puis sélectionner votre installation de python
* puis activer requirements.txt pour installer toutes les librairies nécessaires au projet

 
Générer la documention du projet  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dans l'interface permettant de lancer des runs, lancer 

Commencer à lire la documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La documentation projet est générée dans le répertoire doc/build/html 

Allez dans ce répertoire, click droit sur index.html > Reveal in File Explorer 

Ouvrez le fichier index.thml avec chrome, et commencez à lire 