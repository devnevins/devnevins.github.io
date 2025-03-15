AUTHOR = 'Dean Nevins'
SITENAME = 'devnevins'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

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

# Should be 5
DEFAULT_PAGINATION = 5

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'uncategorized'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
PAGE_PATHS = ['pages']
SUMMARY_MAX_LENGTH = 50

# Regenerate everything every time. Change to True when done experimenting.
LOAD_CONTENT_CACHE = False

# Used to support the pelican-bootstrap3 theme
#THEME = "basic"

#JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
