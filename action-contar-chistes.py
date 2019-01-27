#!/usr/bin/env python2
from hermes_python.hermes import Hermes 
import requests
import html2text

MQTT_IP_ADDR = "localhost" 
MQTT_PORT = 1883 
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT)) 


def extraer_chiste():
    url = "http://www.chistes.com/M//ChisteAlAzar.aspx?n=3"
    response = requests.get(url)
    webContent = response.read()
    webContent2 = webContent.decode().replace('<div class="chiste">','@',1)
    webContent3 = webContent2.split('@')
    webContent4 = webContent3[1].replace('</div>','@',1)
    chiste = webContent4.split('@')
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
