import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import pygame
import time

def record_audio(file_path, duration=5, fs=44100):
    print("Please say something...")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
    sd.wait()
    wav.write(file_path, fs, audio_data)
    print("Recording complete.")

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)
