import datetime
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os
for i in range(1000):
    
    dtatual = datetime.now()
    print(dtatual)
    chrome_options = Options()
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 '
         '(kHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    # chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) '
    #                             'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1')
    
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://app.ganheporassistir.com/login")
    driver.maximize_window()
    time.sleep(2)
    cpf = driver.find_element(By.NAME, 'cpf')
    cpf.send_keys('92723365972')
    time.sleep(2)
    cpf.submit()
    time.sleep(1)
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    
    img_you = pyautogui.locateCenterOnScreen('c:/temp/youtube.png', confidence=0.7)
    time.sleep(1)
    pyautogui.moveTo(img_you.x, img_you.y, 1)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)
    
    pyautogui.moveTo(1341, 144, 1)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1321, 157, 1)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    
    link = driver.find_element(By.NAME, 'url')
    page = 'https://www.youtube.com/watch?v=OVyRNv9Tl4Q'
    link.send_keys(page)
    link.submit()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print('assistindo')
    time.sleep(1580)
    i += 1
    
    os.system("taskkill /f /im chrome.exe")
    os.system("taskkill /f /im chromedriver.exe")
   #driver.quit()
    print(i, 'executada')