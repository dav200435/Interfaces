import speech_recognition as sr
import subprocess
import webbrowser
import sys
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def options(text):
    if "calculadora" in text:
        try:
            subprocess.run("calc" if sys.platform == "win32" else "open -a Calculator" if sys.platform == "darwin" else "gnome-calculator")
        except Exception as e:
            print("No se pudo abrir la calculadora:", e)

    elif "algo" in text:
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ&autoplay")
        
    elif "no lo hagas" in text:
        webbrowser.open("https://www.youtube.com/watch?v=_HCqOqGwDfE&list=PLvaLWyx1hhfwvDH7Fo9OB1ohpUjqHGbot&autoplay")
    
    elif "cerrar" in text:
        print("Cerrando el asistente por voz.")
        speak("hasta la proxima")
        sys.exit()

def run():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            speak("Hola, soy tu asistente por voz ¿que necesitas?: ")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language="es-ES")
                print(f"Has dicho: {text}")
                options(text)
                    
            except sr.UnknownValueError:
                speak("No te he entendido")
            except sr.RequestError:
                print("Error con el servicio de reconocimiento de voz")


run()