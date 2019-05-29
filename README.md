# Face Recognition With Kafka and Raspberry
1. environment requirements
  1. for consumer
  2. for publisher
2. train recognizer
  1. image data preparation
  2. train model
3. test recognizer

## environment requirements
#### for consumer
Develop Environment:
- OS: Ubuntu 14. 04 desktop 64
- Memory: 4GB=4096MB
- Hard disk: 100GB
- Network: bridge
- Software: 
  - zookeeper 
  - kafka: [link](https://medium.com/@kevin.michael.horan/distributed-video-streaming-with-python-and-kafka-551de69fe1dd)
  - pip: python package installer
  - wget: tool to download sources from url
- Libraries:
  - kafka-python: python library to connect with kafka server
  - opencv-contrib-python: opency library to manipulate images
  - python3-dev: python language version 3
  
#### for publisher
Raspberry pi 3 model B:
- OS: rasbian stretch
- CPU: Quad Core 1.2GHz Broadcom BCM2837 64bit CPU
- RAM: 1GB RAM
- Software: 
  - pip: python package installer
  - wget: tool to download sources from url
- Libraries:
  - kafka-python: python library to connect with kafka server
  - python3-dev: python language version 3
  - opencv-contrib-python: opency library to manipulate images [link](https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/)

## train recognizer
### for gethering face images
note: in the python code you have to change the ip address to the machine where the kafka server is runing.
#### in consumer

1. start kafka server
change directory to kafka server directory then run it
```
$bin bin/kafka-server-start.sh config/server.properties
```
2. execute save image python code to save image from kafka
```
$python3 FaceGathering.py
```
#### in publisher
1. change to virtual environment(note: if you did not using virtual environment just ignore)
in home directory of user
```
$source .profile
$workon cv
```
2. execute image capture and publisher to publish image get from camera to kafka
```
$ python PublishImageToKafka.py
```

### for train model
#### in consumer
1. execute model training python code to train model with gathered images
```
$python3 TrainFaceDetector.py
```

## test recognizer
note: in the python code you have to change the ip address to the machine where the kafka server is runing.
#### in consumer

1. start kafka server
change directory to kafka server directory then run it
```
$bin bin/kafka-server-start.sh config/server.properties
```
2. execute Face Detector to recognize streaming image from raspberry pi
```
$python3 CaptureTrainImage.py
```
#### in publisher
1. change to virtual environment(note: if you did not using virtual environment just ignore)
in home directory of user
```
$source .profile
$workon cv
```
2. execute image publisher to publish image get from camera to kafka
```
$ python PublishImageToKafka.py
```

######for github syntax [fefer to](https://guides.github.com/features/mastering-markdown/)
