# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


# Cette partie du code est nécessaire afin que Sphinx puisse documenter l'ensemble des modules python
import os
import sys

for path, folders, files in os.walk('../../src'):
    for fd in folders:
        sys.path.insert(0, os.path.abspath(fd))

# Informations associées au projet et issues de sphinx-quickstart
project = 'Accenture - Modèle ALM'
copyright = '2024, L. Aldebert / G. Legris'
author = 'L. Aldebert / G. Legris'
release = '24.05'

# Extensions Sphinx à activer
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosectionlabel',
    'sphinx_design',
    #'sphinx_fontawesome',
    'sphinx.ext.extlinks',
    'sphinx_multiversion',
    'sphinxcontrib.mermaid',
    # 'sphinx.ext.intersphinx', 
    # 'hoverxref.extension',
    # 'sphinx_tippy'
]

# Définit les différentes extensions utilisées dans la documentation
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# fichiers à exclure de la documentation
exclude_patterns = []

# Répertoire templates et static, utilisé dans le cas de l'utilisation de sphinx multi version
templates_path = ['_templates']
html_static_path = ['_static']

html_js_files = [
   'js/mermaid.js',
]

# css à utiliser dans le cas du site web 
html_css_files = [
    'custom.css',
    'gantt.css'
    # 'tippy.css'
]

mermaid_params = ['--configFile', '_static/ganttConfig.json']

# langue
language = 'fr'

# Choix du thème Sphinx
html_theme = 'sphinx_rtd_theme'

# options assiciées au thème 
html_theme_options = {
    #'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    #'analytics_anonymize_ip': False,
    #'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    #'style_external_links': False,
    'vcs_pageview_mode': '',
    #'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': -1,
    'includehidden': True,
    'titles_only': False
}

# Configuration de mathjax3, utilisé pour l'affichage des équations mathématiques (directive .. math::)
mathjax3_config = {'chtml': {
    'scale': '.8',                     # global scaling factor for all expressions
    'minScale': '.3',                  # smallest scaling factor to use
    'matchFontHeight': 'true',         # true to match ex-height of surrounding font
    'mtextInheritFont': 'false',       # true to make mtext elements use surrounding font
    'merrorInheritFont': 'true',       # true to make merror text use surrounding font
    'mathmlSpacing': 'false',          # true for MathML spacing rules, false for TeX rules
    'skipAttributes': '{}',            # RFDa and other attributes NOT to copy to the output
    'exFactor': '.5',                  # default size of ex in em units
    'displayAlign': 'left',            # default for indentalign when set to 'auto'
    'displayIndent': '0'               # default for indentshift when set to 'auto'
}}

# Configuration des liens externes : A supprimer si non utilisé
extlinks = {
    'var': ('file:///C:/Users/lionel.aldebert/Repositories/modele-alm-polars-v2/doc/build/html/metadata/catalogue-donnees.html#%s', '%s'),
    'df': ('file:///C:/Users/lionel.aldebert/Repositories/modele-alm-polars-v2/doc/build/html/metadata/dataframes.html#%s', '%s'),
    # Ajoutez d'autres liens si nécessaire
}

autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 3



# Configuration de hoverxref
# hoverxref_roles = ['ref', 'doc']
# hoverxref_auto_ref = True  # Activer les info-bulles pour les références automatiques
# hoverxref_domains = ['std']
# hoverxref_role_types = {
#     'doc': 'modal',
#     'ref': 'modal',
# }
# hoverxref_lazy_load = False

# hoverxref_roles = ['ref', 'doc', 'numref', 'confval', 'mod', 'class', 'meth', 'attr', 'func']
# hoverxref_auto_ref = True  # Activer les info-bulles pour les références automatiques
# hoverxref_role_types = {
#     'hoverxref': 'tooltip',
#     'doc': 'tooltip',
#     'ref': 'tooltip',
#     'numref': 'tooltip',
#     'confval': 'tooltip',
#     'mod': 'tooltip',
#     'class': 'tooltip',
#     'meth': 'tooltip',
#     'func': 'tooltip',
#     'attr': 'tooltip',
#     'exc': 'tooltip',
#     'obj': 'tooltip',
# }

# intersphinx_mapping = {
#     'readthedocs': ('https://docs.readthedocs.io/en/stable/', None),
#     'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
#     'sympy': ('https://docs.sympy.org/latest/', None),
#     'numpy': ('https://numpy.org/doc/stable/', None),
#     'python': ('https://docs.python.org/3/', None),
# }
# hoverxref_intersphinx = [
#     'readthedocs',
#     'sphinx',
#     'sympy',
#     'numpy',
#     'python',
# ]
# hoverxref_intersphinx_types = {
#     'readthedocs': 'modal',
#     'sphinx': 'tooltip',
# }

# Configuraiton de autodoc, utilisé pour la génération de la doc des modules python
autodoc_default_options = {
    'members': True,
    'undoc-members': False,
    'private-members': False,
    'special-members': False,
    'inherited-members': False,
    'show-inheritance': False,
    'member-order': 'bysource',
    'exclude-members': '__weakref__',
    'show-inheritance': False,
    'ignore-module-all': True,
    'docstring_signature': True,
}


# Paramètre associés à la configuration de sphinx-multiversion
smv_tag_whitelist = r'^v\d+\.\d+.*$'
smv_branch_whitelist = r'^(main|develop)$'
smv_remote_whitelist = r'^origin$'
smv_released_pattern = r'^refs/tags/v\d+\.\d+$'
smv_outputdir_format = '{ref.name}'

# Options de configuration pour napoleon
# napoleon_google_docstring = True
# napoleon_numpy_docstring = True
# napoleon_include_init_with_doc = False
# napoleon_include_private_with_doc = False
# napoleon_include_special_with_doc = True
# napoleon_use_admonition_for_examples = False
# napoleon_use_admonition_for_notes = False
# napoleon_use_admonition_for_references = False
# napoleon_use_ivar = False
# napoleon_use_param = True
# napoleon_use_rtype = True
# napoleon_custom_sections = [('Returns', 'params_style')]
