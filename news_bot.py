from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

BOT_TOKEN = "123456789:AAABCDeFGhiJKLmnoPQRstuVWxyZ"  # replace with your full real token

def reply_hello(update: Update, context: CallbackContext):
    update.message.reply_text("Hello World")

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_hello))

print("Bot started...")
updater.start_polling()
updater.idle()
