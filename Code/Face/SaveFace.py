# Create raw database 
# This script creates 15 samples of a person stores it it a file
# Make sure no two person should have same IDs
# This script uses laptop camera to detect faces and extract it.

import cv2
import numpy as np
import csv
#To assign a particular name to person

id = int(input('Enter your ID: '))
name = input('Enter Name: ')


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
		cv2.imwrite("C:/Users/leo_0/Downloads/Python/Thakkar/dataSet/"+str(id)+"."+str(sample)+".jpg", gray[y:y+h, x:x+w])
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
	
		
	
	

