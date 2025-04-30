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