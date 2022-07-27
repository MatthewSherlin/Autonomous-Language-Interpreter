## ALI: Autonomous Ianguage interpreter. 
ALI was developed as an open-source tool for use in hospitals to bridge language barriers in the medical environment. It is designed to work similarly to a live interpreter who would be present for the conversation. Not all medical facilities have access to live interpreters, so we created ALI in hopes to aid where interpreters are not accessible. ALI is able to not only interpret conversations as they happen, but ALI also features several components that may be useful for a medical professional interacting with a patient. These additional features include a database to log transcibed conversations, as well as a highlight button to grab key information from conversations. These conversations and highlights are stored for future reference, up to 24 hours. ALI also includes a sidebar menu to create SOAP notes from the information gained during conversation. Additionally, it is possible to use ALI to create discharge instructions for a given patient. Finally, ALI can also be used for basic translations of information to be stored for the patient.

All of these features are intended to aid a professional user in interpretation, translation and transcription of conversations. All information presented in ALI should be checked for accuracy by the professional user.

ALI is a complex program that uses several APIs and specific modules in order to function correctly. The following modules must be installed to properly run ALI:

## Full Installation

Getting started:

- Install python and pip

Install server libraries/extensions in terminal:
```
pip install bottle
pip install mysql-connector-python
```

Open a clean folder and set up virtual environment:
```
cd your-project
py -m venv env
```

Activate the virtual environment:
```
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

To run the software:
```
py server.py
```

## Required for Usage
In order to run ALI, you will need to sign up for a Google Cloud API account (https://cloud.google.com/apis).
Here, you will need to enable 3 different Google Cloud APIs:
```
Cloud Text-to-Speech API
Cloud Translation API
Cloud Speech-to-Text API
```
These are required for interpretations, transcriptions and translations.
You will need to create a file in the main directory named "ServiceKey.json" and enter in your Google Cloud API key.

