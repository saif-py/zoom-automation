from datetime import date
from tkinter import *
import datetime
from tkinter import ttk

date = date.today()
date = str(date)
dates: list[str] = date.split('-')


def show_entry_fields():
    print("hrs: %s\nmin: %s\nid: %s\npassword: %s" % (e1.get(), e2.get(), e3.get(), e4.get()))
    hrs = int(e1.get())
    min = int(e2.get())
    li = int(e3.get())
    pas = e4.get()
    ww = open('data.txt', 'a+')
    ww.write(f'\n{hrs}:{min} {li} {pas}')
    ww.close()
    www = open('dara.txt', 'a+')
    www.write(f'\n{hrs}:{min} {li} {pas}                                            $ {date}')
    www.close()
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')


we = datetime.datetime.now()


def end():
    master.destroy()
    import main


def other():
    bu = Button(master, text='clear all the previously added meetings', command=clear_rest, ).grid(row=7, column=1,
                                                                                                   columnspan=3)


def clear_rest():
    a = open('data.txt', 'w')
    a.close()


master = Tk()
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
Button(master, text='save Info', command=show_entry_fields).grid(sticky=W, row=6, column=0)
Button(master, text='done', command=end).grid(row=6, column=1)
Button(master, text='Other options', command=other).grid(row=6, column=3)
master.mainloop()
