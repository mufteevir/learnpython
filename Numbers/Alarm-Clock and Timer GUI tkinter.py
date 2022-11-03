"""
A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.
GUI on tkinter
"""

# Importing all the necessary libraries to form the alarm clock:
import datetime
import time
from tkinter import *

import winsound


def alarm2(n):
    while True:
        time.sleep(1)
        print("Wait time:", n, "seconds.")
        n = n - 1
        if n == 0:
            sound()
            break


def alarm1(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:", date)
        print(now)
        print(set_alarm_timer)
        if now == set_alarm_timer:
            sound()
            break


def sound():
    print("Time to Wake up")
    winsound.PlaySound("sound.wav", winsound.SND_ASYNC)


def actual_clock():
    set_alarm_clock = f"{hour_clock.get()}:{min_clock.get()}:{sec_clock.get()}"
    alarm1(set_alarm_clock)


def actual_timer():
    min_value = min_timer.get()
    sec_value = sec_timer.get()
    alarm2(int(min_value) * 60 + int(sec_value))


clock = Tk()
clock.title("DataFlair Alarm Clock and Timer")
# clock.iconbitmap(r"dataflair-logo.ico")
clock.geometry("400x200")
time_format = Label(clock, text="Enter time in 24 hour format xx:xx:xx", fg="red", bg="black", font="Arial").place(
    x=100,
    y=70)
addClock = Label(clock, text="Hour  Min   Sec", font=60).place(x=110)
setYourAlarm = Label(clock, text="Alarm clock", fg="blue", relief="solid", font=("Helevetica", 7, "bold")).place(
    x=30,
    y=30)
setYourAlarm2 = Label(clock, text="Timer", fg="blue", relief="solid", font=("Helevetica", 7, "bold")).place(x=50,
                                                                                                            y=140)

# The Variables we require to set the alarm(initialization):
hour_clock = StringVar()
min_clock = StringVar()
sec_clock = StringVar()
# The Variables we require to set the timer(initialization):
min_timer = StringVar()
sec_timer = StringVar()

# Time required to set the alarm clock:
hourClock = Entry(clock, textvariable=hour_clock, bg="pink", width=15).place(x=110, y=30)
minClock = Entry(clock, textvariable=min_clock, bg="pink", width=15).place(x=150, y=30)
secClock = Entry(clock, textvariable=sec_clock, bg="pink", width=15).place(x=200, y=30)

# To take the time input by user:
submitClock = Button(clock, text="Set Alarm", fg="red", width=10, command=actual_clock).place(x=5, y=70)

# Time required to set the timer:
addTimer = Label(clock, text="Min   Sec", font=60).place(x=130, y=110)
minTimer = Entry(clock, textvariable=min_timer, bg="pink", width=15).place(x=110, y=140)
secTimer = Entry(clock, textvariable=sec_timer, bg="pink", width=15).place(x=160, y=140)

# To take the time input by user:
submitTime = Button(clock, text="Set Timer", fg="red", width=10, command=actual_timer).place(x=5, y=170)

clock.mainloop()
# Execution of the window.
