import cv2
import numpy as np
import csv
from django.http.response import HttpResponse
from django.shortcuts import render
import win32api
import string, random
import urllib  # Python URL functions
import urllib.request  # Python URL functions
# Create your views here.
import pyaudio
import wave
import os
from PIL import Image


def fir(request):
    return render(request, 'fir.html')

def add(request):
    return render(request, 'add.html')

def newinfo(request):

    name =request.GET.get('name')
    id =int(request.GET.get('num'))


    sample = 0
    row = [id, name]

    with open('names.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()

    # to generate classifier which classifies the frontalFace

    faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    #eyeDetect = cv2.CascadeClassifier('haarcascade_eye.xml')
    # TO capture image from webcam we need video capture object

    cam = cv2.VideoCapture(0) # Most of the time 0 is working but if it doesnt then use different iDs

    # Capture images one by one and detect the faces and show it in window


    while(True):
        '''
             Capturing the ima0e.. cam read will return one status variable and one captured image
        '''
        ret,img = cam.read();

        #and this image is colored and for classifier to work we need grayscaled image
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);

        # Now we have gray scaled image and we can detect face from that
        faces = faceDetect.detectMultiScale(gray,1.3,5);

        # faces have all the images and what we need to do is we need to put a square on each of the face
        for(x,y,w,h) in faces:
            sample = sample+1;
            # here we need to save the faces
            cv2.imwrite("C:/Users/leo_0/PycharmProjects/Project/dataSet/"+str(id)+"."+str(sample)+".jpg", gray[y:y+h, x:x+w])
            cv2.waitKey(100)

            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2);
        cv2.imshow('image',img)

        cv2.waitKey(1)

        # Take samples and quit the loop if it increaes 15

        if(sample>55):
            break;
    #This will release the camera

    cam.release()

    #	THIS CODE FOR WHILE LOOP

    cv2.destroyAllWindows()



    info='Your Face Sample has been Added Succesfully !!!'
    return render(request, 'fir.html',{'info':info})


def viewlive(request):


    faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
    rec=cv2.cv2.face.LBPHFaceRecognizer_create()
    rec.read("trainingData.yml")
    cam=cv2.VideoCapture(0)

    fontface=cv2.FONT_HERSHEY_SIMPLEX
    name = "un"
    id = 0
    namedict = {}
    with open('names.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            namedict[int(row['Id'])] = row['Name']
    c=0
    d=0
    while(True):

        ret,img= cam.read();
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces=faceDetect.detectMultiScale(gray,1.3,5);
        print('done')
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            id,conf =rec.predict(gray[y:y+h,x:x+w])
            print(conf)
            print(id)

            if(conf<40):
                if(id>0):
                    c=c+1
                    name = namedict[id]
                else:
                    d=d+1
                    name = "unknown"
                    id = 0
            else:
                d=d+1
                name = "unknown"
                id = 0
            print(id)
            cv2.putText(img,name,(x,y+h),fontface,1,(0,0,255),2);
        cv2.imshow("Face",img);
        if(cv2.waitKey(1)==ord('q')):
            break
        '''elif c==45:
            print("Valid Entry")
            break
        elif d==45:
            print('Envalid Entry')
            break'''
    cam.release()
    cv2.destroyAllWindows()
    return render(request, 'fir.html')

def train(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

    def getImagesAndLabels(path):
        #get the path of all the files in the folder
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
        #create empth face list
        faceSamples=[]
        #create empty ID list
        Ids=[]
        #now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:

            # Updates in Code
            # ignore if the file does not have jpg extension :
            if(os.path.split(imagePath)[-1].split(".")[-1]!='jpg'):
                continue

            #loading the image and converting it to gray scale
            pilImage=Image.open(imagePath).convert('L')
            #Now we are converting the PIL image into numpy array
            imageNp=np.array(pilImage,'uint8')
            #getting the Id from the image
            Id=int(os.path.split(imagePath)[-1].split(".")[0])
            # extract the face from the training image sample
            faces=detector.detectMultiScale(imageNp)
            #If a face is there then append that in the list as well as Id of it
            for (x,y,w,h) in faces:
                faceSamples.append(imageNp[y:y+h,x:x+w])
                Ids.append(Id)
        return faceSamples,Ids


    faces,Ids = getImagesAndLabels('dataSet')
    recognizer.train(faces, np.array(Ids))
    recognizer.save('trainingData.yml')
    train='Your Model Has been Trained !!!'
    return render(request, 'fir.html', {'train':train})

