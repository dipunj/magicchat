# Command Handlers for the main telegram bot
import _shared
from googletrans import Translator
import juicer,moody

# list of list of strs -> dictionary(string->listOfStr)
def list2dic(chats):
    # the result dictionary to be returned
    result = dict()
    # x -> (username, "Message")
    for x in chats:
        if x[0] in result:
            # if key is known, append new values to existing ones
            result[x[0]].append(x[1])
        else :
            # if key is new to the dictionary, add it
            result[x[0]] = [x[1]]
        pass
    return result
pass



# on invoking the /start command
def start(bot, update):
    """Send a message when the command /start is issued"""
    # bot.send_message(chat_id=458059323, text="Kesarwani")
    update.message.reply_text('Hi! I am magicchat, try /help to see what else I can do')

# invoking the /help command
def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text()

# keeps on rolling when the conversation is in progress
def driver(bot, update):
    # stores username and the text sent by that user
    _shared.chats.append([update.message.from_user.username,update.message.text])

# juices out the essential information messages stored in global variable chat
def juice(bot, update):
    # update.message.reply_text("THE JUICE IS : " + str(list2dic(_shared.chats)))
    temp = list2dic(_shared.chats)
    big = ''
    for key in temp:
        big += temp[key][0]+"."
    pass

    update.message.reply_text(str(juicer.textrank(big)))
    _shared.chats = []

# Defines error handler
def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

# Calculates mood(most likely) of all users based on their previous chats
def mood(bot, update):
    """Calculates mood"""
    update.message.reply_text(str(moody.evaluate(list2dic(_shared.chats))))
    pass

# Allows users to format their text before sending
# Invoked by calling @magicchat_Bot inline (inline bot functionality)

def formater(bot, update):
    """Handle the inline query."""
    query = update.inline_query.query
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title="Caps",
            input_message_content=InputTextMessageContent(
                query.upper())),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Bold",
            input_message_content=InputTextMessageContent(
                "*{}*".format(escape_markdown(query)),
                parse_mode=ParseMode.MARKDOWN)),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Italic",
            input_message_content=InputTextMessageContent(
                "_{}_".format(escape_markdown(query)),
                parse_mode=ParseMode.MARKDOWN))]
    update.inline_query.answer(results)


# Translates from english to a user specified language
def translate(bot,update,args):
    translated = Translator().translate(str(args[1]),str(args[0]))
    update.message.reply_text(str(translated))
pass

# <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
