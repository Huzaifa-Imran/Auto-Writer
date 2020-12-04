from pynput.keyboard import Key, Controller
import time

def main():
    keyboard = Controller()
    time.sleep(5)
    with open('content.txt', 'r') as file:
        text = file.read()
        keyboard.type(text)

        
if __name__ == '__main__':
    main()