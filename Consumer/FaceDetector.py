import cv2
import numpy as np
from kafka import KafkaConsumer
import os 
import time
import sys

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/FaceDetector.yml')
cascadePath = "faceDetector.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX
#iniciate id counter
id = 0
# names related to ids: example ==> Rongxu: id=1,  etc
names = ['None', 'Rongxu'] 
topic = 'image'
try:
	consumer = KafkaConsumer(
		topic,
		bootstrap_servers=['192.168.0.17:9092']
	)
	while(True):
		print("read image from kafka")
		
		for msg in consumer:
			img = np.frombuffer(msg.value,dtype=np.uint8)
			img = cv2.imdecode(img,1)
			gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

			faces = faceCascade.detectMultiScale( 
				gray,
				scaleFactor = 1.2,
				minNeighbors = 5,
				minSize = (20,20)
			)
			
			for(x,y,w,h) in faces:
				cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
				id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
				# Check if confidence is less them 100 ==> "0" is perfect match 
				if (confidence < 100):
					id = names[id]
					confidence = "  {0}%".format(round(100 - confidence))
				else:
					id = "unknown"
					confidence = "  {0}%".format(round(100 - confidence))
				print("detected face is : "+id+"\n the probability is: "+confidence)
				
				cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
				cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
				
			cv2.imshow('camera',img) 
			k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
			if k == 27:
				break
		#time.sleep(1)	
			
except:
	# Do a bit of cleanup
	print(sys.exc_info())
	print("\n [INFO] Exiting Program and cleanup stuff")
	sys.exit(1)

