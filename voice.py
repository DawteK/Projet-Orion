import pyttsx3

class Voice:
    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if voice.name == "french":
                self.engine.setProperty('voice', voice.id)
                break
        self.engine.setProperty('rate', 150)

    def speak(self, text):
        self.engine.say(text)
       
