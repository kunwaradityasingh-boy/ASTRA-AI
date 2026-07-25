import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(
            source,
            timeout=5,
            phrase_time_limit=5
        )
        
    try:
        command = recognizer.recognize_google(audio, language="hi-IN")
        print(f"You: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        print("Speech Recognition service is unavailable.")
        return ""
    