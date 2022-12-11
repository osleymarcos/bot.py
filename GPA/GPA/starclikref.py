import webbrowser as wb
import pyautogui
import time

wb.open("file:///C:/Users/18-02003/iCloudDrive/testeeee.html")
time.sleep(5)

for i in range(102):
    pyautogui.moveTo(1430, 114, 1)
    pyautogui.click()
    
    time.sleep(25)
    
    pyautogui.vscroll(-1000)
    pyautogui.vscroll(1000)
    pyautogui.moveTo(1387, 45, 1)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(1454, 46, 1)
    pyautogui.click()
    time.sleep(2)
    
