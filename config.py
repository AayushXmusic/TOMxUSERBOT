import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "21422769")) #optional
API_HASH = getenv("API_HASH", "e1c78c5e5abe5308feac03b5bf52989e") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6351799366").split()))
OWNER_ID = int(getenv("OWNER_ID","6351799366"))
MONGO_URL = getenv("MONGO_URL","mongodb+srv://venomridee0001:<password>@cluster0.ivgjrqj.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6499928811:AAH1fdtDXFtcJQ8t58KLsxxNw3pmpl3ocaI")
ALIVE_PIC = getenv("ALIVE_PIC", "https://graph.org/file/7687974685b539af12cb5.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP","https://t.me/TomXuserbott")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQFG4rEAVwPxx6tStxDpKYLaZGGN_fRAstOOyN93H9MLvIFBzYK-Uy5ev9lowH_3h_qWttrIdnSUsgyYwwoJjCap8iM6Z6u24acYGMMA_vukTORCpKBJODU-cpr7KeOFbtFEopqUQHtB9psEjrYuAkpK6lrlg8xILfCS946eMuR")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
