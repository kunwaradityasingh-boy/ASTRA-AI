import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate", 175)
engine.setProperty("volume", 1.0)
voices = engine.getProperty("voices")
if len(voices) > 1:
    engine.setProperty("voice", voices[1].id)
else:
    engine.setProperty("voice", voices[0].id)
def speak(text):
    if not text:
        return
    
    engine.stop()
    engine.say(str(text))
    engine.runAndWait()