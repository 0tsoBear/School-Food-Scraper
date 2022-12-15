import requests
import GetMenu
import datetime
today = (datetime.date.today())

TOKEN = "5111964806:AAHQO0JiOB7XP1KZ30mo1Nb61lCi-ct0qMQ"
chat_id = "-801445102"
message = GetMenu.ruokalista(today, "espoo_olarinkoulu")
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json()) # this sends the message