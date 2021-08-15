import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob
import librosa as lr
import sys
import os


def main():
  print(sys.version)
  audio_file_path = "C:/Users/andrei/Desktop/Hacker/Say It [Misc]/text.mp3"
  audio_sample = lr.util.example_audio_file()
  #print(os.path.exists(audio_file_path))
  audio, sfreq = lr.load(audio_file_path)
  #frequencies, D = lr.ifgram(y=audio, sr=sfreq)
  print(sfreq)
  time = np.arange(0, len(audio)) / sfreq
  #print(time)
  fig, ax = plt.subplots()
  ax.plot(time, audio)
  ax.set(xlabel='Time (s)', ylabel='Sound Amplitude')
  plt.show()


main()