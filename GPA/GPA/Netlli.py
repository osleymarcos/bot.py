import time
from selenium import webdriver
from datetime import datetime

for i in range(50):
    driver = webdriver.Chrome(executable_path="C:/temp/driver/chromedriver.exe")
    driver.get("https://nettli.plus/go/PVy3x")
    time.sleep(30)
    i += 1
    print(i, 'executada')
    dtatual = datetime.now()
    print(dtatual)
    driver.quit()
    