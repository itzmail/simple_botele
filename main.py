from logging import Filter
from turtle import update
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5207594806:AAGGGcfejx-qN2LFUq_vrzyuOoZj9Py09K8", use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hi! In My Simple Telegram Bot, this bot i make for practice not for bussines. For more menu you can click /help"
    )

def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /youtube - To get the youtube URL
    /linkedin - To get the LinkedIn profile URL
    /gmail - To get gmail URL
    /geeks - To get the GeeksforGeeks URL"""
    )

def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text("ismailnuralam@gmail.com")

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry dude, i can't recognize you, you said '%s'" % update.message.text
    )

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text
    )

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))

# Filters Command tidak dikenal
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

# Filters pesan tidak dikenal
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()