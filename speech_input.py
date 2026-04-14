import speech_recognition as sr

def get_voice_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            return command.lower()
        except:
            return "Sorry, I didn't understand."

def get_text_command():
    return input("Enter command: ").lower()
