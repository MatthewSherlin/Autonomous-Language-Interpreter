## ALI is an autonomous language interpreter. 
ALI was developed as a tool for use in hospitals to bridge language barriers in the medical environment. It is designed to work similarly to a live interpreter who would normally be present for the conversation. ALI is able to not only translate conversations as they happen, but also features several components that may be useful for a medical professional when interacting with a patient. These include a database to log conversations as well as highlight key parts of conversations. These conversations and highlights are stored for future reference, up to 24 hours. In addition, ALI includes a menu to create SOAP notes in regards to a conversation. Additionally, it is possible to use ALI to create discharge instructions for a given patient. 

All of these features are intended to aid a professional user in interpretation, and all information presented in ALI should be checked for accuracy by the professional user.

It is a complex program that uses several APIs and specific modules in order to function correctly. The following modules must be installed to properly run A.L.I:

## Full Installation

How to set up virtual environment:
```
cd your-project
py -m venv env
.\env\Scripts\activate
```

You will need the following python modules to be installed to run our software. Use the following commands in your terminal:

```
pip install pandas
pip install pipwin
pipwin install pyaudio
pip install google-cloud-speech
pip install google-cloud-translate
pip install Flask
pip install lxml
pip install playsound
pip install google-cloud-texttospeech
pip install keyboard
```

In order to run the software:

```
py server.py
```
