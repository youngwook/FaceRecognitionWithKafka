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



