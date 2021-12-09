A.L.I. is an autonomous language interpreter. It was developed as a tool for use in hospitals to bridge language barriers in the medical environment. It is designed to work similarly to a live interpreter who would normally be present for the conversation. A.L.I. is able to not only translate conversations as they happen, but also features several components that may be useful for a medical professional when interacting with a patient. These include a database to log conversations as well as highlight key parts of conversations. These conversations and highlights are stored for future reference, up to 24 hours. In addition, A.L.I includes a menu to create SOAP notes in regards to a conversation. Additionally, it is possible to use A.L.I. to create discharge instructions for a given patient. 

All of these features are intended to aid a professional user in interpretation, and all information presented in A.L.I. should be checked for accuracy by the professional user.

There are several known issues with A.L.I. These include:
problems with using space to end the interpretation process.
problems with French accents not displaying correctly.
problems with spaces not appearing correctly in translated text.
Occasional bugs with the Google APIs used in A.L.I.

It is a complex program that uses several APIs and specific modules in order to function correctly. The following modules must be installed to properly run A.L.I:

How to set up virtual environment:
cd your-project
py -m venv env
.\env\Scripts\activate

You will need the following python modules to be installed to run our software. Use the following commands in your terminal:

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
