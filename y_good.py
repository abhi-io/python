import pyautogui
from PIL import Image
import time
jpgfile = Image.open("templ5.png")
for i in range (6):
        x, y = pyautogui.locateCenterOnScreen(jpgfile, grayscale=False)
        pyautogui.click(x,y)
        print x,y,"main" 
        for i in range (4):
                
                y=y+119
                 
                pyautogui.click(x,y)
                print x,y
                time.sleep(1)
        pyautogui.vscroll(-8) 
        time.sleep(3)
