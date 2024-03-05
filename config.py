# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import os
from distutils.util import strtobool
from os import getenv
from Uputt.helpers.cmd import cmd

from dotenv import load_dotenv

load_dotenv("config.env")


ALIVE_EMOJI = getenv("ALIVE_EMOJI", "🥵")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://telegra.ph/file/b42b7a4a22ba89287cad4.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Hey, I am alive.")
API_HASH = getenv("API_HASH", "0aa344ab03694fce2a2e6c5512dfa2d9")
API_ID = getenv("API_ID", "16810251")
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001608701614, -1001675459127, -1001473548283, -1001608701614]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "1.1.5@main"
BRANCH = getenv("BRANCH", "main") #don't change
CMD_HNDLR = cmd
OWNER_ID = getenv("OWNER_ID", "5972289509")
BOT_TOKEN = getenv("BOT_TOKEN", "7071192358:AAGlV0CXTaYvbIzugM07a_rhNRqUEuOvFkk")
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "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")
CHANNEL = getenv("CHANNEL", "chayyan")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "mongodb+srv://bgdjewi199:1234@cluster0.rpugscx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
GIT_TOKEN = getenv("GIT_TOKEN", "")
GROUP = getenv("GROUP", "jamalbotsupport")
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
REPO_URL = getenv("REPO_URL", "https://github.com/iamuput/Uputt-Pyrobot")
STRING_SESSION1 = getenv("STRING_SESSION1", "BQEAgQsAT6enQbTiYJcwNI32jWujwGH_d8rh3iGJQMGSrBqflja7izy2hcuedMxNib-eiDXyA01gOV03C3BasZGJwc30iniS601jqkKrtoeAjYPRU2JhXYFhLPcVnTC4nwRWZKXdlYKplU6ULEkhYJfromn1ichuOuAskmIeuRcVmkbKFYXfng-o_y0vfTIPkkrYTR0jIHuSY4743Ziql6qbT867xSXvPpazcazadxEjisDW9d6YHwzwbv_zep9iYU-VOEQO-EQLy7L3aYMz8gm_Wva83a01Dpm3-8SkHzDOjun2PN-LP-ERlP31S9OavPuXWivF15z2s-rdbLFtlHiLMCNTXgAAAABw9GfxAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
