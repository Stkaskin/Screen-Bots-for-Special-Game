import datetime
from pyautogui import *
import pytesseract as tess
import pyautogui
import cv2
import keyboard
import random
import win32api, win32con
import threading

c1 = 250, 20
c2 = 250, 130
m1 = 1
hp = 300
shield = 800
wait = False

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def keyP(key):
    keyboard.press(key)
    sleep(0.04)
    keyboard.release(key)
    sleep(0.04)


def map_search():
    if pyautogui.locateOnScreen('3-6.png', region=(0, 0, 1366, 768), grayscale=True, confidence=0.95):
        current_map = "3-6"
    else:
        current_map = "others"


def map_s():
    mapc1 = pyautogui.locateOnScreen('map.png', region=(0, 0, 1366, 768), grayscale=True, confidence=0.7)
    if mapc1:
        global mapc
        mapc = mapc1
        print(mapc[0])
        print(mapc[1])
        return mapc[0], mapc[1]


topla = False


def arabox():
    datess = datetime.datetime.now()
    cadar = pyautogui.locateCenterOnScreen('bonusbox.png', region=(80, 30, 1100, 700), grayscale=True, confidence=0.8)
    if cadar:

        return cadar[0], cadar[1]


def arabox2():
    datess = datetime.datetime.now()
    cadar = pyautogui.locateCenterOnScreen('bonusbox.png', region=(500, 250, 350, 300), grayscale=True, confidence=0.8)
    if cadar:
        print(datess - datetime.datetime.now())
        return cadar[0], cadar[1]


saldiri = False
# t1 = threading.Thread(target=calistir, args=("thread-1",))

# t2.start()
# c[0]+30 , c[1]+50  260*160
next_x = 240
next_y = 20
mapc = 0, 0

x1 = 1110, 1318, 1318, 1110
y1 = 730, 700, 620, 615
eksiar = False
times = 0
counter = -1
time = datetime.datetime.now().today()
cccc=0
yyyy=0

def arasifi(ss,timmm):
    global time
    global boxcount
    if boxcount > 8:
        sleep(300)


    if time:
        t = datetime.datetime.now().today() - time
        global cccc
        global yyyy
        if ss:
           if cccc:
            leftClick(cccc, yyyy)
            time = datetime.datetime.now().today()
           else:
               leftClick(1200, 650)
        elif (t.seconds.numerator > 3 and timmm ==False):
            cat = pyautogui.locateOnScreen('sifir.png', region=(1150, 575, 73, 20), grayscale=False, confidence=0.8)
            if cat:
                time = datetime.datetime.now().today()

                cccc = random.randint(1100, 1295)
                yyyy = random.randint(620, 750)
                while cccc>1295 and yyyy >725:
                    cccc = random.randint(1100, 1295)
                    yyyy = random.randint(620, 750)

                leftClick(cccc, yyyy)
                keyP('0')
                keyP('7')
        elif timmm:
            cccc = random.randint(1100, 1295)
            yyyy = random.randint(620, 750)
            while cccc > 1295 and yyyy > 725:
                cccc = random.randint(1100, 1295)
                yyyy = random.randint(620, 750)
            time = datetime.datetime.now().today()
            leftClick(cccc, yyyy)

    print(boxcount)
    if  boxcount>5:
            sleep(5)
            boxcount=0
            global timebox
            timebox = datetime.datetime.now()


boxcount=0
timebox=datetime.datetime.now()
while 1:
    # hp_search()
   # arasifi(False, False)
    cev = False
    cada = arabox()

    if cada:
        leftClick(cada[0], cada[1])
        sleep(1)
        cada = arabox2()
        if (datetime.datetime.now() - timebox).seconds < 5:
            boxcount += 1
       # timebox = datetime.datetime.now()
        cev = True
        if cada:
            leftClick(cada[0], cada[1])
            sleep(0.3)
            cev = True
         #   if (datetime.datetime.now()- timebox).seconds<5 :
          #    boxcount += 1
        timebox = datetime.datetime.now()
 #   if cev:
  #      arasifi(True, False)


  #  elif ((datetime.datetime.today() - time).seconds.numerator > 50):
   #     arasifi(False,True)
    #    keyP('0')
     #   keyP('7')
      #  sleep(2)

