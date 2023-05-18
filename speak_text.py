import pyttsx3


def take_5_minutes_rest():
    engine = pyttsx3.init()

    engine.say("Naw you will take five minutes rest.")

    engine.runAndWait()

