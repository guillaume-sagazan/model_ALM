Sphinx
======

Liens externes
--------------

`Documentation Sphinx <https://www.sphinx-doc.org/en/master/>`_

`Documentation Sphinx RTD theme <https://sphinx-rtd-theme.readthedocs.io/en/stable/>`_

`Guide Sublime and Sphinx <https://sublime-and-sphinx-guide.readthedocs.io/en/latest/index.html>`_

`Sphinx Design <https://sphinx-design.readthedocs.io>`_ 

`Symboles Latex <https://www.cmor-faculty.rice.edu/~heinken/latex/symbols.pdf>`_

`Sphinx Multi-versions <https://www.cmor-faculty.rice.edu/~heinken/latex/symbols.pdf>`_

Installation des packages
-------------------------

Est recommandé l'installation des packages python suivants :

* **sphinx :** Package de base 
* **sphinx_rtd_theme :** Sphinx gère différents thèmes, celui-ci est le plus populaire
* **sphinx-design :** Ce package permet l'utilisation des directives dropdown, octicon...
* **sphinx-multiversion :** Ce package permet de gérer l'accès à différentes versions de la documentation 

Utilisation de sphinx au sein d'un projet Python
------------------------------------------------

Soit un projet python ayant été précédemment structuré avec :abbr:

* un répertoire "src" contenant les sources
* un répertoire "doc" ayant vocation à contenir la documentation
* un répertoire "tools" contenant les différents scripts

Suivre les étapes suivantes :

* Ouvrir un terminal Python dans VS code
* se placer dans le répertoire "doc" du projet : "cd doc"
* Initialiser le projet sphinx avec la commande : "sphinx-quickstart"
* Répondre aux questions posées par le terminal. Est conseillé de séparer les sources et le site web
* Tester la génération de la documentation avec la commande : "make html"

Une fois cette commande effectuée, est possible de visualiser la documentation en ouvrant le fichier "doc/build/html/index.html" dans un navigateur.

Est possible de nettoyer les fichiers générés avec la commande "make clean html" avant de regénérer la documentation avec "make html".

Mise à jour du fichier conf.py
------------------------------

Le theme par défaut, alabaster, n'est pas très esthétique. Pour changer de thème, il est nécessaire de modifier le fichier "doc/source/conf.py".

Ce fichier dans ce projet est entièrement commenté de sorte à pouvoir être facilement réutilisé.   

Création d'une "run config vs code"
-----------------------------------

A des fins de productivité, il est possible de créer une "run config vs code" pour automatiser le processus de création de la documentation.

Pour cela, est possible de reprendre le script "tools/genererDocumentation.py" présent dans ce projet.

Celui est commenté. A noter qu'il intègre différentes étapes spécifiques qu'il peut ne pas être nécessaire de reprendre dans le cas d'un projet plus classique.

Ceci étant fait, reste simplement à créer la configuration nécessaire dans VS code.

Génération automatique de la documentation via GitLab
-----------------------------------------------------

Tuto à écrire