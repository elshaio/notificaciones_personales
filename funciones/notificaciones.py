import config
from telegram import Bot


def mensaje(text):
    bot = Bot(config.token)
    bot.send_message(
        chat_id=config.chat_id,
        text=text)
