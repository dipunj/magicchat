from webwhatsapi import WhatsAPIDriver
driver = WhatsAPIDriver(username="Phoenix")
from summarizer import textrank

while True:
	inp = input("Is your phone connected y/n ?")
	if inp == "y":
		break
print("Phone Connected!!")
l = driver.view_unread()
print(l)
group=dict()
for x in range(len(l)):
	v = l[x]['id']
	if(v[-4] == 'g'):
		group[l[x]['contact']] = l[x]['messages']
group_message = dict()
for key in group:
	lo = len(group[key])
	li = []
	for x in range(lo):
		li.append(group[key][x]['message'])
		group_message[key] = li
print(group_message)

for key in group_message:
	v = len(group_message[key])
	text=""
	for x in group_message[key]:
		text += x
	text += "."
	textrank(text)
	text=""


