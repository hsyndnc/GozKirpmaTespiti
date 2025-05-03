import pygame
import os
import cv2
import dlib
from scipy.spatial import distance
import time

def calculate_EAR(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear_aspect_ratio = (A+B)/(2.0*C)
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

    alarm_playing = False
    eyes_closed_start_time = 0
    eyes_closed_duration = 0

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
                next_point = n+1 
                if n == 47:
                    next_point = 42
                x2 = landmarks.part(next_point).x
                y2 = landmarks.part(next_point).y
                cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)
        
        # test kodu
        left_ear = calculate_EAR(leftEye)
        right_ear = calculate_EAR(rightEye)
        EAR = (left_ear + right_ear) / 2.0
        print(f"EAR: {EAR:.2f}")

        # gözün kapalı kalma süresi ile alarm ilişkisi
        if EAR < 0.26:
                if not alarm_playing:
                    eyes_closed_start_time = time.time()
                    alarm_sound.play(-1)
                    alarm_playing = True
                eyes_closed_duration = time.time() - eyes_closed_start_time
                cv2.putText(frame, "GOZLER KAPALI", (20,100),
                              cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,255), 4)
                cv2.putText(frame, f"Kapali Sure: {eyes_closed_duration:.1f} saniye", (20,400),
                              cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
                print(f"Drowsy - Kapalı Süre: {eyes_closed_duration:.1f} saniye")
        else:
                if alarm_playing:
                    alarm_sound.stop()
                    alarm_playing = False
                    eyes_closed_duration = 0

            print(f"EAR: {EAR:.2f}")


        cv2.imshow("Görüntü", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


            