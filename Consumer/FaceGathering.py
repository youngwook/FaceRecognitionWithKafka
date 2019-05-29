from datetime import datetime
import numpy as np
import sys
import cv2
from kafka import KafkaConsumer

topic = "image"

def readImage():

    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=['192.168.0.17:9092']
    )

    try:
        face_id = 1
        count = 0
        while(True):
            print("start read from kafka")
            for msg in consumer:

                print("save image")
                img = np.frombuffer(msg.value,dtype=np.uint8) #convert bytes to np array.
                img = cv2.imdecode(img,0)                     #decode np array to cv2 image pattern. 
                file = "dataset/User."+str(face_id)+"."+str(count)+".jpg" 
                cv2.imwrite(file,img)
                count= count+1

    except:
        print(sys.exc_info())
        print("\nExiting.")
        sys.exit(1)
def getDateTime():
    print("set time")
    now = datetime.now()
    return now.strftime("%m-%d-%Y.%H-%H-%M-%S")

if __name__ == '__main__':

    print("start read iamges")
    readImage()
