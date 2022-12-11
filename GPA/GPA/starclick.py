import webbrowser as wb
import pyautogui
import time

wb.open("https://www.star-clicks.com/portal/ads")
time.sleep(6)

for i in range(79):
    pyautogui.moveTo(1700, 13, 1)
    pyautogui.click()

    time.sleep(6)
    
    pyautogui.moveTo(2193, 734, 1)
    pyautogui.click()
    
    time.sleep(6)



