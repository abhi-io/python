import pyautogui
from PIL import Image
import time
jpgfile = Image.open("templ5.png")
for i in range (1):
        x, y = pyautogui.locateCenterOnScreen(jpgfile, grayscale=False)
        pyautogui.moveTo(x,y)
        print x,y,"main" 
        for i in range (7):
                y=y+60
                pyautogui.moveTo(x,y)
                print x,y
                time.sleep(1)
