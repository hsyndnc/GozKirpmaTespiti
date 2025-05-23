# Göz Kapanması (Uyuklama) Tespiti

Bu proje, gerçek zamanlı kamera görüntüsünden göz açıklık oranı (EAR) hesaplayarak kişinin uyuklama durumunu tespit eder. Gözler belirli bir süre kapalı kalırsa sesli bir alarm devreye girer.

## 🔍 Özellikler

- Gerçek zamanlı yüz ve göz tespiti
- Eye Aspect Ratio (EAR) hesaplama
- Gözlerin uzun süre kapalı olması durumunda sesli uyarı (alarm)
- Anlık uyarı metinleri ve görselleştirme

## 🛠 Gereksinimler

- Python 3.x
- OpenCV
- Dlib
- SciPy
- Pygame
- `shape_predictor_68_face_landmarks.dat` dosyası
- `alarm.wav` (alarm sesi dosyası)

## 📁 Proje Yapısı
│
├── alarm.wav # Alarm sesi dosyası
├── shape_predictor_68_face_landmarks.dat # dlib'in yüz hatları model dosyası
├── proje.py # Ana Python scripti
└── README.md # Bu dosya

## 🔧 Kurulum
1.Depoyu klonlayın:

```bash
git clone https://github.com/hsyndnc/GozKirpmaTespiti.git
cd GozKirpmaTespiti
```

### 1. Gerekli Kütüphaneleri Yükleyin

Terminal veya komut satırında aşağıdaki komutu çalıştırın:

```bash
pip install opencv-python dlib scipy pygame
```