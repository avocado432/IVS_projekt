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
@file controller.py
@brief Tkinter GUI controller

@author Tereza Magerková (xmager00)
@date April 13, 2024

"""

import tkinter as tk
import math_lib as ml

from os import path
import subprocess

show_tip = False

soundfile = path.abspath(path.join(path.dirname(__file__), 'resources/cat_meow.wav'))

class TipBubble:
    '''
    @brief the TipBubble class creates a user tip popup
    '''
    def __init__(self, widget, message):
        '''
        @brief Constructor for TipBubble class
        @param widget master widget for text frame
        @param message text of the popup
        '''
        self.widget = widget
        self.message = message
        # create the message bubble frame
        self.bubble_frame = tk.Frame(widget, bg='#ADD8E6', relief='solid', name="tipbubble")
        self.bubble_label = tk.Label(self.bubble_frame, text=message, bg='#ADD8E6', padx=10, pady=20)
    def show(self):
        '''
        @brief displays the message and packs the frame into root widget
        '''
        self.bubble_label.pack()
        self.bubble_frame.pack()

def button_click_handle(event, entry_widget):
    '''
    @brief Button click handler
    @param entry_widget 
    @param event

    @todo clear input after error
    '''
    if hasattr(event, 'widget'):
        text = event.widget.cget("text")
    else:
        text = event

    expression = entry_widget.get()
    
    if text == "=":
        result = ml.evaluate_expression(expression)
        if result is None:
            result = "Error"
        entry_widget.delete(0, tk.END)
        entry_widget.insert(tk.END, str(result))

    elif text == "C":
        entry_widget.delete(0, tk.END)
        
    elif text == "←":
        entry_widget.delete(len(entry_widget.get()) - 1, tk.END)
    
    else:
        entry_widget.insert(tk.END, text)

def keyboard_input_handle(event, entry_widget):
    '''
    @brief Button click handler
    @param entry_widget 
    @param event

    '''
    if event.keysym in ["Return", "KP_Enter"]:
        button_click_handle("=", entry_widget)
    elif event.char.isdigit() or event.char in ['+', '-', '*', '/', '(', ')', '.']:
        entry_widget.insert(tk.END, event.char)
    elif event.keysym == "BackSpace":
        entry_widget.delete(len(entry_widget.get()) - 1, tk.END)

def cat_click_handle():
    '''
    @brief Cat button click handle. Plays meow sound
    '''
    try:
        # Use subprocess to run the aplay command
        subprocess.run(["aplay", soundfile], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def show_tip():
    '''
    @brief Toggles user tip messages
    '''
    global show_tip
    show_tip = not show_tip

def show_message_bubble(event, widget, text):
    '''
    @brief displays user tip messages
    @param event 
    @param widget root widget for the message text frame
    @param text text of the button that created event
    '''
    if(text == "cat"):
        message_bubble = TipBubble(widget, "MEOW?")
        
    elif(text == "+"):
        message_bubble = TipBubble(widget, "Addition \n a + b")
        
    elif(text == "-"):
        message_bubble = TipBubble(widget, "Subtraction \n a - b \n This button can be used as unary minus - a")
        
    elif(text == "*"):
        message_bubble = TipBubble(widget, "Multiplication \n a * b")
        
    elif(text == "/"):
        message_bubble = TipBubble(widget, "Division \n a / b \n Tip: Did you know you should not divide by 0?")
        
    elif(text == "!"):
        message_bubble = TipBubble(widget, "Factorial \n n !")
        
    elif(text == "^"):
        message_bubble = TipBubble(widget, "nth power of x \n n ^ x ")
        
    elif(text == "√"):
        message_bubble = TipBubble(widget, "nth root of x \n n √ x")
        
    elif(text == "?"):
        message_bubble = TipBubble(widget, "Click to enable/disable tips")
       
    else:
        message_bubble = TipBubble(widget, "")

    if show_tip:
        message_bubble.show()

def hide_message_bubble(event, widget):
    '''
    @brief displays empty tip message
    @param event 
    @param widget root widget for the message text frame
    '''
    message_bubble = TipBubble(widget, "")
    if show_tip:
        message_bubble.show()



# ********************     end of controller.py file     ******************** 