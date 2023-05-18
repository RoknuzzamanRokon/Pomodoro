import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Find the Alex voice
alex_voice = None
for voice in voices:
    print(voice.id)
    # if voice.name == 'Alex':
    #     alex_voice = voice
    #     break

if alex_voice:
    engine.setProperty('voice', alex_voice.id)
    engine.say("Hello, this is Alex speaking.")
    engine.runAndWait()
else:
    print("Alex voice not found.")

