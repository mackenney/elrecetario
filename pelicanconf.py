AUTHOR = 'Ignacio Mackenney'
SITENAME = 'El Recetario'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Santiago'

DEFAULT_LANG = 'es'

THEME = 'themes/elegant'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

AUTHORS = {
    "Guille": {
        "blurb": "Entusiasta de la comida",
    },
    "Ignacio": {
        "blurb": "Vegano nerd"
    }
}

LANDING_PAGE_TITLE = "Un recetario armado entre amigos"

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
