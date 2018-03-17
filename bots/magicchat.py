import zulip

class magicchat(object):
    '''
    A docstring documenting this bot.
    '''

    def usage(self):
        return '''I am magicChat bot, built using python and Zulip API'''

    # This handles the message that the chatbot recieves
    def handle_message(self, message, bot_handler):
	# echo back whatever bot is asked
        bot_handler.send_reply(message, message["content"])



handler_class = magicchat
