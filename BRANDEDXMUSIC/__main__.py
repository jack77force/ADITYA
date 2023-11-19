import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from BRANDEDXMUSIC import LOGGER, app, userbot
from BRANDEDXMUSIC.core.call import Anony
from BRANDEDXMUSIC.misc import sudo
from BRANDEDXMUSIC.plugins import ALL_MODULES
from BRANDEDXMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("BRANDEDXMUSIC.plugins" + all_module)
    LOGGER("BRANDEDXMUSIC.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Anony.start()
    try:
        await Anony.stream_call("https://graph.org/file/e7753627c90e83012848d.mp4")
    except NoActiveGroupCall:
        LOGGER("BRANDEDXMUSIC").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Anony.decorators()
    LOGGER("BRANDEDXMUSIC").info(
        "@BRANDED_WORLD"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("BRANDEDXMUSIC").info("Stopping BRANSED Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
