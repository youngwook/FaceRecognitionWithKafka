import sys
import time
from datetime import datetime
import cv2
from kafka import KafkaProducer

topic = "image"

def publish_camera():
    """
    Publish camera video stream to specified Kafka Server`s topic.
    Kafka Server is expected to be running on the external place. Not partitioned.
    """

    # get detector of Face

    faceDetector = cv2.CascadeClassifier('Cascades/face_default.xml')

    # Start up producer

    producer = KafkaProducer(bootstrap_servers='192.168.0.17:9092')

    
    print("start read")
    camera = cv2.VideoCapture(0)
    try:
        while(True):
            success, frame = camera.read()

            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
            faces = faceDetector.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(20,20)
            )
            
            if(len(faces)>0):
                print("\n face detected");
                ret, buffer = cv2.imencode('.jpg', frame)
                producer.send(topic, buffer.tobytes())
                print("\n Image Streaming"+datetime.now().strftime('%m-%d-%Y,%H:%M:%S')) 
                # Choppier stream, reduced load on processor
                time.sleep(0.2)
           

    except:
        print("\nExiting.")
        sys.exit(1)

    
    camera.release()


if __name__ == '__main__':
    """
    Producer will publish to Kafka Server a video file given as a system arg. 
    Otherwise it will default by streaming webcam feed.
    """
    print("publishing feed!")
    publish_camera()
