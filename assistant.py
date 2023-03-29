import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from dictionary import DictionaryAPI

class Voice:
    def __init__(self, lang="fr"):
        self.lang = lang

    def speak(self, text):
        tts = gTTS(text, lang=self.lang)
        tts.save("audio.mp3")
        playsound("audio.mp3")

class Assistant:
    def __init__(self):
        self.dictionary_api = DictionaryAPI()
        self.voice = Voice()

    def listen(self):  # sorcery skip: inline-immediately-returned-variable
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="ang-ANG")
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None

    def respond(self, text):
        if text:
            if "définition" in text:
                word = text.replace("définition de ", "")
                definition = self.dictionary_api.get_definition(word)
                if definition is None:
                    self.voice.speak(f"Désolé, je n'ai pas pu trouver la définition de {word}.")
                else:
                    self.voice.speak(f"La définition de {word} est : {definition}")
            else:
                self.voice.speak(f"Vous avez dit: {text}.")

