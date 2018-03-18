from webwhatsapi import WhatsAPIDriver
driver = WhatsAPIDriver(username="Phoenix")
from summarize_func import summarize
from mood_func import mood
from translate_func import translate_text

while True:
	inp = input("Is your phone connected y/n ?")
	if inp == "y":
		break
print("Phone Connected!!")
l = driver.view_unread()
group=dict()
user_chat = dict()

for x in range(len(l)):
	v = l[x]['id']
	if(v[-4] == 'g'):
		group[l[x]['contact']] = l[x]['messages']
	else :
		user_chat[l[x]['contact']] = l[x]['messages']
		
group_message = dict()
user_message = dict()

for key in group:
	lo = len(group[key])
	li = []
	for x in range(lo):
		li.append(group[key][x]['message'])
		group_message[key] = li
#print("Group messages " ,group_message)

for key in user_chat:
	uo = len(user_chat[key])
	ui = []
	for x in range(uo):
		ui.append(user_chat[key][x]['message'])
		user_message[key] = ui
		
#print("user messages " ,user_message)


#summarize function
list_of_mesg = summarize(group_message)
print(list_of_mesg)

#mood generating
mood_func(user_message)

#translate
translate_text('en','hi',list_of_mesg)



