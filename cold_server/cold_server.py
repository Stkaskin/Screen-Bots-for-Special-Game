from pyautogui import *
import pytesseract as tess
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import threading

c1 = 190, 160
c2 = 190, 75
m1 = 1
hp = 300
shield = 800
patlama = False
confi = 0
times = 0
shipx = 320
shipy = 225
shipposx = 0
shipposy = 0
portalx = 260
portaly = 190
wait = False
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def calistir(threadName):
    global shipposx
    global shipposy
    while True:
        global patlama
        patlama = repair()
        sh = shipPos()
        if sh:
            shipposx = sh[0]
            shipposy = sh[1]
        if shipposx != 0:
            hp_search()
            global confi
            confi = confi_search()
            shield_search()
        map_search()

        # print("controller tamam")

    # if shipposx:
    #  print(shipposx)
    # print(shipposy)


def repair():
    tarif = False
    tut = pyautogui.locateOnScreen('connection.png', region=(0, 0, 1366, 768), grayscale=True, confidence=0.8)

    if tut:
        leftClick(tut[0], tut[1])
        sleep(1)
        tarif = False
        sleep(1)
    tut = pyautogui.locateOnScreen('repair.png', region=(0, 0, 1366, 768), grayscale=True, confidence=0.8)
    if tut:
        leftClick(tut[0], tut[1])
        print("patladı")
        sleep(1)
        tarif = True

    tut = pyautogui.locateOnScreen('repair_click.png', region=(0, 0, 1366, 768), grayscale=True, confidence=0.8)
    if tut:
        leftClick(tut[0], tut[1])
        sleep(1)
        tarif = True
    return tarif


def keyP(key):
    keyboard.press(key)
    sleep(0.15)
    keyboard.release(key)
    sleep(0.15)


def shipPos():
    sh = pyautogui.locateOnScreen('shiptext.png', region=(0, 0, 1366, 768), grayscale=True, confidence=0.8)
    if sh:
        return sh


def shield_search():
    text = tess.image_to_string(screenshot(region=(shipposx + 25, shipposy + 50, 50, 15)))
    if text:

        try:
            fayt = int(str(text).replace(',', ""))
            global shield
            shield = fayt
        except:
            print("hata" + text)

        if shield > 400000:
            1 == 1
        elif shield > 300000:
            keyP('8')
            keyP('4')
        elif shield < 70000:
            keyP('5')
            keyP('4')
            global wait
            wait = True


# if pyautogui.locateOnScreen('sh90.png', region=(shipposx+30, shipposy+50, 50, 15), grayscale=True, confidence=0.5):
#     shield = 90
# elif pyautogui.locateOnScreen('sh50.png', region=(shipposx, shipposy, shipx, shipy), grayscale=True,
#                             confidence=0.5):
#  shield = 50
# keyP('4')
# elif pyautogui.locateOnScreen('sh33.png', region=(shipposx, shipposy, shipx, shipy), grayscale=True,
#                             confidence=0.5):
#  shield = 33
# keyP('5')
# else:
#   shield = 0
# print(shield)


def confi_search():
    if pyautogui.locateOnScreen('confi1.png', region=(shipposx, shipposy, shipx, shipy), grayscale=True,
                                confidence=0.9):
        print("confi 1")
        return 1

    elif pyautogui.locateOnScreen('confi2.png', region=(shipposx, shipposy, shipx, shipy), grayscale=True,
                                  confidence=0.9):
        print("confi 2")
        return 2

    else:
        print("confi bulunamadı")


def map_search():
    if pyautogui.locateOnScreen('3-6.png', region=(0, 0, 1366, 768), grayscale=True, confidence=0.95):
        current_map = "3-6"
    else:
        current_map = "others"


def hp_search():
    text = tess.image_to_string(screenshot(region=(shipposx + 25, shipposy + 26, 60, 20)))
    if text:

        try:
            fayt = int(str(text).replace(',', ""))
            global hp
            hp = fayt
        except:
            print("hata" + text)

        if hp > 300000:
            1 == 1
        elif hp > 150000:
            1 == 1
        elif hp < 70000:

            print("hp 33 kritik")
            if confi == 2:
                keyP('c')
            cor = [portalx, portaly]
            map_s(cor)
            keyP('5')
            sleep(5)
            keyP('4')


def map_s(cor):
    if pyautogui.locateOnScreen('map.png', region=(0, 0, 1366, 768), grayscale=True, confidence=0.8):
        mapc = pyautogui.locateOnScreen('map.png', region=(0, 0, 1366, 768), grayscale=True, confidence=0.8)
        if mapc:
            leftClick(mapc[0] + cor[0], (mapc[1] + cor[1]))
            sleep(1)


t1 = threading.Thread(target=calistir, args=("thread-1",))
t1.start()
while 1:
    # hp_search()

    buldu = False
    if wait==False:
        if patlama:
            print("tamir ediliyor portalda")
            cor = [235, 185]
            print("hp 33 kritik595")
            if confi == 2:
                keyP('c')
            map_s(cor)
            sleep(1)
            map_s(cor)
            # sleep(600)
            patlama = False

        elif pyautogui.locateOnScreen('isaret.png', region=(0, 0, 1366, 768), grayscale=True, confidence=0.8) != None:
            confi = confi_search()
            print("confi")
            keyP('5')
            if confi == 2:
                keyP('c')

            sleep(0.1)
        elif pyautogui.locateOnScreen('kutu1.png', region=(0, 0, 1366, 768), grayscale=True, confidence=0.8) != None:
            cada = pyautogui.locateOnScreen('kutu1.png', region=(0, 0, 1366, 768), grayscale=True, confidence=0.8)
            print("I can see it X")
            if cada:
                if pyautogui.locateOnScreen('task2.png', region=(0, 0, 1366, 768), grayscale=True, confidence=0.8):
                    print("saldırı başlayabilir")
                    sleep(0.5)
                    cada = pyautogui.locateOnScreen('task2.png', region=(0, 0, 1366, 768), grayscale=True,
                                                    confidence=0.8)
                    if cada:
                        leftClick(cada[0] + 70, cada[1] + 70)
                        sleep(0.5)
                        buldu = True
                        while pyautogui.locateOnScreen('task2.png', region=(0, 0, 1366, 768), grayscale=True,
                                                       confidence=0.6):
                            ara = False
                            if pyautogui.locateOnScreen('parca1.png', region=(0, 0, 1366, 768), grayscale=True,
                                                        confidence=0.6):
                                ara = True
                            if pyautogui.locateOnScreen('parca2.png', region=(0, 0, 1366, 768), grayscale=True,
                                                        confidence=0.6):
                                ara = True
                            if pyautogui.locateOnScreen('parca3.png', region=(0, 0, 1366, 768), grayscale=True,
                                                        confidence=0.6):
                                ara = True
                            if ara == False:
                                buldu == False
                                break

                            print("saldırılıyor2")

                            keyP('1')
                            keyP('2')
                            keyP('1')

                            if confi == 1:
                                keyP('c')
                                confi = 2
                            keyP('4')
                            keyP('7')
                            keyP('8')
                            sleep(0.2)




        else:

            if buldu:

                buldu = False

                if m1 == 1:
                    map_s(c1)
                    m1 = 2
                else:
                    map_s(c2)
                    m = 1
            if times > 5:
                if pyautogui.locateOnScreen('parca1.png', region=(0, 0, 1366, 768), grayscale=True,
                                            confidence=0.8) != None:
                    times = 0
                elif pyautogui.locateOnScreen('parca2.png', region=(0, 0, 1366, 768), grayscale=True,
                                              confidence=0.8) != None:
                    times = 0
                elif pyautogui.locateOnScreen('parca3.png', region=(0, 0, 1366, 768), grayscale=True,
                                              confidence=0.8) != None:
                    times = 0
                elif pyautogui.locateOnScreen('isaret.png', region=(0, 0, 1366, 768), grayscale=True,
                                              confidence=0.8) == None:
                    times = 0

                    if confi == 2:
                        keyP('c')
                        confi = 1
                    if m1 == 1:
                        map_s(c1)
                        m1 = 2

                    else:
                        map_s(c2)
                        m1 = 1

            time.sleep(0.1)
            times = times + 1
    else:
        cor = [portalx, portaly]
        map_s(cor)
        sleep(5)
        cor = [portalx, portaly]
        map_s(cor)
        sleep(25)
        wait=True
