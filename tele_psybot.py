import requests
import os, sys
from os.path import expanduser
from dotenv import load_dotenv

env_path = expanduser("~/.env")
load_dotenv(dotenv_path=env_path)


def telegram_bot_sendtext(bot_message):

    token = os.getenv("API_TOKEN")
    channel_id = "-1001558460086"

    send_text = (
        "https://api.telegram.org/bot"
        + token
        + "/sendMessage?chat_id="
        + channel_id
        + "&parse_mode=Markdown&text="
        + bot_message
    )

    response = requests.get(send_text)

#     print(response)

    return response.json()
