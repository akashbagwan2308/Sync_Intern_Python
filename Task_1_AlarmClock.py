#  Alarm Clock Using Python
#  admin : Akash Bagwan
# date : 01/07/23
# --------------------------------------------------------------------------------------------------------

from tkinter import *
import datetime
import time
import pygame
from pygame import mixer
import threading
from tkinter import messagebox

# --------------------------------------------------------------------------------------------------------

root = Tk()

root.geometry("580x350")
root.title("Alarm Clock")

head = Label(root,text = "Alarm Clock",font=("comic sans",20))
head.grid(row=0,columnspan=3)

alarmtime = StringVar()
msgin = StringVar()

mixer.init()


def ala():
    alarmT = alarmtime.get()

    currentTime = time.strftime("%H:%M")

    while alarmT != currentTime:
        currentTime = time.strftime("%H:%M")
    if alarmT==currentTime:
        mixer.music.load("tone.mp3")
        mixer.music.play()
        msg = messagebox.showinfo("Info",f"{msgin.get()}")
        if msg =="ok":
            mixer.music.stop()



clockimg = PhotoImage(file="clk2.png")
img = Label(root,image=clockimg)
img.grid(row= 3,rowspan=4,column=0)

inputTime = Label(root,text="Set Time (Hr:Min)",font=("comic sans",18))
inputTime.grid(row=1,column=3)

altime =Entry(root,textvariable=alarmtime,font=("comic sans",19),width=18)
altime.grid(row=2,column=3)

msg = Label(root,text="Message",font=("comic sans",18))
msg.grid(row=3,column=2,columnspan=2)

msginput = Entry(root,textvariable=msgin,font=("comic sans",19),width=18)
msginput.grid(row=4,column=2,columnspan=2)

submit = Button(root,text="Set Alarm",font=("comic sans",17),command=ala)
submit.grid(row=5,column=3,columnspan=2)

root.mainloop()