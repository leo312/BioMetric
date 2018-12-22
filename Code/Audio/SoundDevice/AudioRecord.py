import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from tempfile import TemporaryFile
import csv

num=0

id = int(input('Enter Your ID: '))


def extract_mfcc(myrecording):
        (rate,sig) = wav.read(StringIO.StringIO(myrecording))
        mfcc_feat = features.mfcc(sig,rate)
        data = numpy.asarray(mfcc_feat, dtype='float32')
        return data      



def record():
    
    fs=44100
    duration = 1  # seconds
    myrecording = sd.rec(duration * fs, samplerate=fs, channels=2,dtype='float64')
    print("Recording Audio")
    sd.wait()
    print("Audio recording complete , Play Audio")
    sd.play(myrecording, fs)
    sd.wait()
    print("Play Audio Complete")
    num = input('Press 1 to Continue: \nPress 2 to Record Again:')
    if (num=='1'):
        row=[id,myrecording]
        with open('recordData.csv','a') as File:
            write=csv.writer(File)
            write.writerow(row)
        File.close()
        extract_mfcc(myrecording)
        print('done')
        print(data)
    else:
        record()

    
record()



