import pynput        
log=""
# creating a global variable to store the log
def on_press(key):
    global log
    log += str(key) 
    print(log)
# This function is called whenever a key is pressed, appending the key to the log and printing it.
key_listener = pynput.keyboard.Listener(on_press=on_press)
# This sets up a listener for keyboard events, calling on_press when a key is pressed.
with key_listener:
    key_listener.join()
# This script listens for keyboard events and prints "key" whenever a key is pressed.
