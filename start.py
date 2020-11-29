from datetime import date
from tkinter import *
import datetime
from tkinter import ttk, Label
import keyboard
from tkinter import messagebox

date = date.today()
date = str(date)
dates: list[str] = date.split('-')


def show_entry_fields(self):
    print("hrs: %s\nmin: %s\nid: %s\npassword: %s" % (e1.get(), e2.get(), e3.get(), e4.get()))
    print("-------------------------------------------------------")
    hrs = int(e1.get())
    min = int(e2.get())
    li = int(e3.get())
    pas = e4.get()
    ww = open('data.txt', 'a+')
    ww.write(f'{hrs}:{min} {li} {pas}\n')
    ww.close()
    www = open('dara.txt', 'a+')
    www.write(f'\n{hrs}:{min} {li} {pas}                                            $ {date}')
    www.close()
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    # e4.delete(0, 'end')


def show_entry_fieldss():
    print("hrs: %s\nmin: %s\nid: %s\npassword: %s" % (e1.get(), e2.get(), e3.get(), e4.get()))
    print("-------------------------------------------------------")
    hrs = int(e1.get())
    min = int(e2.get())
    li = int(e3.get())
    pas = e4.get()
    ww = open('data.txt', 'a+')
    ww.write(f'{hrs}:{min} {li} {pas}\n')
    ww.close()
    www = open('dara.txt', 'a+')
    www.write(f'\n{hrs}:{min} {li} {pas}                                            $ {date}')
    www.close()
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    # e4.delete(0, 'end')


we = datetime.datetime.now()


def end(self):
    master.destroy()
    import main


def endd():
    master.destroy()
    import main


def other():
    bu = Button(master, text='clear all the previously added meetings', command=clear_restt, ).grid(row=7, column=1,
                                                                                                    columnspan=3)
    buu = Button(master, text='show all the previously added meetings', command=show, ).grid(row=8, column=1,
                                                                                             columnspan=3)


def clear_rest(self):
    a = open('data.txt', 'w')
    a.close()
    messagebox._show('deleted', ' all the previously added meetings have been deleted')


def clear_restt():
    a = open('data.txt', 'w')
    a.close()
    messagebox._show('deleted', ' all the previously added meetings have been deleted')


def show():
    a = open('data.txt')
    ab = a.read()
    messagebox._show('meetings', ab)
    a.close()


master = Tk()
master.title('enter the meeting details below')
master.iconbitmap('zoom.ico')
Label(master, text="Enter the time of the meeting in 24 hr format").grid(row=0, column=0, columnspan=3)
Label(master, text="Hrs :").grid(sticky=E, row=1)
Label(master, text="Min :", width=4).grid(sticky=E, row=1, column=2)
e1 = Entry(master, width=10)
e2 = Entry(master, width=10)
e1.grid(sticky=W, row=1, column=1)
e2.grid(sticky=W, row=1, column=3)
Label(master, text="Enter the meeting details").grid(sticky=W, row=3, column=0, columnspan=3)
Label(master, text="ID :").grid(sticky=E, row=4)
Label(master, text="Password :").grid(sticky=E, row=4, column=2)
e3 = Entry(master, width=10)
e4 = Entry(master, width=10)
e3.grid(sticky=W, row=4, column=1)
e4.grid(sticky=W, row=4, column=3)
e4.insert(END, f'{dates[2]}{dates[1]}{dates[0]}')
Button(master, text='save Info', command=show_entry_fieldss).grid(sticky=W, row=6, column=0)
Button(master, text='done', command=endd).grid(row=6, column=1)
Button(master, text='Other options', command=other).grid(row=6, column=3)

master.bind("<Delete>", clear_rest)
master.bind("<Escape>", end)
master.bind("<Return>", show_entry_fields)
master.mainloop()
