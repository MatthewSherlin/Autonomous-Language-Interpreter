from __future__ import division

import os
import re
import sys
import pandas as pd

from google.cloud import speech
from google.cloud import translate_v2 as translate
from google.cloud import texttospeech # outdated or incomplete comparing to v1
from google.cloud import texttospeech_v1
from playsound import playsound #play mp3 files

#-----------------------credential[path] needs to be change per user testing-------------------------------
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\Matthew Sherlin\Desktop\APIKey\myServiceKey.json"
#------------------------------------------------^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^----

import pyaudio
from six.moves import queue

#set output file path to reduce error risk //CHANGE TO FILE PATH INSIDE ALI FOLDER//
path = r"C:\\Users\\Matthew Sherlin\\Desktop\\ALI-Software\\env\\Capstone-2021\\ALI-Output\\output.mp3"
assert os.path.isfile(path)

#define parameters for multi-use purpose
initalLanguage = 'es'
targetLanguage= 'en'
languageCode= 'en' #language of the accent for output speech

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms

# instantiate clients for translate and T2S
translate_client = translate.Client()
client = texttospeech_v1.TextToSpeechClient()

class MicrophoneStream(object):
    """Opens a recording stream as a generator yielding the audio chunks."""

    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk

        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            # The API currently only supports 1-channel (mono) audio
            # https://goo.gl/z757pE
            channels=1,
            rate=self._rate,
            input=True,
            frames_per_buffer=self._chunk,
            # Run the audio stream asynchronously to fill the buffer object.
            # This is necessary so that the input device's buffer doesn't
            # overflow while the calling thread makes network requests, etc.
            stream_callback=self._fill_buffer,
        )

        self.closed = False

        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the buffer."""
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            # Now consume whatever other data's still buffered.
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b"".join(data)


def listen_print_loop(responses):
    
    """Iterates through server responses and prints them.
    The responses passed is a generator that will block until a response
    is provided by the server.
    Each response may contain multiple results, and each result may contain
    multiple alternatives; for details, see https://goo.gl/tjCPAU.  Here we
    print only the transcription for the top alternative of the top result.
    In this case, responses are provided for interim results as well. If the
    response is an interim one, print a line feed at the end of it, to allow
    the next result to overwrite it, until the response is a final one. For the
    final one, print a newline to preserve the finalized transcription.
    """
    num_chars_printed = 0
    for response in responses:
        if not response.results:
            continue

        # The `results` list is consecutive. For streaming, we only care about
        # the first result being considered, since once it's `is_final`, it
        # moves on to considering the next utterance.
        result = response.results[0]
        if not result.alternatives:
            continue

        # Display the transcription of the top alternative.
        transcript = result.alternatives[0].transcript

        # Display interim results, but with a carriage return at the end of the
        # line, so subsequent lines will overwrite them.
        #
        # If the previous result was longer than this one, we need to print
        # some extra spaces to overwrite the previous result
        overwrite_chars = " " * (num_chars_printed - len(transcript))

        if not result.is_final:
            sys.stdout.write(transcript + overwrite_chars + "\r")
            sys.stdout.flush()

            num_chars_printed = len(transcript)

        else:
            print(transcript + overwrite_chars)

            text = (transcript)
            target = targetLanguage

            output = translate_client.translate(text, target_language=target)
            #print(output.keys())
            #print(output.values())
            print(output['translatedText'])
            speechString = output['translatedText']
            #print input and output
            with open('transcript2.txt', 'a') as f:
                f.write(output['input'])
                f.write("\n")
                f.close()

            with open('transcript1.txt', 'a') as f:
                f.write(output['translatedText'])
                f.write("\n")
                f.close()

            voice_list = []
            for voice in client.list_voices().voices:
                voice_list.append([voice.name, voice.language_codes[0], voice.ssml_gender, voice.natural_sample_rate_hertz])
                df_voice_list = pd.DataFrame(voice_list, columns=['name', 'language code', 'ssml gender', 'hertz rate']).to_csv('Voice List.csv', index=False)

            # Set the text input to be synthesized
            quote = output['translatedText']
            synthesis_input = texttospeech_v1.SynthesisInput(text=quote)


            voice = texttospeech_v1.VoiceSelectionParams(
                language_code=languageCode, ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
            )

            voice = texttospeech_v1.VoiceSelectionParams(
                name='en-US-Standard-A,en-US,1,15000', language_code=languageCode
                # name='vi-VN-Wavenet-D', language_code="vi-VN"
            )

            # Select the type of audio file you want returned
            audio_config = texttospeech_v1.AudioConfig(
                # https://cloud.google.com/text-to-speech/docs/reference/rpc/google.cloud.texttospeech.v1#audioencoding
                audio_encoding=texttospeech_v1.AudioEncoding.MP3
            )

            # Perform the text-to-speech request on the text input with the selected voice parameters and audio file type
            response = client.synthesize_speech(
                input=synthesis_input, voice=voice, audio_config=audio_config
            )

            # The response's audio_content is binary.
            with open(path, "wb") as out:
                # Write the response to the output file.
                out.write(response.audio_content)
                print('Audio content written to file "output.mp3"')
            
            playsound(path)

            # Exit recognition if any of the transcribed phrases could be
            # one of our keywords.
            if re.search(r"\b(exit|quit)\b", transcript, re.I):
                print("Exiting..")


                break

            num_chars_printed = 0
def main():
    # See http://g.co/cloud/speech/docs/languages for a list of supported languages.

    client = speech.SpeechClient()
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=initalLanguage,
    )

    streaming_config = speech.StreamingRecognitionConfig(
        config=config, interim_results=True
    )

    with MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        requests = (
            speech.StreamingRecognizeRequest(audio_content=content)
            for content in audio_generator
        )

        responses = client.streaming_recognize(streaming_config, requests)

        # Now, put the transcription responses to use.
        listen_print_loop(responses)


if __name__ == "__main__":
    main()