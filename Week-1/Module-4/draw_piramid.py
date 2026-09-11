import time
import pyautogui

num = int(input())

time.sleep(3)

for i in range(1, num + 1):
    pyautogui.typewrite('#' * i)
    pyautogui.press('enter')

