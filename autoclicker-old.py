# importing time and threading
import time
import threading
import pynput.mouse

# pynput.keyboard is used to watch events of
# keyboard for start and stop of auto-clicker
import pynput.keyboard

def on_press(key):
    try:
        keyboard.press(',')
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

listener = keyboard.Listener(on_press=on_press)
listener.start()