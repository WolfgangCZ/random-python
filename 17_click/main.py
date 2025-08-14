from pynput import mouse, keyboard
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
import threading
import time

clicking = False
stop_program = False
mouse_controller = Controller()

TOGGLE_KEY = KeyCode(char='t')  # press 't' to toggle clicking
EXIT_KEY = KeyCode(char='q')    # press 'q' to quit


def click_loop():
    global clicking
    while not stop_program:
        if clicking:
            mouse_controller.press(Button.left)
            mouse_controller.release(Button.left)
            t
            # no sleep → maximum speed
        else:
            time.sleep(0.05)  # reduce CPU usage when idle


def on_press(key):
    global clicking, stop_program
    if key == TOGGLE_KEY:
        clicking = not clicking
        print("Clicking:", clicking)
    elif key == EXIT_KEY:
        stop_program = True
        return False  # stop listener


# Start click loop in background thread
threading.Thread(target=click_loop, daemon=True).start()

# Listen for key presses
with Listener(on_press=on_press) as listener:
    listener.join()
