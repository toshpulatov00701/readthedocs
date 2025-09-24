# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'myAI'
copyright = '2025, Abduhalil'
author = 'Abduhalil'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    # 'sphinx.ext.autodoc',     # Agar docstringlardan API hosil qilmoqchi bo‘lsangiz
    # 'sphinx.ext.napoleon',    # Google/NumPy style docstringlar uchun
    'myst_parser',            # Agar Markdown ishlatmoqchi bo‘lsangiz
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'   # Read the Docs rasmi temasi

html_static_path = ['_static']
html_css_files = ['custom.css']
html_show_sourcelink = False

# Maxsus logo (rasmni docs/_static/ ichiga joylashtiring)
# html_logo = "_static/mylogo.png"

# Ixtiyoriy sozlamalar (navigatsiya uchun qulaylik)
html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 3,
}