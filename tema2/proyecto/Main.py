import cv2
import speech_recognition as sr
import pyttsx3
from transformers import pipeline
import os

class SistemaDeteccion:
    def __init__(self):
        # Inicializar síntesis de voz
        self.engine = pyttsx3.init()
        self.reconocedor = sr.Recognizer()
        self.modelo_ia = self.cargar_modelo_ia()
        self.camara = cv2.VideoCapture(0)
        self.nombre_imagen = "captura.jpg"
        self.hablar("Sistema iniciado. Di '¿Qué ves?' para analizar la imagen o 'salir' para salir.")

    def cargar_modelo_ia(self):
        """Carga el modelo de IA para detección de objetos."""
        print("Cargando el modelo de detección de objetos...")
        return pipeline("object-detection", model="facebook/detr-resnet-50")

    def hablar(self, mensaje):
        """Convierte texto en voz."""
        self.engine.say(mensaje)
        self.engine.runAndWait()

    def escuchar_comando(self):
        """Escucha un comando de voz y lo devuelve como texto."""
        with sr.Microphone() as source:
            print("Escuchando...")
            try:
                audio = self.reconocedor.listen(source)
                comando = self.reconocedor.recognize_google(audio, language="es-ES")
                return comando.lower()
            except sr.UnknownValueError:
                self.hablar("No he podido oirte bien.")
                return None
            except sr.RequestError:
                self.hablar("Error en el servicio de reconocimiento de voz.")
                return None

    def analizar_imagen(self):
        """Captura una imagen, la analiza y describe los objetos detectados."""
        ret, frame = self.camara.read()
        if not ret:
            self.hablar("No se pudo acceder a la cámara.")
            return

        # Guardar la imagen capturada
        cv2.imwrite(self.nombre_imagen, frame)

        # Usar el modelo de IA para detectar objetos
        try:
            detecciones = self.modelo_ia(self.nombre_imagen)
            objetos_detectados = [
                (obj["label"], int(obj["score"] * 100)) for obj in detecciones if obj["score"] > 0.4
            ]
        except Exception as e:
            self.hablar("Error al analizar la imagen.")
            print("Error:", e)
            return

        # Hablar sobre los objetos detectados
        if objetos_detectados:
            for objeto, probabilidad in objetos_detectados:
                self.hablar(f"Veo un {objeto} con una probabilidad del {probabilidad} por ciento.")
        else:
            self.hablar("No detecto objetos relevantes en la imagen.")

    def eliminar_imagen(self):
        """Elimina la imagen capturada si existe."""
        if os.path.exists(self.nombre_imagen):
            os.remove(self.nombre_imagen)
            print(f"Imagen '{self.nombre_imagen}' eliminada.")

    def ejecutar(self):
        """Ejecuta el sistema en un bucle principal."""
        while True:
            comando = self.escuchar_comando()
            if not comando:
                continue

            if "que ves" in comando or "qué ves" in comando or "que vez" in comando:
                self.analizar_imagen()
            elif "salir" in comando:
                self.hablar("Saliendo del programa. Adiós.")
                break
            else:
                self.hablar("No te entiendo.")

        # Limpiar recursos
        self.limpiar()

    def limpiar(self):
        """Libera los recursos utilizados."""
        self.camara.release()
        cv2.destroyAllWindows()
        self.eliminar_imagen()


if __name__ == "__main__":
    sistema = SistemaDeteccion()
    sistema.ejecutar()
