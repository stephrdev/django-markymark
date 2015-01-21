# -*- coding: utf-8 -*-
import sys
import os
import pkg_resources

try:
    import sphinx_rtd_theme
except ImportError:
    sphinx_rtd_theme = None

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'examples.example.settings')

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx'
]

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

# General information about the project.
project = u'markymark'
copyright = u'2015, Moccu GmbH & Co. KG'

distribution = pkg_resources.get_distribution('django-markymark')

version = distribution.version
release = version

exclude_patterns = []

pygments_style = 'sphinx'

html_domain_indices = True

if sphinx_rtd_theme:
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
else:
    html_theme = 'default'

html_static_path = ['_static']

htmlhelp_basename = 'markymarkdoc'


latex_elements = {}

latex_documents = [
  ('index', 'markymark.tex', u'markymark Documentation',
   u'Moccu GmbH \\& Co. KG', 'manual'),
]

man_pages = [
    ('index', 'markymark', u'markymark Documentation',
     [u'Moccu GmbH & Co. KG'], 1)
]

texinfo_documents = [
  ('index', 'markymark', u'markymark Documentation',
   u'Moccu GmbH & Co. KG', 'markymark', 'One line description of project.',
   'Miscellaneous'),
]
