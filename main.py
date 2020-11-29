import time
from datetime import datetime
import tkinter
import pyautogui
import os
import subprocess


loop = True
if os.stat("data.txt").st_size == 0:
    loop = False
    print("no data found!!!!")
ab = open('data.txt')
if loop:
    print(f'meetings that are added to join are')
for i in ab:
    if i != '\n':
        b = i.split()
        print(b[0])
ab.close()
while loop:
    print("waiting for the next meeting to start")
    data = open("data.txt", 'r')
    for i in data:
        if i != '\n':
            a = i.split()
            li = a[1]
            pas = a[2]
            ti = a[0].split(':')
            current_mins = datetime.now().time().minute
            current_hrs = datetime.now().time().hour
            if int(ti[0]) == int(current_hrs):
                if int(ti[1]) == int(current_mins):
                    pyautogui.hotkey('enter')
                    print(f"uh ho you've got a zoom meeting now :-- {current_hrs}:{current_mins}")
#                     pyautogui.click(x=614, y=745)
                    subprocess.Popen(r"path\to\zoom.exe")
                    time.sleep(1)
                    pyautogui.hotkey('windows', 'up')
                    time.sleep(1)
                    root = tkinter.Tk()
                    screen_width = root.winfo_screenwidth()
                    screen_height = root.winfo_screenheight()
                    width = 0.3894 * screen_width
                    heght = 0.375 * screen_height
                    pyautogui.click(x=width, y=heght)
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
                time.sleep(8)
                continue
        else:
            continue

    data.close()

