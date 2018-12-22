import pyaudio
import wave
import os
import pylab

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 2


id = int(input('Enter Your ID: '))
name = input('Enter Your Name: ')

print("You have to give Sample 5 Times")
x = input('Press Any Key to record Audio: ')
print("Speak Your Name")

if not os.path.exists('AudioSample/'+name):
    os.mkdir('AudioSample/'+name)

    for i in range(5):
        

    
        WAVE_OUTPUT_FILENAME = 'C:/Users/leo_0/Downloads/Python/Audio/New folder (2)/AudioSample/'+name+'/'+str(i)+'.wav'
            
        def graph_spectrogram(WAVE_OUTPUT_FILENAME,i):
            
            sound_info, frame_rate = get_wav_info(WAVE_OUTPUT_FILENAME)
            pylab.figure(num=None, figsize=(19, 12))
            pylab.subplot(111)
            pylab.title('spectrogram of %r' % WAVE_OUTPUT_FILENAME)
            pylab.specgram(sound_info, Fs=frame_rate)
            
            pylab.savefig('C:/Users/leo_0/Downloads/Python/Audio/New folder (2)/Spectrogram/'+str(id)+'.'+str(i)+'.png')
            #pylab.savefig('spectrogram of'+str(i)+'.png')
            
        def get_wav_info(WAVE_OUTPUT_FILENAME):
            
            wav = wave.open(WAVE_OUTPUT_FILENAME, 'r')
            frames = wav.readframes(-1)
            sound_info = pylab.fromstring(frames, 'Int16')
            frame_rate = wav.getframerate()
            wav.close()
            return sound_info, frame_rate
            
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for j in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()
           
        print("Directory " , name ,  " Created ")
        
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        
        graph_spectrogram(WAVE_OUTPUT_FILENAME,i)
        
        
     
        
        wf.close()


else:    
    print("Directory " , name ,  " already exists")
