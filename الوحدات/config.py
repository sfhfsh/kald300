import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "10394604"))
API_HASH = getenv("API_HASH", "0938b69d0f0da9a0ff3199dd5823b5e7")
BOT_TOKEN = getenv("BOT_TOKEN", "6279433332:AAHgwjlfOwSA1O5cCoE0sRgNmHxlzBma4ds")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "1ApWapzMBu53vvo9O4ax_VU_IvoMIkA3xPTPgN8VsJdm9YymmDnqZYUfsX4P5EBgg1UryCWwf7iR7AycbeWnBcB5f6-8j9qeincwjxgWAjdj3FRsJPfPbyAUDS4CXlI4NlhnNQIrrHEV4YSPsmsETSjOy2bUI-l7Du4PxL_LvXd7fqkBCpJ8tyULB-tztBoFyIJFoze7CD571CSTHilUoyvphdOBLq85rjvyycuuGASAFcbpznfZ-wDmmsyolyTxrkqkrpp0xkRQL5Xi86YPxpZDlOWr4VLGUcgf-ynMXUhm_rpByChWdu90W4bkTU6I0tUAKO1UopYo0Ktq6Mdz08bf0ZcRQJ78=")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
