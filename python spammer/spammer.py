import pyautogui as gui
import time
time.sleep(1)
for i in range(100):
    gui.write('something')
    time.sleep(1)
    gui.press('enter')
    print(f'message {i} send!')
    time.sleep(1)