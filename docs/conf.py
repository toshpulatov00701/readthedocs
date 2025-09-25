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
    "sphinx.ext.mathjax",
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
    "navigation_depth": 2,      # faqat sahifa nomlari
    "collapse_navigation": False,
    "includehidden": True,      # yashirin toctree'lar ham bo‘lsin (kerak bo‘lsa)
    "sticky_navigation": True,
}


myst_enable_extensions = [
    "dollarmath",  # $inline$ va $$block$$ matematikalar
    "amsmath",     # \begin{align} ... \end{align} va h.k.
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}