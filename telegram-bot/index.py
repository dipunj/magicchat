#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Modules
from uuid import uuid4
from telegram.utils.helpers import escape_markdown
from telegram import InlineQueryResultArticle,ParseMode,InputTextMessageContent
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler

# Custom modules
from handler import *

# Enable logging
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("591691335:AAGIFic5HZvXu29H3jiZ0JOYNjV4x-5xUbs")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("juice", juice))
    dp.add_handler(CommandHandler("mood", mood))
    dp.add_handler(CommandHandler("translate", translate, pass_args=True))
    dp.add_handler(InlineQueryHandler(formater))

    # on noncommand i.e message - driver the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, driver))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
