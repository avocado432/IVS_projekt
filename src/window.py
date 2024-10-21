# This file is part of TBD Calculator.
#
# TBD Calculator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TBD Calculator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TBD Calculator. If not, see <https://www.gnu.org/licenses/>.
"""
@file window.py
@brief Tkinter GUI view

@author Tereza Magerková (xmager00)
@date April 13, 2024

@example
python3 window.py
"""

import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

import controller

from os import path


#---------------------------------------------------------------------------
#                               WINDOW
#---------------------------------------------------------------------------
window = ttk.Window(themename='minty')
window.title('TBD Calculator')

iconfile = path.abspath(path.join(path.dirname(__file__), 'resources/icon.png'))
icon = tk.PhotoImage(file=iconfile)
window.iconphoto(True, icon)

#styles
style = ttk.Style()
style.configure('secondary.TButton', font=('Helvetica', 18), foreground='#2F2F2F')

#cat image source https://www.pinterest.com/pin/676595544042893345/
imagefile = path.abspath(path.join(path.dirname(__file__), 'resources/cat.png'))
image = tk.PhotoImage(file=imagefile)


number_buttons = [("7",0,0), ("8",0,1), ("9",0,2),
                  ("4",1,0), ("5",1,1), ("6",1,2),
                  ("1",2,0), ("2",2,1), ("3",2,2),
                  ("0",3,0), (".",3,1), ("?",3,2)]
operation_buttons = [("/",0,1), ("*",1,1), ("-",2,1), ("+",3,1),
                     ("!",0,2), ("^",1,2), ("√",2,2), ("cat",3,2)]

#entry widget
entry = tk.Entry(master=window, font=('Helvetica', 32))  

#---------------------------------------------------------------------------
#                               FRAMES
#---------------------------------------------------------------------------
#define frames
top_buttons = ttk.Frame(master=window)
bottom_buttons = ttk.Frame(master=window)

brackets_frame = ttk.Frame(master=top_buttons)
clear_frame = ttk.Frame(master=top_buttons)

numbers_frame = ttk.Frame(master=bottom_buttons)

operation_frame = ttk.Frame(master=bottom_buttons)
padding_frame = ttk.Frame(master=operation_frame, width=40)
#---------------------------------------------------------------------------
#                               BUTTONS
#---------------------------------------------------------------------------
#create grids from buttons for numbers and operations
for (text, row, column) in number_buttons:
    if text == "?":
        button = ttk.Button(master=numbers_frame, text=text, width=4,padding='15 15', style='secondary.TButton', command=controller.show_tip)
        button.bind("<Enter>", lambda event, widget=window, text=text: controller.show_message_bubble(event, widget, text))
        button.bind("<Leave>", lambda event, widget=window: controller.hide_message_bubble(event, widget))
    else:
        button = ttk.Button(master=numbers_frame, text=text,padding='15 15', style='secondary.TButton')
        button.bind("<Button-1>", lambda event, entry=entry: controller.button_click_handle(event, entry))
    button.grid(row=row, column=column, sticky="nsew")  
    #layout reacting to window size
    numbers_frame.rowconfigure(row, weight=2) 
    numbers_frame.columnconfigure(column, weight=2) 
    
   

for (text, row, column) in operation_buttons:
    if text == "cat":
        button = ttk.Button(master=operation_frame, text=" ", width=4,padding='15 15', image=image, 
                            compound="center", style='secondary.TButton', command=controller.cat_click_handle)
    else:
        button = ttk.Button(master=operation_frame, text=text, width=4,padding='15 15', style='secondary.TButton')
        button.bind("<Button-1>", lambda event, entry=entry: controller.button_click_handle(event, entry))

    button.bind("<Enter>", lambda event, widget=window, text=text: controller.show_message_bubble(event, widget, text))
    button.bind("<Leave>", lambda event, widget=window: controller.hide_message_bubble(event, widget))
    button.grid(row=row, column=column, sticky="nsew") 
    #layout reacting to window size
    operation_frame.rowconfigure(row, weight=1)
    operation_frame.columnconfigure(column, weight=1)

#backspace and clear buttons
clear_button = ttk.Button(master=clear_frame, text='C', width=4,padding='15 15', style='secondary.TButton')
backspace_button = ttk.Button(master=clear_frame, text='←', width=4,padding='15 15', style='secondary.TButton')

clear_button.bind("<Button-1>", lambda event, entry=entry: controller.button_click_handle(event, entry))
backspace_button.bind("<Button-1>", lambda event, entry=entry: controller.button_click_handle(event, entry))

clear_button.pack(side='left')
backspace_button.pack(side='right')

#brackets buttons
lbracket_button = ttk.Button(master=brackets_frame, text='(', width=4,padding='15 15', style='secondary.TButton')
rbracket_button = ttk.Button(master=brackets_frame, text=')', width=4,padding='15 15', style='secondary.TButton')

lbracket_button.bind("<Button-1>", lambda event, entry=entry: controller.button_click_handle(event, entry))
rbracket_button.bind("<Button-1>", lambda event, entry=entry: controller.button_click_handle(event, entry))

lbracket_button.pack(side='left')
rbracket_button.pack(side='right')

#pack widgets into frames
brackets_frame.pack(side='left')
clear_frame.pack(side='right')
numbers_frame.pack(side='left', expand=True, fill='both')
padding_frame.grid(row=0, column=0)
operation_frame.pack(side='right', fill='both') 

#pack widget frames into window
entry.pack(fill='x', padx=10, pady=10)
top_buttons.pack(padx=10, pady=10, fill='x')
bottom_buttons.pack(padx=10, pady=10, fill='x')
#evaluation button
eval_button = ttk.Button(master=window, text='=', width=4,padding='15 15', style='secondary.TButton')
eval_button.bind("<Button-1>", lambda event, entry=entry: controller.button_click_handle(event, entry))
eval_button.pack(fill='x', padx=10, pady=10)

#run window
window.bind("<Key>", lambda event, entry=entry: controller.keyboard_input_handle(event, entry))
entry.bind("<Button-1>", lambda event: "break")
window.mainloop()

# ********************     end of window.py file     ******************** 