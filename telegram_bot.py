import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from binance_coins import new_list

telegram_bot_token = "1946817442:AAH71fx0Mlp0K3-YFH00n6jgBRCfa6haPwE"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    chat_id = update.effective_chat.id
    message = ""

    data = new_list()
    message = f"{data}"
    context.bot.send_message(chat_id = chat_id, text = message)


dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()