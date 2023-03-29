import requests

import speech_recognition as sr
from dictionary import DictionaryAPI
from text_to_speech import speak

class DictionaryAPI:
    def __init__(self):
        self.url = "https://api.dicolink.com/v1/mot"
        self.headers = {"Authorization": "Bearer API_KEY"}

    def get_definition(self, word):
        params = {"mot": word}
        response = requests.get(self.url, headers=self.headers, params=params)
        if response.status_code == 200:
            result = response.json()
            if "definitions" in result and result["definitions"]:
                return result["definitions"][0]["definition"]
        return None


class Assistant:
    def __init__(self):
        self.name = "Orion"
        self.dictionary_api = DictionaryAPI()

    def greet(self):
        speak(f"Bonjour, je suis {self.name}. Comment puis-je vous aider ?")

    def listen(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
        text = ""
        try:
            text = recognizer.recognize_google(audio, language='fr-FR')
        except sr.UnknownValueError:
            pass # Si la reconnaissance échoue, on ignore simplement le texte
        except sr.RequestError:
            speak("Je n'ai pas pu me connecter au service de reconnaissance vocale.")
        return text

    def respond(self, text):
        if "définition" in text:
            word = text.replace("définition de ", "")
            definition = self.dictionary_api.get_definition(word)
            if definition is None:
                speak(f"Désolé, je n'ai pas pu trouver la définition de {word}.")
            else:
                speak(f"La définition de {word} est : {definition}")
        else:
            speak(f"Vous avez dit: {text}.")

    def run(self):
        self.greet()
        while True:
            text = self.listen()
            if text:
                if "Orion" in text:
                    self.respond(text)

