import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)

desenho_mp = mp.solutions.drawing_utils
maos_mp = mp.solutions.hands

maos = maos_mp.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

while True:
    success, image = webcam.read()

    resultado = maos.process(image)

    cv2.imshow("Webcam", image)

    key = cv2.waitKey(1)

    if key == 32:
        break

cv2.destroyAllWindows()