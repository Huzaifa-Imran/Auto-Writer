from pynput.keyboard import Key, Controller, Listener
import threading

def process_keys(key):
    if str(key) == "Key.f2":
        with open('content.txt', 'r') as file:
            autowriter.type(file.read())

def main():
    global autowriter
    autowriter = Controller()
    print('Press f2 to type the text of content.txt file')
    keylog = Listener(on_press = process_keys)
    with keylog:
        keylog.join()

        
if __name__ == '__main__':
    main()