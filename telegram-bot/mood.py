import indicoio

indicoio.config.api_key = 'b09e30618dac907d86f8afb6dbeff68e'


# dictOfLists is supplied -> dictOfList with usr:mood is returned
def evaluate(dictOfList):
	result = dict()
	for key in dictOfList:
		result[key] = evalMood(dictOfList[key])
pass

# listOfStrings is supplied -> mood of those strings
def evalMood(listOfStr):
	stats=indicoio.emotion(str(listOfStr))
	return max(stats, key=stats.get)
pass


# group=dict()
# user_chat = dict()
#
# for x in range(len(l)):
# 	v = l[x]['id']
# 	if(v[-4] == 'g'):
# 		group[l[x]['contact']] = l[x]['messages']
# 	elif :
# 		user_chat[l[x]['contact']] = l[x]['messages']
#
#
#
#
#
# group_message = dict()
# user_message = dict()
#
# for key in group:
# 	lo = len(group[key])
# 	li = []
# 	for x in range(lo):
# 		li.append(group[key][x]['message'])
# 		group_message[key] = li
# print(group_message)
#
# for key in user_chat:
# 	uo = len(user_chat[key])
# 	ui = []
# 	for x in range(uo):
# 		ui.append(user_chat[key][x]['message'])
# 		user_message[key] = ui
#
#
# list_of_mesg = []
# for key in group_message:
# 	v = len(group_message[key])
# 	text=""
# 	for x in group_message[key]:
# 		text += x
# 	text += "."
# 	list_of_mesg.append(textrank(text))
# 	text=""
#
#
# for key in user_message:
# 	if(len(user_message[key]) >= 5):
# 		text = ""
# 		mod = len(user_message[key])%5
# 		for y in range(0,len(user_message[key])-mod,5):
# 			text+=user_message[key][y]+"."
# 			text+=user_message[key][y+1]+"."
# 			text+=user_message[key][y+2]+"."
# 			text+=user_message[key][y+3]+"."
# 			text+=user_message[key][y+4]+"."
# 			stats=indicoio.emotion(text)
# 			print(max(stats, key=stats.get))
# 			text=""
# 		for y in range(mod):
# 			text+=user_message[key][y]+"."
# 			indicoio.emotion(text)
# 			text=""
# 	else:
# 		mod = len(user_message[key])%2
# 		for y in range(0,len(user_message[key])-mod,2):
# 			text+=user_message[key][y]+"."
# 			text+=user_message[key][y+1]+"."
# 			stats=indicoio.emotion(text)
# 			print(max(stats, key=stats.get))
# 			text=""
# 		if(mod !=0):
# 			stats=indicoio.emotion(user_message[key][mod])
# 			print(max(stats, key=stats.get))
#
#
#
# def translate_text(_from='en',_to='en'):
# 	for x in range(len(list_of_mesg)):
# 		for y in range(len(list_of_mesg[x])):
# 			en_blob = TextBlob(list_of_mesg[x][y])
# 			en_blob.translate(from_lang=_from,to=_to)
