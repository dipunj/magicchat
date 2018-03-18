from typing import Any, Dict
import sys,os
sys.path.insert(0,os.getcwd())
from webwhatsapi import WhatsAPIDriver
from summarize_func import summarize
from translate_func import translate_text
from textblob import TextBlob
from googletrans import Translator
import indicoio
indicoio.config.api_key = 'b09e30618dac907d86f8afb6dbeff68e'


class magicchat(object):
  collection=[]
  global driver
  driver = WhatsAPIDriver(username="Phoenix")
  
  
    

  def usage(self):
    return "I am here to help you"
    

  def handle_message(self, message, bot_handler):
    content = message['content'].split()
    
    
    l = driver.view_unread()
    print(l)
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
        
    for key in user_chat:
	    uo = len(user_chat[key])
	    ui = []
	    for x in range(uo):
	      ui.append(user_chat[key][x]['message'])
	      user_message[key] = ui

    if(content[0]=='juice'):
      list_of_mesgs = summarize(group_message,content[1])
      bot_handler.send_reply(message,list_of_mesgs)
    elif(content[0]=='mood'):
      final_val=""
      username=str(content[1])
      for key in user_message:
        if(key==username):
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
              final_val=(max(stats, key=stats.get))
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
              final_val=(max(stats, key=stats.get))
              text=""
            if(mod !=0):
              stats=indicoio.emotion(user_message[key][mod])
              final_val=(max(stats, key=stats.get))
        bot_handler.send_reply(message,final_val)
    elif(content[0]=='translate'):
      lang=content[1]
      stry=""
      length=len(content)
      #print("length=",length)
      for i in range(2,length):
        stry+=str(content[i])+" "
      print(lang)
      print(stry)
      print(type(stry))
      # en_blob = TextBlob(stry)
      # output=en_blob.translate(from_lang='en',to=lang)
      translated = Translator().translate(str(stry),lang)
      bot_handler.send_reply(message,str(translated))
    else:
      bot_handler.send_reply(message,"no valid help can be provided :(")


  '''
    results=[]


    new_content = ''
    for idx, result in enumerate(results, 1):
     new_content += ((str(idx)) if len(results) > 1 else '') + result + '\n'

    bot_handler.send_reply(message, new_content)
  '''

handler_class = magicchat
