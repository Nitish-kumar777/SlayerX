import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Filled environment values
API_ID = 24771124
API_HASH = "b3f70c241c23f11c3dc8ff76bbe1a9e9"
BOT_TOKEN = "7540382306:AAFlbFzAbJZmJvKaMXBVpMQU1-9a4v_HOQM"
LOGGER_ID = -1001910615796
MONGO_DB_URI = "mongodb+srv://adhikansharodhiyaroshiya:J6qFA7fzM2rLN9uv@cluster0.ycxcxiw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
OWNER_ID = 5425656625
STRING_SESSION = "BQAPxRPqHXEGffPrQ6FgD7mitrbC8jry7rrelYPVC119V4tl7sG5mFa2v4ll0-AdlXGsmEQGK8A6Lu-0d5wkZ4pVGs6YBCAf_6klyj618xaWBhmdAdoBxDaMVeogg-mNKMIRoB5ILig-n8hBET0QQJGlLpNeXjUcEIHqRzD_TLWiY4I5DIhbyExlunUshurMLI4pPRRmy_y8x-_XrQLa-TBCRrCmeANw2JHEN5pE-O9TU-fLpvJRRQAnGbsTOAznSRr1G061kTpEJrLJOdUcihDJ7WTfZoXZf0ctC0ng5rZ2X5wfMpkf3bJHCCmYwtEKM5qJ98cWIxnbkVaCAsY0Mct1AAAAAbbrERYA"

# Optional environment values
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
GIT_TOKEN = getenv("GIT_TOKEN", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 180))
DURATION_LIMIT = int(DURATION_LIMIT_MIN * 60)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Learningbots79/LB_Music")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ANIMEVERSEDD")
SUPPORT_CHAT = getenv("SUPPORT_GROUP", "https://t.me/ANIMEVERSEDD")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Spotify credentials
SPOTIFY_CLIENT_ID = getenv("Sb8a10b88f4d949b0bab917b53b29a2e4")
SPOTIFY_CLIENT_SECRET = getenv("2fcb52035b9c4a14a73189a30cf38082")

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# File size limits
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# Images
START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/214f53702f788c668e294.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/214f53702f788c668e294.jpg")

# Check URLs
if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL URL is invalid.")

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Your SUPPORT_CHAT URL is invalid.")
