import speech_recognition as sr
import pyttsx3
from googletrans import Translator

# Initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()
translator = Translator()

# Set voice properties
engine.setProperty('rate', 170)

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen function
def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("🧠 Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except:
        speak("Sorry, I didn't understand")
        return ""

# Translate function
def translate_text(text, lang="en"):
    try:
        translated = translator.translate(text, dest=lang)
        return translated.text
    except:
        return text

# Language selection
def choose_language():
    speak("Choose language English, Hindi, or Punjabi")

    lang = listen()

    if "hindi" in lang:
        return "hi"
    elif "punjabi" in lang:
        return "pa"
    else:
        return "en"

# Main assistant
def run_assistant():
    lang = choose_language()
    speak("Voice assistant started")

    while True:
        command = listen()

        if command == "":
            continue

        # Exit command
        if "stop" in command or "exit" in command:
            speak(translate_text("Goodbye", lang))
            break

        # Greetings
        elif "hello" in command or "hi" in command:
            speak(translate_text("Hello, how can I help you?", lang))

        # Time
        elif "time" in command:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M")
            speak(translate_text(f"The time is {now}", lang))

        # Basic response
        else:
            response = "You said " + command
            speak(translate_text(response, lang))


# Run
if __name__ == "__main__":
    run_assistant()