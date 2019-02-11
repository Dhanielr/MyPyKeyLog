from pynput import mouse
import logging

logging.basicConfig(filename="/home/dhaniel/Gitlab/PyKeyl/mouse_log.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

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