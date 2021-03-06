#!/usr/bin/env python3
from tkinter import Tk, Label, Button, LEFT, RIGHT, BOTH
from tkinter.font import Font
from util import get_logger

log = get_logger(__name__)
paused = True
# Duration in second
duration = 0
# Loop time in millisecond
loopTime = 1000


def calc_duration(d):
    hours, remainder = divmod(d, 3600)
    mintues, seconds = divmod(remainder, 60)
    log.info('calc duration: %s, %s, %s', hours, mintues, seconds)
    # return '{:02}:{:02}:{:04.1f}'.format(int(hours), int(mintues), seconds)
    return '{:02}:{:02}:{:02.0f}'.format(int(hours), int(mintues), seconds)


def run():
    global paused, duration, loopTime

    if paused:  # End infinite recursive loop
        return
    # Update duration
    duration += loopTime / 1000
    displayLabel.config(text=calc_duration(duration))

    # After ${loopTime} millisecond, call run again (start an infinite recursive loop)
    master.after(loopTime, run)


def reset():
    global duration, paused
    duration = 0
    paused = True
    displayLabel.config(text=calc_duration(duration))
    startButton.config(text='Start')


def start_or_stop():
    global startButton, paused
    paused = not paused
    startButton.config(
        text='Start') if paused else startButton.config(text='Stop')
    master.after(1, run)  # after 1 millisecond, start Run


def quit():
    global master
    master.quit()


master = Tk()
master.winfo_toplevel().title("Stop Watcher")
master.geometry('400x200')

displayLabel = Label(master, text=calc_duration(duration), font=Font(family='Consolas', size=70))
displayLabel.pack(fill=BOTH, expand=1)

buttonFont = Font(family='Consolas', size=15)
buttonStyle = dict(font=buttonFont, pady=15)
Button(master, cnf=buttonStyle, text='Reset', command=reset).pack(
    fill=BOTH, expand=1, side=LEFT)
startButton = Button(master, cnf=buttonStyle,
                     text="Start", command=start_or_stop)
startButton.pack(fill=BOTH, expand=1, side=RIGHT)
# Button(master, cnf=buttonStyle, text='Quit', command=quit).pack(side=LEFT)

master.mainloop()
