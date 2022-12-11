import time
from datetime import datetime
import pyautogui
import webbrowser as wb
import pyscreeze
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
from pytesseract import pytesseract
import pyscreeze
for i in range(1, 1500):
    
    print("------------------------------")
    dtatual = datetime.now()
    print(dtatual)
    chrome_options = Options()
    chrome_options.add_extension('c:/temp/tiktok.crx')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-popup-blocking')
    chrome_options.add_argument('C:/Users/18-02003/AppData/Local/Google/Chrome/User Data/Default')
    chrome_options.add_argument(
        '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 '
        '(kHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    driver = webdriver.Chrome(executable_path="c:/temp/driver/chromedriver.exe", chrome_options=chrome_options)
    
    driver.get("https://app.ganheporassistir.com/login")
    driver.maximize_window()
    time.sleep(1)
    cpf = driver.find_element(By.NAME, 'cpf')
    cpf.send_keys('92723365972')
    cpf.submit()
    time.sleep(3)
    
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    time.sleep(3)
    
    print("TIKTOK1")
    img_tiktok = pyautogui.locateCenterOnScreen('c:/temp/tiktok.png', confidence=0.9)
    time.sleep(1)
    pyautogui.moveTo(img_tiktok.x, img_tiktok.y, 1)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    
    print("TIKTOK2")
    img_tiktok2 = pyautogui.locateCenterOnScreen('c:/temp/tiktok2.png', confidence=0.9)
    if img_tiktok2 != " ":
        wb.open("https://www.tiktok.com/pt-BR/")
    else:
        time.sleep(1)
        pyautogui.moveTo(img_tiktok2.x, img_tiktok2.y, 1)
        time.sleep(1)
        pyautogui.click()
    
    # time.sleep(15)
    # #fazendo verificação do pop up
    # pyscreeze.screenshot()
    # im = pyscreeze.screenshot(region=(600, 500, 200, 200))
    # im.save(r"c:\temp\tela.jpg")
    # path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    # image_path = r"c:\temp\tela.jpg"
    # img = Image.open(image_path)
    # pytesseract.tesseract_cmd = path_to_tesseract
    # text = pytesseract.image_to_string(img)
    # #print(text)
    # palavra = "Depois"
    # if palavra not in text:
    #     print("CLOSE")
    #     img_close = pyautogui.locateCenterOnScreen('c:/temp/close.png', confidence=0.7)
    #     pyautogui.moveTo(img_close.x, img_close.y, 1)
    #     time.sleep(1)
    #     pyautogui.click()
    # else:
    #     print("DPS")
    #     img_dps = pyautogui.locateCenterOnScreen('c:/temp/dps.png', confidence=0.7)
    #     time.sleep(1)
    #     pyautogui.moveTo(img_dps.x, img_dps.y, 1)
    #     pyautogui.click()
    
    time.sleep(1205)
    i = i + 1
    print(i, ' - Execuções')
    print("------------------------------")

    driver.quit()
