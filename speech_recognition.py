import speech_recognition as sr

def recognize():

    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="fr-FR")
    except sr.UnknownValueError:
        text = "Je n'ai pas compris ce que vous avez dit."
    except sr.RequestError:
        text = "Impossible de se connecter au service de reconnaissance vocale."

    return text
