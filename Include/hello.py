import pyautogui

pyautogui.PAUSE= 0.1
pyautogui.FAILSAFE = True

def Locate():
    im = pyautogui.screenshot()
    x, y = pyautogui.center(pyautogui.locateOnScreen('button.png'))
    return x,y

def  Toclick(x,y):
     pyautogui.click(x - 150, y - 150)
     pyautogui.hotkey('ctrl', 'v')
     pyautogui.click(x, y)


try:
    x,y=Locate()
    while True:
        Toclick(x,y)
except:
    print('\nExit.')

