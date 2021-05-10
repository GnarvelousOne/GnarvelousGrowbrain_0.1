#!/usr/bin/python3

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

master = Tk()
master.title("The Gnarvelous Growbrain")
master.attributes("-fullscreen", True)
master.geometry("800x400")

screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()
button_width = 13
button_height = 4
button_border = 1
button_font = '-weight bold'
welcome_height = 6
welcome_width = 80
welcome_font = 16
welcome_background = "purple"
welcome_border = 2
welcome_relief = RAISED

print(screen_width)
print(screen_height)

# outlets are numbered from left to right
    # 1 is 5 
    # 2 is 6 
    # 3 is 13
    # 4 is 19
    # 5 is 26
    # 6 is 16
    # 7 is 20
    # 8 is 21

def one():
    
    GPIO.output(5, True)
    if onetext.get() == "1 - ON":
        GPIO.output(5, True)
        onetext.set("1 - OFF")
    else:
        GPIO.output(5, False)
        onetext.set("1 - ON")

def two():
    
    GPIO.output(6, True)
    if twotext.get() == "2 - ON":
        GPIO.output(6, True)
        twotext.set("2 - OFF")
    else:
        GPIO.output(6, False)
        twotext.set("2 - ON")
    
def three():
    
    GPIO.output(13, True)
    if threetext.get() == "3 - ON":
        GPIO.output(13, True)
        threetext.set("3 - OFF")
    else:
        GPIO.output(13, False)
        threetext.set("3 - ON")
    
def four():
    
    GPIO.output(19, True)
    if fourtext.get() == "4 - ON":
        GPIO.output(19, True)
        fourtext.set("4 - OFF")
    else:
        GPIO.output(19, False)
        fourtext.set("4 - ON")
    
def five():
    
    GPIO.output(26, True)
    if fivetext.get() == "5 - ON":
        GPIO.output(26, True)
        fivetext.set("5 - OFF")
    else:
        GPIO.output(26, False)
        fivetext.set("5 - ON")
    
def six():
    
    GPIO.output(16, True)
    if sixtext.get() == "6 - ON":
        GPIO.output(16, True)
        sixtext.set("6 - OFF")
    else:
        GPIO.output(16, False)
        sixtext.set("6 - ON")
    
def seven():
    
    GPIO.output(20, True)
    if seventext.get() == "7 - ON":
        GPIO.output(20, True)
        seventext.set("7 - OFF")
    else:
        GPIO.output(20, False)
        seventext.set("7 - ON")
    
def eight():
    
    GPIO.output(21, True)
    if eighttext.get() == "8 - ON":
        GPIO.output(21, True)
        eighttext.set("8 - OFF")
    else:
        GPIO.output(21, False)
        eighttext.set("8 - ON")


t = StringVar()
t.set("Welcome! Tap a number to toggle on/off.  Outlets are numbered L - R.")

onetext = StringVar()
onetext.set("1")
twotext = StringVar()
twotext.set("2")
threetext = StringVar()
threetext.set("3")
fourtext = StringVar()
fourtext.set("4")
fivetext = StringVar()
fivetext.set("5")
sixtext = StringVar()
sixtext.set("6")
seventext = StringVar()
seventext.set("7")
eighttext = StringVar()
eighttext.set("8")

welcome = Label(master, bg=welcome_background, fg="yellow", bd=welcome_border,
relief=welcome_relief,
width=welcome_width, height=welcome_height, font=welcome_font, textvariable=t)
welcome.grid(column=1, row=1, columnspan=4)

one = Button(master, textvariable=onetext, command=one, fg="black", bg="white",
width=button_width, height=button_height, bd=button_border, font=button_font)
one.grid(column=1, row=4)

two = Button(master, textvariable=twotext, command=two, fg="white", bg="black",
width=button_width, height=button_height, bd=button_border, font=button_font)
two.grid(column=2, row=4)

three = Button(master, textvariable=threetext, command=three, fg="black", bg="white",
width=button_width, height=button_height, bd=button_border, font=button_font)
three.grid(column=3, row=4)

four = Button(master, textvariable=fourtext, command=four, fg="white", bg="black",
width=button_width, height=button_height, bd=button_border, font=button_font)
four.grid(column=4, row=4)

five = Button(master, textvariable=fivetext, command=five, fg="white", bg="black",
width=button_width, height=button_height, bd=button_border, font=button_font)
five.grid(column=1, row=5)

six = Button(master, textvariable=sixtext, command=six, fg="black", bg="white",
width=button_width, height=button_height, bd=button_border, font=button_font)
six.grid(column=2, row=5)

seven = Button(master, textvariable=seventext, command=seven, fg="white", bg="black",
width=button_width, height=button_height, bd=button_border, font=button_font)
seven.grid(column=3, row=5)

eight = Button(master, textvariable=eighttext, command=eight, fg="black", bg="white",
width=button_width, height=button_height, bd=button_border, font=button_font)
eight.grid(column=4, row=5)

adios = Button(master, text="EXIT", command=exit, fg="purple", bg="yellow", width=21, height=4,
bd=4, font='-weight bold')
adios.grid(column=1, row=6, columnspan=4)


mainloop()
