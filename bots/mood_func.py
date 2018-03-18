import indicoio
indicoio.config.api_key = 'b09e30618dac907d86f8afb6dbeff68e'


def mood(user_message):
	for key in user_message:
	if(len(user_message[key]) >= 5):
		text = ""
		mod = len(user_message[key])%5
		for y in range(0,len(user_message[key])-mod,5):
			text+=user_message[key][y]+"."
			text+=user_message[key][y+1]+"."
			text+=user_message[key][y+2]+"."
			text+=user_message[key][y+3]+"."
			text+=user_message[key][y+4]+"."
			stats=indicoio.emotion(text)
			print(max(stats, key=stats.get))
			text=""
		for y in range(mod):
			text+=user_message[key][y]+"."
			indicoio.emotion(text)
			text=""
	else:
		mod = len(user_message[key])%2
		for y in range(0,len(user_message[key])-mod,2):
			text=""
			text+=user_message[key][y]+"."
			text+=user_message[key][y+1]+"."
			stats=indicoio.emotion(text)
			print(max(stats, key=stats.get))
			text=""
		if(mod !=0):
			stats=indicoio.emotion(user_message[key][mod])
			print(max(stats, key=stats.get))
