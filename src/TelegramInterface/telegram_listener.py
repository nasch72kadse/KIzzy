from utils import init_sqlite_table
import os
from TelegramInterface import TelegramInterface


def telegram_listener(config_path):
    telegram_interface = TelegramInterface(config_path)
    bot = telegram_interface.bot

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(self, message):
        bot.reply_to(message, "Hello! I am KIzzy!")
        # Initialize DB if it does not exist yet
        if not os.path.isfile("telegram_data.db"):
            init_sqlite_table("telegram_data.db")

    @bot.message_handler(func=lambda m: True)
    def echo_all(message):
        chat_id = message.chat.id
        return_message = handle_message(message, chat_id)
        bot.reply_to(message, return_message)

    bot.polling()
