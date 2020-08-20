import flask_calendar.constants as constants

DEBUG = True
DATA_FOLDER = "data"
USERS_DATA_FOLDER = "users"
BASE_URL = "http://127.0.0.1:5000"
MIN_YEAR = 2017
MAX_YEAR = 2100
PASSWORD_SALT = "something random and full of non-standard characters"
HOST_IP = "0.0.0.0"  # set to None for production
LOCALE = "fr_FR.UTF-8"
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
TIMEZONE = "Europe/Paris"

WEEK_STARTING_DAY = constants.WEEK_START_DAY_SUNDAY

MONTHS_TO_EXPORT = 6  # currently only used for ICS export

FEATURE_FLAG_ICAL_EXPORT = False

# (base ^ attempts ) second delays between failed logins
FAILED_LOGIN_DELAY_BASE = 2

# If true, will automatically decorate hyperlinks with <a> tags upon rendering them
AUTO_DECORATE_TASK_DETAILS_HYPERLINK = True

SHOW_VIEW_PAST_BUTTON = False

# Of use if SHOW_VIEW_PAST_BUTTON is False
HIDE_PAST_TASKS = False

# days past to keep hidden tasks (future ones always kept) counting all months as 31 days long
DAYS_PAST_TO_KEEP_HIDDEN_TASKS = 62

# Cookies config
COOKIE_HTTPS_ONLY = False
COOKIE_SAMESITE_POLICY = "Lax"

# If to render emoji buttons at the task create/edit page
EMOJIS_ENABLED = True

# Colors for new task buttons
BUTTON_CUSTOM_COLOR_VALUE = "#3EB34F"
BUTTONS_COLORS_LIST = (
    ("#FF4848", "Rouge"),
    ("#3EB34F", "Vert"),
    ("#2966B8", "Bleu"),
    ("#808080", "Gris"),
    ("#B05F3C", "Marron"),
    ("#9588EC", "Violet"),
    ("#F2981A", "Orange"),
    ("#3D3D3D", "Noir"),
)

# Emojis for new task buttons
BUTTONS_EMOJIS_LIST = (
    "💬",
    "📞",
    "🍔",
    "🍺",
    "📽️",
    "🎂",
    "🏖️",
    "💻",
    "📔",
    "✂️",
    "🚂",
    "🏡",
    "🐶",
    "🐱",
)
