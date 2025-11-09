import pynput        

def on_press(key):
    print(key)


key_listener = pynput.keyboard.Listener(on_press=on_press)

with key_listener:
    key_listener.join()
# This script listens for keyboard events and prints "key" whenever a key is pressed.
