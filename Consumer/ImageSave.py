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
        while(True):
            print("start read from kafka")
            for msg in consumer:
                print("np image\n")
                img = np.frombuffer(msg.value,dtype=np.uint8)
                print("decode")
                img = cv2.imdecode(img,1)
                print("get time")
                file = "Images/"+getDateTime()+".jpg"
                cv2.imwrite(file,img)

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
