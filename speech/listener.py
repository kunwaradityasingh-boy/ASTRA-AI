import speech_recognition as sr
from speech_recognition.exceptions import WaitTimeoutError

def listen():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=8
            )
            command = recognizer.recognize_google(audio, language="en-IN")
            print(f"You: {command}")
            return command
        except WaitTimeoutError:
            print("Listening timed out.")
            return ""
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            print("Speech Recognition service is unavailable.")
            return ""
    