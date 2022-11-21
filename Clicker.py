import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from tkinter import *
from PIL import ImageTk, Image
import threading

# Constant Variables

count = 0
level = 1
auto_click_level = 1
a_cost = 0
cp_cost = 10
clicking_power_text = "Clicking Power - "+str(cp_cost)
auto_power_text = "Auto Power - "+str(a_cost)
upgrades = 0
upgrades_text = ('Total Upgrades - '+str(upgrades))

# Functions

def raise_a_price():
    global count
    global a_cost
    count = count-a_cost
    counter['text']=count
    a_cost = round((a_cost*1.20)+2)
    auto_button['text']="Auto Power - "+str(a_cost)

def raise_cp_price():
    global count
    global cp_cost
    count = count-cp_cost
    counter['text']=count
    cp_cost = round((cp_cost*1.25)+1.5)
    click_power_button['text']="Clicking Power - "+str(cp_cost)

def upgrade_auto_click_level():
    global a_cost
    global count
    if a_cost > count:

        pass

    else:
        global auto_click_level
        global upgrades
        auto_click_level = (auto_click_level * 1.15)+1
        raise_a_price()
        upgrades+=1
        text = ('Total Upgrades - '+str(upgrades))
        upgrades_label_text['text'] = text


def auto_click():
    global a_cost
    global count
    global auto_click_level
    threading.Timer(2.0, auto_click).start()
    count+=auto_click_level
    count = round(count)
    counter['text']=str(count)
    auto_button['command']=upgrade_auto_click_level

    if a_cost == 0:
        global upgrades
        a_cost = round((a_cost*1.20)+2)
        auto_button['text']="Auto Power - "+str(a_cost)
        upgrades+=1
        text = ('Total Upgrades - '+str(upgrades))
        upgrades_label_text['text'] = text


def upgrade_level():
    global count
    global cp_cost
    if cp_cost > count:

        pass

    else:
        global level
        global upgrades
        level = (level * 1.1)+2
        raise_cp_price()
        upgrades+=1
        text = ('Total Upgrades - '+str(upgrades))
        upgrades_label_text['text'] = text



def append_counter():
    global level
    global count
    count+=level
    count = round(count)
    counter['text']=str((count))

# Window

window = tk.Tk()
window.geometry("800x700")
window.title('Cookie Clicker')

# Image

img = ImageTk.PhotoImage(Image.open('/Users/anthonyvalle/Clicker_game/cookie.png'))

# Frame

frame = Frame(window,  bg='light blue')
frame.pack(fill='both', expand=1)

# "Welcome to" label

welcome_label = Label(frame, text='Welcome to Cookie Clicker',  bg='light blue', font=('Halbfette Secession', 40))
welcome_label.pack(pady=(20,0))

# "By Anthony" Label

by_label = Label(frame, text='By - Anthony Valle',  bg='light blue', font=('Halbfette Secession', 25))
by_label.pack()

# Git Label

git_label = Label(frame, text='Github - anthonyvalle',  bg='light blue', font=('Halbfette Secession', 25))
git_label.pack(pady=(0, 40))

# Cookie Button

cookie_button = Button(frame,image=img, bg='blue', command=append_counter).pack(pady=5)

# Counter for your score

counter = Label(frame, text='0',bg='light blue',font=('Halbfette Secession', 30))
counter.pack(pady=(5,5))

# Cost for Clicking Power

click_power_button=tk.Button(frame, text=clicking_power_text, command=upgrade_level)
click_power_button.pack()

# Cost for AUto Power

auto_button=tk.Button(frame, text=auto_power_text, command=auto_click)
auto_button.pack()

# Label for # of times you've upgraded

upgrades_label_text = Label(frame, text = upgrades_text, bg='light blue',font=('Halbfette Secession', 30))
upgrades_label_text.pack(pady=(10))








window.mainloop()
