from SONALI.core.bot import RAUSHAN
from SONALI.core.dir import dirr
from SONALI.core.git import git
from SONALI.core.userbot import Userbot
from SONALI.misc import dbb, heroku
from SafoneAPI import SafoneAPI

# Initialize directories, git config, DB, and Heroku
dirr()
git()
dbb()
heroku()

# Initialize main bot and APIs
app = RAUSHAN()
api = SafoneAPI()
userbot = Userbot()

# Import platform APIs
from SONALI.platforms import (
    AppleAPI,
    CarbonAPI,
    SoundAPI,
    SpotifyAPI,
    RessoAPI,
    TeleAPI,
    YouTubeAPI,
)

# Initialize platform API clients
Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()