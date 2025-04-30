from scipy.spatial import distance
import pygame
import os

def calculate_EAR(eye):
    """Göz açıklık oranını (EAR) hesaplar"""
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear_aspect_ratio = (A + B) / (2.0 * C)
    return ear_aspect_ratio

def main():
    pygame.mixer.init()
    alarm_sound=pygame.mixer.Sound("alarm.wav")
    
    if not os.path.exists("Shape_predictor_68_face_landmarks.dat"):
        print("Hata: shape_predictor_68_face_landmarks.dat dosyası bulunamadı!")
        return