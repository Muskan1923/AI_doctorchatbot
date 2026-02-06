from docs.conf import language
from gtts import gTTS
import elevenlabs
from elevenlabs.client import ElevenLabs
from elevenlabs import save
import os
import pygame
import time
import subprocess
import platform

pygame.init()
pygame.mixer.init()
# ELEVELABS_API_KEY=os.getenv("ELEVELABS_API_KEY")
def text_to_speech_with_gtts(input_text,output_filepath):
    language="en"
    audio_obj=gTTS(
        text=input_text,
        lang=language,
        slow=False

    )
    audio_obj.save(output_filepath)
    pygame.mixer.music.load(output_filepath)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)

def text_to_speech_with_elevenlabs(input_text,output_filepath):
    client=ElevenLabs(api_key="elevenlabs_api_key")
    audio=client.text_to_speech.convert(
        text=input_text,
        voice_id="EXAVITQu4vr4xnSDxMaL",
        output_format="mp3_22050_32",
        model_id="eleven_multilingual_v2"
    )
    save(audio,output_filepath)
    pygame.mixer.music.load(output_filepath)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)
    # os_name=platform.system()
    # try:
    #     if os_name == "Darwin":
    #         subprocess.run(['afplay',output_filepath])
    #     elif os_name == "Linux":
    #         subprocess.run(['afplay',output_filepath])
    #     elif os_name=="Windows":
    #         subprocess.run(['powershell','-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
    #     else:
    #         raise OSError("Unsupported operating system")
    # except Exception as e:
    #     print(f"An error occured while trying to play the audio:{e}")



input_text='Hi,My Name is Muskan Jhala'
# text_to_speech_with_gtts(input_text=input_text,output_filepath="gtts_testing.mp3")
# text_to_speech_with_elevenlabs(input_text=input_text,output_filepath="Elevenlabs_testing.mp3")

