from pynput.keyboard import Key, Controller, Listener
import time
import threading

def process_keys(key):
    if str(key) == "Key.f2":
        return False

def main():
    keyboard = Controller()
    print('Press f2 to type the text of content.txt file.')
    while True:
        stop = False
        with Listener(on_press = process_keys) as listener:
            listener.join()
        with open('content.txt', 'r') as file:
            while True:
                data = file.read(512)
                if not data:
                    break
                keyboard.type(data)
                time.sleep(0.5)

        
if __name__ == '__main__':
    main()