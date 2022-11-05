from os import getenv

from dotenv import load_dotenv

load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', 'session')
BOT_TOKEN = getenv('BOT_TOKEN', '5749384137:AAFFMFssI6O_LZ9F110EZWsYIW9UuwYuZEU')
API_ID = int(getenv('API_ID', '23989721'))
API_HASH = getenv('API_HASH', '7877d54731b7979f7a55457f6b5b088e')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '7'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ !').split())
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '1892226702').split()))
