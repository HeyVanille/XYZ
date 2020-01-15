import pyaudio
import numpy as np

maxValue = 2**16
bars = 35
p=pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=6, rate = 44100,
              input=True, frames_per_buffer=2048, input_device_index=3)
while True:
    data = np.fromstring(stream.read(2048),dtype=np.int16)
    dataL = data[0::3]
    dataR = data[1::3]
    dataC = data[2::3]
    peakL = np.abs(np.max(dataL)-np.min(dataL))/maxValue
    peakR = np.abs(np.max(dataR)-np.min(dataR))/maxValue
    peakC = np.abs(np.max(dataC)-np.min(dataC))/maxValue
    lString = "#"*int(peakL*bars)+"-"*int(bars-peakL*bars)
    rString = "#"*int(peakR*bars)+"-"*int(bars-peakR*bars)
    cString = "#"*int(peakC*bars)+"-"*int(bars-peakC*bars)
    print("L=[%s]\tR=[%s]\tC=[%s]"%(lString, rString, cString))