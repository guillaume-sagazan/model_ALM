import logging
import os
import pickle
import re
import subprocess
import sys

# Import de la classe DocGen permettant la génération des fichiers rst pour le catalogue de données ainsi que les formats des dataframes
# Supprimer si non souhaité dans le cadre de la réutilisation de ce script
from docgen.DocGen import getRstContentDictionnaireDonnees, getRstContentDfMdRegistry

# Simple configuration du logger
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")

# Définition des répertoires de travail
fdSrc = os.path.join(os.getcwd(),'src')
fdRstModules = os.path.join(os.getcwd(),'doc/source/modules')
fdRstMetadata = os.path.join(os.getcwd(),'doc/source/metadata')

# Commande à utiliser pour générer la documentation du code
sphinxApiDocCmd = os.path.join(os.getcwd(),"sphinx-apidoc.exe")

logging.info(f'fdSrc : {fdSrc}')
logging.info(f'outputFdModules : {fdRstModules}')
logging.info(f'outputFdMetadata : {fdRstMetadata}')

logging.info(f'Clean du répertoire src/modules')
for path, folders, files in os.walk('doc/source/modules'):
    for f in files:
        os.unlink(os.path.join('doc\\source\\modules', f))

logging.info(f'Generation de la documentation du code')
subprocess.call('sphinx-apidoc.exe -M -o doc/source/modules src/', stdout=sys.stdout, stderr=sys.stdout, cwd=os.getcwd())

# Corrections apportées au code généré par sphinx-apidoc
# A supprimer / modifier éventuellement 
for path, folders, files in os.walk('doc/source/modules'):
    for f in files:
        with open('doc/source/modules/' + f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        content = re.sub(' package\n========', '\n', content)
        content = re.sub(' module\n-------', '\n', content)
        content = re.sub('src\n===', 'Documentation du code\n=====================\n\nCette partie de la documentation est dédiée à la documentation du code.\n\n Celui est décomposé en différents packages :', content)
        content = re.sub('\nSubmodules\n----------', '', content)
        content = re.sub('Subpackages\n-----------\n', '', content)
        content = re.sub('.. toctree::', '.. toctree::\n   :hidden:', content)
                                     
        with open('doc/source/modules/' + f, 'w', encoding='utf-8') as file:
            file.write(content)


# Generation du fichier DictionnairesDonnees.rst
# A supprimer / modifier éventuellement
rstDataCatalog = 'catalogue-donnees.rst'
logging.info(f'Génération du fichier {fdRstMetadata + "/" + rstDataCatalog}')
f = open(fdRstMetadata + "/" + rstDataCatalog, "w", encoding='utf-8')
f.write(getRstContentDictionnaireDonnees())
f.close()
logging.info(f'Génération du fichier {fdRstMetadata + "/" + rstDataCatalog} - Fin')

#Generation du fichier dataframes.rst
# A supprimer / modifier éventuellement
rstDataframes = 'dataframes.rst'
logging.info(f'Génération du fichier {fdRstMetadata + "/" + rstDataframes}')
f = open(fdRstMetadata + "/" + rstDataframes, "w", encoding='utf-8')
f.write(getRstContentDfMdRegistry())
f.close()
logging.info(f'Génération du fichier {fdRstMetadata + "/" + rstDataframes} - Fin')

#Generation du site web html simples
logging.info(f'Génération du site web - Regénération du site')
logging.info(sys.argv[0])
logging.info(sys.argv[1])

makeBatPath = os.path.join(os.getcwd(),"doc", "make.bat")
logging.info(f'Execution de .\\make clean html')
subprocess.call([makeBatPath, "clean", "html"], stdout=sys.stdout, stderr=sys.stdout, cwd=os.path.join(os.getcwd(),"doc"))

if sys.argv[1] == 'html':
    logging.info(f'Execution de .\\make html')
    subprocess.call([makeBatPath, "html"], stdout=sys.stdout, stderr=sys.stdout, cwd=os.path.join(os.getcwd(),"doc"))
else: # sys.argv[0] == 'git'
    logging.info(f'Execution de sphinx-multiversion')
    subprocess.call(["sphinx-multiversion.exe", "source/", "build/html"], stdout=sys.stdout, stderr=sys.stdout, cwd=os.path.join(os.getcwd(),"doc"))

# logging.info(f'Listing des labels')

# # Chemin vers le fichier environment.pickle
# env_file = os.path.join(os.getcwd(),'doc', 'build', 'doctrees', 'environment.pickle')

# # Charger le fichier environment.pickle
# with open(env_file, 'rb') as f:
#     env = pickle.load(f)

# # Extraire les labels
# labels = env.domaindata['std']['labels']

# # Afficher les labels
# for label, (docname, labelid, sectname) in labels.items():
#     logging.info(f'{label}: {docname}#{labelid} ({sectname})')

logging.info(f'Génération du site web - Fin')