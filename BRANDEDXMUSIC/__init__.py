from BRANDEDXMUSIC.core.bot import Anony
from BRANDEDXMUSIC.core.dir import dirr
from BRANDEDXMUSIC.core.git import git
from BRANDEDXMUSIC.core.userbot import Userbot
from BRANDEDXMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
