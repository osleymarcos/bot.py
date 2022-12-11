import time
from datetime import datetime
from selenium import webdriver
import os

for i in range(1000):
    dtatual = datetime.now()
    print(dtatual)
    
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('https://www.siteview.com.br/ai.php?id=SV0AD662AE')
    time.sleep(20)
    # driver.get('https://www.siteview.com.br/SV0AD662AE')
    # time.sleep(20)
    # driver.get('https://www.siteview.com.br/gp.php?id=SV0AD662AE')
    # time.sleep(20)
    # driver.get('http://r.siteview.com.br/?id=SV0AD662AE')
    # time.sleep(20)
    # driver.get('http://a.siteview.com.br/?id=SV0AD662AE')
    # time.sleep(20)
    # driver.get('http://www.siteview.com.br/rdl.php?i=SV0AD662AE')
    # time.sleep(20)
    # driver.get('http://l.siteview.com.br/r.php?id=SV0AD662AE')
    # time.sleep(20)
    i += 1
    print(i, 'executada')
    # driver.quit()
    os.system("taskkill /f /im chrome.exe")
    os.system("taskkill /f /im chromedriver.exe")
    # os.system("taskkill /f /im msedgewebview2")
    # os.system("taskkill /f /im msedge.exe")

    
