import time
from datetime import datetime

import pyautogui

is_class = False

while True:
    data = open("data.txt", 'r')
    for i in data:
        a = i.split()
        li = a[1]
        pas = a[2]
        ti = a[0].split(':')
        current_mins = datetime.now().time().minute
        current_hrs = datetime.now().time().hour
        if int(ti[0]) == int(current_hrs):
            if int(ti[1]) == int(current_mins):
                print(f"uh ho you've got a zoom meeting now:-- {current_hrs}:{current_mins}")
                pyautogui.click(x=614, y=745)
                time.sleep(1)
                pyautogui.hotkey('windows', 'up')
                time.sleep(1)
                pyautogui.click(x=532, y=288)
                time.sleep(1)
                pyautogui.typewrite(li)
                pyautogui.hotkey('enter')
                time.sleep(7)
                pyautogui.typewrite(pas)
                pyautogui.hotkey('enter')
                time.sleep(1800)
            else:
                continue
        else:
            continue

    data.close()
