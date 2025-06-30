import os
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get from my.telegram.org
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get from @BotFather
BOT_TOKEN = getenv("BOT_TOKEN")

# Bot and Owner info
OWNER_USERNAME = getenv("OWNER_USERNAME", "ll_ALPHA_BABY_lll")
BOT_USERNAME = getenv("BOT_USERNAME", "Sonali_Music_bot")
BOT_NAME = getenv("BOT_NAME", "SONALI")
OWNER_ID = int(getenv("OWNER_ID", 6051510669))

# OpenAI key
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "")

# MongoDB
MONGO_DB_URI = getenv("MONGO_DB_URI")

# Logging
LOGGER_ID = int(getenv("LOGGER_ID", -1002267586320))

# Heroku
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# Repo
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Gxinfinity/ANYA_MUSIC")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN")

# Support
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/who_cares_qt")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Destiny_Infinity_Og")

# Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET")

# Limits
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# Strings
STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")

# Filters
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Images
START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/1951b91d265c94bb90d2f-70bea2d338ca641e75.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/9cevdg.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/i493lf.jpg"
STATS_IMG_URL = "https://files.catbox.moe/i0qmgf.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/8e3552aa743ffdb6f18c9.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/8e3552aa743ffdb6f18c9.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"

# Time conversion
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# URL validation
if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - SUPPORT_CHANNEL must start with https://")

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - SUPPORT_CHAT must start with https://")