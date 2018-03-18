from textblob import TextBlob
'''
def translate_text_group(_from='en',_to='hi',list_of_mesg):
	for x in range(len(list_of_mesg)):
		for y in range(len(list_of_mesg[x])):
			en_blob = TextBlob(list_of_mesg[x][y])
			en_blob.translate(from_lang=_from,to=_to)
'''			
def translate_text(frm,too,message):
	en_blob = TextBlob(message)
	return en_blob.translate(from_lang=frm,to=too)
	
