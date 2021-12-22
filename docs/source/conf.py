# Configuration file for the Sphinx documentation builder.

# -- Project information

project = ' CFGS Administración de Sistemas Operativos en Red'
copyright = '2021, Pablo González, CC BY 4.0'
author = 'Pablo González Troyano - 2º ASIR - IES VILLABLANCA'

release = '0.4'
version = '0.4'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Modificar el FAVICON -- 
html_favicon = 'https://avatars.githubusercontent.com/u/44492590?v=4'

# -- Quitar las flechitas entre las páginas -- 
html_theme_options = {
    'prev_next_buttons_location': 'none',
    'analytics_id': 'UA-97273241-13',
    'analytics_anonymize_ip': True,
    'canonical_url': 'https://asir.gonzaleztroyano.es/',
    'collapse_navigation': True
}   

html_context = {
  'display_github': True,
  'github_user': 'gonzaleztroyano',
  'github_repo': 'ASIR2-DOCS-MAIN',
  'github_version': 'main/docs/source/'
}
