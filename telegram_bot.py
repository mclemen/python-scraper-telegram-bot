import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from coinbase import new_list

telegram_bot_token = "1946817442:AAEDoe8iVWsteUv2ctTxssBQgN9l67VlJ_w"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    chat_id = update.effective_chat.id
    message = ""

    data = new_list()
    message = f"New Coins: {data}"
    context.bot.send_message(chat_id = chat_id, text = message)

def shutdown():
    updater.stop()
    updater.is_idle = False
def stop(bot, update):
    threading.Thread(target=shutdown).start()

dispatcher.add_handler(CommandHandler("start", start))
updater.start_polling()
updater.dispatcher.add_handler(CommandHandler('stop', stop))