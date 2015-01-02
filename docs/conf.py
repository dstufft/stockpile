#!/usr/bin/env python3
import os

try:
    import sphinx_rtd_theme
except ImportError:
    sphinx_rtd_theme = None

# -- General configuration ------------------------------------------------

about_path = os.path.join(
    os.path.dirname(__file__), os.pardir, "stockpile", "__about__.py",
)
about = {}
with open(about_path) as fp:
    exec(fp.read(), about)


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = about["__title__"]
copyright = about["__copyright__"]

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = about["__version__"]
# The full version, including alpha/beta/rc tags.
release = about["__version__"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
if sphinx_rtd_theme:
    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
else:
    html_theme = "default"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'stockpiledoc'


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "http://docs.python.org/": None,
}
