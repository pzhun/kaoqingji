# -*- coding:utf-8 -*-

import MySQLdb
import pygame
import time
import schedule
from PIL import Image

import Adafruit_ILI9341 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI

DC = 3
RST = 25
SPI_PORT = 0
SPI_DEVICE = 0
# Create TFT LCD display class.
disp = TFT.ILI9341(DC, rst=RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=64000000))
disp.begin()
image = Image.open('cat.jpg')
image = image.rotate(90).resize((240, 320))
disp.display(image)

time.sleep(1)

disp.begin()
image = Image.open('a.jpg')
image = image.rotate(90).resize((240, 320))
disp.display(image)

file1=r"/home/pi/Music/a.mp3"
pygame.mixer.init()
track = pygame.mixer.music.load(file1)
pygame.mixer.music.play()
time.sleep(3)
pygame.mixer.music.stop()

id=int(input("请输入班级ID"))
from f1 import fc1
a=fc1()

disp.begin()
image = Image.open('t1.jpg')
image = image.rotate(90).resize((240, 320))
disp.display(image)

time.sleep(2)

disp.begin()
image = Image.open('b.jpg')
image = image.rotate(90).resize((240, 320))
disp.display(image)

file2=r"/home/pi/Music/b.mp3"
pygame.mixer.init()
track = pygame.mixer.music.load(file2)
pygame.mixer.music.play()
time.sleep(3)
pygame.mixer.music.stop()


p=int(input("语言点名请按1，结束点名请按2"))
if p==1:
    file=r"/home/pi/Music/c.mp3"
    pygame.mixer.init()
    track = pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    time.sleep(10)
    pygame.mixer.music.stop()
else:
    print("点名结束")

time.sleep(1)

disp.begin()
image = Image.open('cat.jpg')
image = image.rotate(90).resize((240, 320))
disp.display(image)


time.sleep(10)


from f2 import fc2
b=fc2()

disp.begin()
image = Image.open('t2.jpg')
image = image.rotate(90).resize((240, 320))
disp.display(image)

time.sleep(1)

disp.begin()
image = Image.open('cat.jpg')
image = image.rotate(90).resize((240, 320))
disp.display(image)

time.sleep(10)

from f3 import fc3
c=fc3()

disp.begin()
image = Image.open('t3.jpg')
image = image.rotate(90).resize((240, 320))
disp.display(image)

time.sleep(1)

disp.begin()
image = Image.open('cat.jpg')
image = image.rotate(90).resize((240, 320))
disp.display(image)


cxn = MySQLdb.Connect(host = 'localhost', user = 'qingniao', passwd = 'qingniao')
cur = cxn.cursor()
cur.execute("USE zldb")

# SQL 查询语句
sql = "SELECT * FROM kc \
       WHERE id  = '%d'" % (id)
cur.execute(sql)
results = cur.fetchall()
for row in results:
	t = row[1]

#a1=t-a
#a2=(t-a)/t
#b1=b-a
#b2=(b-a)/t
#c1=b-c
#c2=(b-c)/t

cur.execute("INSERT INTO count VALUES(%d,%d,%d,%d,%d,%d,%d,%d,%d,%d)"%(id,a,t-a,(t-a)*100/t,b,b-a,(b-a)*100/t,c,b-c,(b-c)*100/t))

cur.close()
cxn.commit()
cur.close()

