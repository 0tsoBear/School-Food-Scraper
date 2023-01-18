# Import necessary modules
import requests
import GetMenu
import datetime
from os import getenv
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get current date
today = (datetime.date.today())

# Get Telegram token and chat ID from environment variables
TOKEN = getenv("TELEGRAMTOKEN")
chat_id = getenv("TELEGRAMCHATID")

# Generate message using GetMenu module
message = GetMenu.ruokalista(today, "espoo_olarinkoulu")

# Construct URL for Telegram API
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"

# Send message and print response as JSON
print(requests.get(url).json())