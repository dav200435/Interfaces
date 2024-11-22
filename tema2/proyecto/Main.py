import cv2
import speech_recognition as sr
import pyttsx3
import numpy as np

# Inicializar síntesis de voz
engine = pyttsx3.init()

def hablar(mensaje):
    engine.say(mensaje)
    engine.runAndWait()

# Inicializar reconocimiento de voz
reconocedor = sr.Recognizer()

def escuchar_comando():
    with sr.Microphone() as source:
        print("Escuchando...")
        try:
            audio = reconocedor.listen(source)
            comando = reconocedor.recognize_google(audio, language="es-ES")
            return comando.lower()
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            hablar("Error en el servicio de reconocimiento de voz.")
            return None

# Cargar modelo pre-entrenado de OpenCV (MobileNet SSD con Caffe)
prototxt_path = "models/MobileNetSSD_deploy.prototxt"
model_path = "models/MobileNetSSD_deploy.caffemodel"
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

# Clases específicas para un aula
clases_interes = {
    "person": "persona",
    "chair": "silla",
    "diningtable": "mesa",
    "pottedplant": "planta",
    "bottle": "botella",
    "tvmonitor": "pantalla",
}

# Captura de video
camara = cv2.VideoCapture(0)

hablar("Sistema iniciado. Di que ves, para analizar la imagen o salir, para salir.")

while True:
    comando = escuchar_comando()
    if comando is None:
        continue

    if "que ves" in comando:
        ret, frame = camara.read()
        if not ret:
            hablar("No se pudo acceder a la cámara.")
            continue

        # Preprocesar la imagen
        altura, ancho = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
        net.setInput(blob)
        detecciones = net.forward()

        # Iterar sobre las detecciones
        objetos_detectados = []
        for i in range(detecciones.shape[2]):
            confianza = detecciones[0, 0, i, 2]
            if confianza > 0.4:  # Umbral de confianza
                idx = int(detecciones[0, 0, i, 1])
                etiqueta = clases_interes.get(clases[idx], None)
                if etiqueta:
                    objetos_detectados.append((etiqueta, int(confianza * 100)))

        # Hablar sobre los objetos detectados
        if objetos_detectados:
            for objeto, probabilidad in objetos_detectados:
                hablar(f"Veo un {objeto} con una probabilidad del {probabilidad} por ciento.")
        else:
            hablar("No detecté objetos relevantes en la imagen.")
    elif "salir" in comando:
        hablar("Saliendo del programa. Adiós.")
        break
    else:
        hablar("No te entiendo.")

# Liberar recursos
camara.release()
cv2.destroyAllWindows()
