# -*- coding:utf-8 -*-
import cv2
import urllib2
import urllib
import time


img = cv2.imread("footballteam.jpeg")
cv2.namedWindow("原图")
cv2.imshow("原图", img)

#URL
http_url='https://api-cn.faceplusplus.com/facepp/v3/detect' 
#用户信息
key = "TtAky0_27VAJA_GLP6IHl76-5lcQBq00"    
secret = "ZuNexcTiKiVnfBI3c0sDoHJ1_oUjZz7c"
#图片存储路径
filepath = r"/home/npukujui/work/facerecognition/footballteam.jpeg"


boundary = '----------%s' % hex(int(time.time() * 1000))
data = []
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
data.append(key)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
data.append(secret)
data.append('--%s' % boundary)
fr=open(filepath,'rb')
data.append('Content-Disposition: form-data; name="%s"; filename=" "' % 'image_file')
data.append('Content-Type: %s\r\n' % 'application/octet-stream')
data.append(fr.read())
fr.close()
data.append('--%s--\r\n' % boundary)

http_body='\r\n'.join(data)
#buld http request
req=urllib2.Request(http_url)
#header
req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
req.add_data(http_body)
try:
    #req.add_header('Referer','http://remotserver.com/')
    #post data to server
    resp = urllib2.urlopen(req, timeout=5)
    #get response
    qrcont=resp.read()
    print qrcont       

except urllib2.HTTPError as e:
    print e.read()


mydict = eval(qrcont)
faces = mydict["faces"]
faceNum = len(faces)
print("识别到了%d个人脸"%(faceNum))

for i in range(faceNum):
    face_rectangle = faces[i]['face_rectangle']
    width =  face_rectangle['width']
    top =  face_rectangle['top']
    left =  face_rectangle['left']
    height =  face_rectangle['height']
    start = (left, top)
    end = (left+width, top+height)
    color = (55,255,155)
    thickness = 3
    cv2.rectangle(img, start, end, color, thickness)

cv2.namedWindow("识别后")
cv2.imshow("识别后", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# print type(resp)
