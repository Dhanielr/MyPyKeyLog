from pynput import mouse
import logging
import time
import os
from datetime import datetime

DATE_FILE = datetime.now().strftime('%d%m%Y')
DATE_LOG = datetime.now().strftime('%d/%m/%Y %H:%M')
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

if os.path.exists(f'{BASE_DIR}/.logs/') == False:
    os.mkdir(f'{BASE_DIR}/.logs/')

logging.basicConfig(filename=f"{BASE_DIR}/.logs/mouse_log_{DATE_FILE}.log", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_move(x, y):
    logging.info(f"Mouse moveu para {x, y}")

def on_click(x, y, button, pressed):
    if pressed:
        logging.info(f"Mouse clicou em {x, y, button}")

def on_scroll(x, y, dx, dy):
    logging.info(f"Mouse scrolled em {x, y, dx, dy}")

a = mouse.Listener()

with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
