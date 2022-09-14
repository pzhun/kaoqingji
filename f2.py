# -*- coding:utf-8 -*-
import cv2
import urllib2
import urllib
import time
import sys
import pyttsx
import MySQLdb
import numpy as np

#def take_photo():
#    cap = cv2.VideoCapture(0)
#    ret, photo = cap.read()
#    if ret:
#        print "take photo successfuly"
#        cv2.imwrite("./text.jpg", photo)
#    else:
#        print "Error! Photo failed!"


#if __name__ == "__main__":
#    take_photo()

# 使用自带的开发包实现的功能
faceCascade = cv2.CascadeClassifier("/home/pi/text4/LearnningXML/haarcascade_frontalface_default.xml")
image = cv2.imread("t2.jpg")
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

b=numberofpeople

def fc2():
    return(b)             # return 字符串 "func2"
print(fc2())
#cxn = MySQLdb.Connect(host = '192.168.1.109', user = 'root', passwd = 'test')
#cur = cxn.cursor()
#cur.execute("USE zldb")
#cur.execute("INSERT INTO count VALUES(%d,%d,%d)"%(a,0,0))

#cur.close()
#cxn.commit()
#cxn.close()


#	return(a)
#f=open('out.txt','w')
#print >>f,"there are %d persons"%(faceNum)
#f.close()


#reload(sys)
#sys.setdefaultencoding('utf8')

#for line in open("out.txt"):
#    print line

#engine = pyttsx.init()
#engine.say("there are %d people"%(faceNum))
#engine.runAndWait()
# 朗读一次engine.endLoop()





#for i in range(faceNum):
#    face_rectangle = faces[i]['face_rectangle']
#    width =  face_rectangle['width']
#    top =  face_rectangle['top']
#    left =  face_rectangle['left']
#    height =  face_rectangle['height']
#    start = (left, top)
#    end = (left+width, top+height)
#    color = (55,255,155)
#    thickness = 3
#    cv2.rectangle(img, start, end, color, thickness)

#cv2.namedWindow("识别后")
#cv2.imshow("识别后", img)


#cv2.waitKey(0)
#cv2.destroyAllWindows()

# print type(resp)
