import cv2
import mediapipe as mp
import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Piedra, Papel o Tijera")

try:
    easteregg_image = pygame.image.load("easteregg_image.jpg")
except FileNotFoundError:
    print("Error: No se encontró el archivo 'easteregg_image.jpg'.")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: No se pudo acceder a la cámara.")
    sys.exit()

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2,
                       min_detection_confidence=0.7, min_tracking_confidence=0.7)

easteregg_sequence = ["manos_juntas", "circulo", "paz", "saludo_militar"]
current_step = 0
easteregg_activated = False

def is_aligned(points, tolerance=0.15):
    y_values = [point.y for point in points]
    return max(y_values) - min(y_values) < tolerance

def detectar_gesto(hand_landmarks, num_hands):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    if num_hands == 2:
        return "manos_juntas"

    if abs(thumb_tip.x - index_finger_tip.x) < 0.05 and abs(thumb_tip.y - index_finger_tip.y) < 0.05:
        return "circulo"
    
    if index_finger_tip.y < thumb_tip.y and middle_finger_tip.y < thumb_tip.y and pinky_tip.y > middle_finger_tip.y:
        return "paz"
    
    if is_aligned([
        hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP],
        hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP],
        hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP],
        hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP],
        hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP]
    ]):
        return 'saludo_militar'

    if thumb_tip.y < index_finger_tip.y and thumb_tip.y < middle_finger_tip.y and pinky_tip.y < middle_finger_tip.y:
        return "Piedra"
    if thumb_tip.y > index_finger_tip.y and pinky_tip.y > index_finger_tip.y:
        return "Tijeras"
    if index_finger_tip.y < thumb_tip.y and middle_finger_tip.y < thumb_tip.y and pinky_tip.y > middle_finger_tip.y:
        return "Papel"
    
    return "Desconocido"

def verificar_easteregg(gesto_detectado):
    global current_step, easteregg_activated
    if easteregg_sequence[current_step] == gesto_detectado:
        current_step += 1
        if current_step == len(easteregg_sequence):
            easteregg_activated = True
            current_step = 0

def determinar_ganador(gesto_jugador, gesto_computadora):
    if gesto_jugador == gesto_computadora:
        return "Empate"
    elif (gesto_jugador == "Piedra" and gesto_computadora == "Tijeras") or \
         (gesto_jugador == "Papel" and gesto_computadora == "Piedra") or \
         (gesto_jugador == "Tijeras" and gesto_computadora == "Papel"):
        return "Ganaste"
    else:
        return "Perdiste"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cap.release()
            pygame.quit()
            sys.exit()

    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)
    num_hands = len(results.multi_hand_landmarks) if results.multi_hand_landmarks else 0
    gesto_detectado = "Desconocido"

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            gesto_detectado = detectar_gesto(hand_landmarks, num_hands)
            verificar_easteregg(gesto_detectado)

    if easteregg_activated:
        screen.blit(easteregg_image, (0, 0))
    else:
        gesto_jugador = detectar_gesto(hand_landmarks, num_hands) if results.multi_hand_landmarks else "Desconocido"
        opciones = ["Piedra", "Papel", "Tijeras"]
        gesto_computadora = random.choice(opciones)
        resultado = determinar_ganador(gesto_jugador, gesto_computadora)

        screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 36)
        text_jugador = font.render(f"Jugador: {gesto_jugador}", True, (0, 0, 0))
        text_computadora = font.render(f"Computadora: {gesto_computadora}", True, (0, 0, 0))
        text_resultado = font.render(f"Resultado: {resultado}", True, (0, 0, 255))

        screen.blit(text_jugador, (50, 50))
        screen.blit(text_computadora, (50, 100))
        screen.blit(text_resultado, (50, 150))

    pygame.display.flip()
    cv2.imshow("Camera Feed", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
pygame.quit()
