import time
import webbrowser as wb
from datetime import datetime
import keyboard
import pyautogui
import pyscreeze
from PIL import Image
from pytesseract import pytesseract

for i in range(1, 1500):
    print("------------------------------")
    dtatual = datetime.now()
    print(dtatual)

    url = "http://app.ganheporassistir.com/login"
    wb.
    wb.open(url)
    time.sleep(2)
    keyboard.write('92723365972')
    time.sleep(5)
    
    print("ENTRAR")
    img_tiktok = pyautogui.locateCenterOnScreen('c:/temp/btnentrar.png', confidence=0.7)
    pyautogui.moveTo(img_tiktok.x, img_tiktok.y, 1)
    pyautogui.click()
    time.sleep(3)
    
    pyautogui.press('pagedown')
    pyautogui.press('pagedown')

    time.sleep(5)
    print("TIKTOK1")
    img_tiktok = pyautogui.locateCenterOnScreen('c:/temp/tiktok.png', confidence=0.7)
    pyautogui.moveTo(img_tiktok.x, img_tiktok.y, 1)
    pyautogui.click()
    time.sleep(3)

    pyautogui.press('pagedown')
    pyautogui.press('pagedown')
    pyautogui.press('pagedown')
    
    print("TIKTOK2")
    img_tiktok2 = pyautogui.locateCenterOnScreen('c:/temp/tiktok2.png', confidence=0.7)
    time.sleep(1)
    pyautogui.moveTo(img_tiktok2.x, img_tiktok2.y, 1)
    time.sleep(1)
    pyautogui.click()
    
    time.sleep(15)
    #fazendo verificação do pop up
    pyscreeze.screenshot()
    im = pyscreeze.screenshot(region=(600, 500, 200, 200))
    im.save(r"c:\temp\tela.jpg")
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path = r"c:\temp\tela.jpg"
    img = Image.open(image_path)
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(img)
    #print(text)
    palavra = "Depois"
    if palavra not in text:
        print("CLOSE")
        img_close = pyautogui.locateCenterOnScreen('c:/temp/close.png', confidence=0.7)
        pyautogui.moveTo(img_close.x, img_close.y, 1)
        time.sleep(1)
        pyautogui.click()
    else:
        print("DPS")
        img_dps = pyautogui.locateCenterOnScreen('c:/temp/dps.png', confidence=0.7)
        time.sleep(1)
        pyautogui.moveTo(img_dps.x, img_dps.y, 1)
        pyautogui.click()
    
    time.sleep(1205)
    i = i + 1
    print(i, ' - Execuções')
    print("------------------------------")
    

