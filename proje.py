import pygame
import os
import cv2
import dlib
from scipy.spatial import distance

def calculate_EAR(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

def main():
    pygame.mixer.init()
    alarm_sound = pygame.mixer.Sound("alarm.wav")

    if not os.path.exists("shape_predictor_68_face_landmarks.dat"):
        print("Hata: shape_predictor_68_face_landmarks.dat dosyası bulunamadı!")
        return

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Hata: Kamera açılamadı!")
        return

    hog_face_detector = dlib.get_frontal_face_detector()
    dlib_facelandmark = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Hata: Kameradan görüntü alınamadı!")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = hog_face_detector(gray)

        for face in faces:
            landmarks = dlib_facelandmark(gray, face)
            leftEye = []
            rightEye = []

            for n in range(36, 42):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                leftEye.append((x, y))
                next_point = 36 if n == 41 else n + 1
                x2 = landmarks.part(next_point).x
                y2 = landmarks.part(next_point).y
                cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)

            for n in range(42, 48):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                rightEye.append((x, y))
                next_point = 42 if n == 47 else n + 1
                x2 = landmarks.part(next_point).x
                y2 = landmarks.part(next_point).y
                cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)
        
        # test kodu
        left_ear = calculate_EAR(leftEye)
        right_ear = calculate_EAR(rightEye)
        ear = (left_ear + right_ear) / 2.0
        print(f"EAR: {ear:.2f}")


        cv2.imshow("Görüntü", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
