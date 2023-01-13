# IMPORTING THE NECESSARY IMPORTS
# PIP INSTALL PYNPUT NEEDED
import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

# THIS CODE IS TO SAY WHICH KEY U WANT TO BE THE KEY THAT ACTIVATE CLICKING
TOGGLE_KEY = KeyCode(char="t")

# CLICKING SET TO FALSE ELSE CLICKING WILL START 
clicking = False
mouse = Controller()

# CLICKER FUNCTION TO START THE CLICKING WHILE CLICKING IS TRUE CLICKING SHOULD BE CLICKED
def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
            time.sleep(0.001)
        else:
            time.sleep(0.001)

# TOGGLE EVENT IS TO CHECK IF THE KEY IS BEING PRESSED AND RUN THE CLICKER
def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking

# THE CHECKING FOR CLICKS AND CLICKING SHOULD HAPPEN AT THE SAME TIME SE WE USE THREADING
click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()