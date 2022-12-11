import time
import pyautogui
import pyscreeze
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import schedule as schedule

from PIL import Image
from pytesseract import pytesseract


pyscreeze.screenshot()
im = pyscreeze.screenshot(region=(550, 250, 115, 105))
im.save(r"c:\temp\tela.jpg")
im.show()
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"c:\temp\tela.jpg"
img = Image.open(image_path)
pytesseract.tesseract_cmd = path_to_tesseract
text = pytesseract.image_to_string(img)
print(text)

# palavra = "Depois"
# if palavra not in text:
#     print("A frase não tem " + palavra)
# else:
#     print("A frase tem " + palavra)
    