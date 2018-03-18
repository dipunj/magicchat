from summarizer import textrank
'''
def summarize(group_message):
	for key in group_message:
	v = len(group_message[key])
	text=""
	for x in group_message[key]:
		text += x
	text += "."
	list_of_mesg.append(textrank(text))
	text=""
	return list_of_mesg
'''	
def summarize(group_message,group_name):
	list_of_mesg = []
	group_chat = dict()
	for key in group_message:
		v = len(group_message[key])
		text=""
		for x in group_message[key]:
			text += x
		text += "."
		list_of_mesg = textrank(text)
		print(list_of_mesg)
		group_chat[key] = list_of_mesg
		text=""
	return group_chat[group_name]
