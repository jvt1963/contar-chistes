#!/usr/bin/env python3
from hermes_python.hermes import Hermes 
import requests
import html2text
from html.parser import HTMLParser

MQTT_IP_ADDR = "localhost" 
MQTT_PORT = 1883 
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT)) 


def extraer_chiste():
    url = "http://www.chistes.com/M//ChisteAlAzar.aspx?n=3"
    response = requests.get(url)
    webContent = response.text
    h = HTMLParser()
    webContent = h.unescape(webContent)
    webContent = webContent.replace('<div class="chiste">','@',1)
    webContent = webContent.split('@')
    webContent = webContent[1].replace('</div>','@',1)
    chiste = webContent.split('@')
    texto = html2text.html2text(chiste[0])
    return texto

def intent_received(hermes, intent_message):
    
    if intent_message.intent.intent_name == 'jaimevegas:PedirChiste':
        sentence = extraer_chiste()
                        
    else:
        return
    
    hermes.publish_end_session(intent_message.session_id, sentence)
    
    
with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()
