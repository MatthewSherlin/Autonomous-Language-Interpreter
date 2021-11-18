from google.cloud import speech
from google.cloud import translate_v2 as translate
from google.cloud import texttospeech # outdated or incomplete comparing to v1
from google.cloud import texttospeech_v1
from bs4 import BeautifulSoup

import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r".\\ServiceKey.json"

translate_client = translate.Client()
client = texttospeech_v1.TextToSpeechClient()

def takeHomeTranslate(var1, text):
    with open('templates/takeHome.html', 'r') as file:
        soup = BeautifulSoup(file.read(), "lxml") 
        output = translate_client.translate(text, target_language=var1)
        soup.find("textarea", {"id": "t1"}).append(text)
        soup.find("textarea", {"id": "t2"}).append(output['translatedText'])
        file.close()
        

    savechanges = soup.prettify("utf-8")
    with open("templates/takeHome.html", "wb") as file:
        file.write(savechanges)
        file.close()


def clearTextTags(): 
    with open('templates/takeHome.html', 'r') as file:
        soup = BeautifulSoup(file.read(), "lxml") 
        soup.find("textarea", {"id": "t1"}).clear()
        soup.find("textarea", {"id": "t2"}).clear()
        file.close()

    savechanges = soup.prettify("utf-8")
    with open("templates/takeHome.html", "wb") as file:
        file.write(savechanges)
        file.close()

