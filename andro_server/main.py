from pyautogui import *
import pytesseract as tess
import pyautogui
import time
import keyboard
import random
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
tpx=0
tpy=0
def arabox(x,y,z,f):
    cadar = pyautogui.locateCenterOnScreen('bonusbox.png', region=(x, y, z, f), grayscale=True, confidence=0.8)
    if cadar:
        cadar = pyautogui.locateCenterOnScreen('sari.png', region=(x, y, z, f), grayscale=True, confidence=0.8)
    if cadar:
        return cadar[0], cadar[1]

def bonusbox(threadName):
    while 1:
        sleep(0.1)
        mm = arabox(80, 30, 1100, 700)
        if mm:
            leftClick(mm[0], mm[1])
            sleep(0.5)
            mm = arabox(500, 250, 350, 300)
            if mm:
                leftClick(mm[0], mm[1])
                sleep(0.5)







def calistir(threadName):
    global shipposx
    global shipposy
    while True:
        global patlama
        patlama = repair()
        sh = shipPos()
        if sh:
            sh7ipposx = sh[0]
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
    sleep(0.04)
    keyboard.release(key)
    sleep(0.04)


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
        mapc = pyautogui.locateOnScreen('map.png', region=(0, 0, 1366, 768), grayscale=True, confidence=0.8)
        if mapc:
            leftClick(mapc[0] + cor[0], (mapc[1] + cor[1]))
            sleep(1)

def okuust():


    text = tess.image_to_string(screenshot(region=(580, 0, 100, 142)))
    try:
        str_t=False
        str_t=str(text).__contains__("Attacking")
        if str_t:
            print("var")
            global saldiri
            saldiri=True
    except:
        1==1



def ara():
    if pyautogui.locateCenterOnScreen('cros.png', region=(100, 68, 1100, 700), grayscale=False,
                                      confidence=0.25):
        print("51")
        return True
    if pyautogui.locateCenterOnScreen('7.png', region=(100, 68, 1100, 700), grayscale=True,
                                      confidence=0.7):
        print("1")
        return True
    if pyautogui.locateCenterOnScreen('1.png', region=(100, 68, 1100, 700), grayscale=True,
                                      confidence=0.7):
        print("1")
        return True
    else:
        return False


serefp = "0"
tuttu = False


def calistir2(threadName):
    kurulum()
    global tuttu
    global serefp
    while (True):
        okuust()
        if (seref(serefp)):
            global saldiri
            saldiri = False
            tuttu = False


def seref(seref_temp):
    # cadas= pyautogui.locateCenterOnScreen('kutu1.png', region=(1160, 465, 70, 17), grayscale=True,                                      confidence=0.7)
    # if cadas:
    temp = None
    global tpx
    global tpy
    try:

        temp = tess.image_to_string(screenshot(region=(tpx+20, tpy+6, 75, 18)))
    except:
        1 == 1
    if temp:
        global serefp
        try:
            if seref_temp != temp:
                serefp = str(temp)
                print(serefp)
                return True
            else:
                serefp = str(temp)
                return False
        except:
            return False
    print("1")
    return False


def araenemy():
    datess = datetime.datetime.now()
    cadar = pyautogui.locateCenterOnScreen('saimon.png', region=(100, 68, 1100, 700), grayscale=True, confidence=0.55)
    if cadar:
            print(datess - datetime.datetime.now())
            return cadar[0]+30, cadar[1]-20

def kurulum():

    while(True):
        catada = pyautogui.locateOnScreen('user.png', region=(0, 0, 1366, 768), grayscale=False, confidence=0.95)
        if catada:
         global tpx
         global tpy
         tpx=catada[0]
         tpy=catada[1]
         break

saldiri=False
#t1 = threading.Thread(target=calistir, args=("thread-1",))
t3 = threading.Thread(target=bonusbox, args=("thread-3",))
t2 = threading.Thread(target=calistir2, args=("thread-2",))
t2.start()
t3.start()
buldu = False
wait = False
tutx = 0
tuty = 0
tiklandi = False
tut = 0
time_temp = 0
bulamadicount=0

while 1:
    # hp_search()

        cada = araenemy()
        ffd=False
        if cada and not (cada[0]>140 and cada[1]>530):
            leftClick(cada[0] + 10, cada[1] - 13)


            keyP('2')
            keyP('1')
            okuust()
            leftClick((cada[0] + 675) / 2, (cada[1] + 394) / 2)
            tutx = cada[0]
            tuty = cada[1]
            bulamadicount=0
            if(saldiri):
                leftClick(600, 400)
                keyP('7')
                keyP('8')
                keyP('8')



            cikis=0
        while (saldiri):
            cikis+=1
            if (cikis>10):
                serefp+="999"

            keyP('2')

            keyP('3')
            sleep(0.05)
            keyP('1')
            sleep(0.15)
            ff = serefp
            tut = 0
        else:
            bulamadicount+=1
        if (bulamadicount>15):
            keyP('7')
            leftClick( random.randint(1275, 1275+66), random.randint(606, 641))
            bulamadicount=-25


