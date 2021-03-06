import cv2
import numpy as np
import csv
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
