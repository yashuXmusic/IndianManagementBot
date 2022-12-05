import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "17273188")
    API_HASH = getenv("API_HASH", "a2e5bb2b69d13ba7553941af16cc2d5b")
    TOKEN = getenv("TOKEN", "5950341199:AAF5ghNkGHqbmf-4VIxZnBdMt94mz34ufv4")
    OWNER_ID = getenv("OWNER_ID", "5151455635")
    STRING_SESSION = getenv("STRING_SESSION", "AQByarGHtJyZxJC639ppzCFAeIpx7_eKspqQPpRqVeNeVoaz_Dj_aWcYtCsAmXq772SS5722QR3-FtU7ZesEUnhVuCJKFkf_NxK076j-sveUs3S_uz0XhwlBy0rQXjPyDfvsbGYa6sfQYpBb_PNvIILCaSNHkGagnWBzndVzoSMwEE5vFnwVTr2dI4jYyJUNOpWgqZuRuTy4Ghyc0ra4342zStFqT6lCB4XcQ2nR0L3NIrHOOYqsmbZxti5YA2oYB9MmJSWhu99HLYzhqgKrFVahHEeYQsEGOX8M2Spky3MZ3UZT0U6jgqouWJS_Lblh2RvlsxMBK2cQS_Y-99goCIBeAAAAAUQaO7AA")
    OWNER_USERNAME = getenv("OWNER_USERNAME", "NULL_CODER_BOT")
    DB_URI = getenv("DATABASE_URL", "mongodb+srv://yashu:yashu@cluster0.knhecdn.mongodb.net/?retryWrites=true&w=majority")
    DB_URI = DB_URI.replace("postgres", "postgresql")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001236143586")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001236143586")
    SYS_ADMIN = getenv("SYS_ADMIN", "5151455635")
    DEV_USERS = getenv("DEV_USERS", "5151455635")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5151455635").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "5151455635").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
