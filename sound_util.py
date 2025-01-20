import os
from playsound import playsound # type: ignore
from gtts import gTTS # type: ignore

def greet_user(name):
    try:
        greeting_message = f"Xin chào, {name}!"
        print(greeting_message)
        tts = gTTS(greeting_message, lang='vi')
        audio_file = "greeting.mp3"
        tts.save(audio_file)
        playsound(audio_file)
        os.remove(audio_file)  # Remove the temporary audio file after playing
    except Exception as e:
        print(f"Error in greeting user: {e}")


# greet_user("Tuấn")