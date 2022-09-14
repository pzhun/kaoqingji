# -*- coding:utf-8 -*-
import cv2
import urllib2
import urllib
import time
import sys
import pyttsx
import MySQLdb
import numpy as np


# 拍照功能
#def take_photo():
   # cap = cv2.VideoCapture("rtmp://www.gvsun.net:19350/live/sz2")
#   cap = cv2.VideoCapture(0)
#   ret, photo = cap.read()
#   if ret:
#       print "take photo successfuly"
#       cv2.imwrite("tttt.jpg", photo)
#   else:
#       print "Error! Photo failed!"


#if __name__ == "__main__":
#   take_photo()


# 使用自带的开发包实现的功能
faceCascade = cv2.CascadeClassifier("/home/pi/text4/LearnningXML/haarcascade_frontalface_default.xml")
image = cv2.imread("t1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.15,
    minNeighbors=4,
    minSize=(1,5),
)
print "Found {0} faces!".format(len(faces))
numberofpeople=len(faces)
for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
cv2.imshow("imageWindow", image)


# 语音读取人头数
reload(sys)
sys.setdefaultencoding('utf8')
engine = pyttsx.init()
engine.say("there are %d people "%(numberofpeople))
engine.runAndWait()
# 朗读一次

a = numberofpeople
def fc1():
    return(a)             # return 字符串 "func2"
print(fc1())
