import socket, tqdm, os, datetime

class ssdede:
	def __init__(self, host, port):
		self.HOST = host; self.PORT = port 
		self.BUFFER = 4096

		self.s = socket.socket()
		self.s.bind((self.HOST, self.PORT))

		self.s.listen(5)

		self.conn, self.addr = self.s.accept()

		print(self.conn)

	def recieve(self):
		filesize = int(self.conn.recv(self.BUFFER).decode())

		prgs = tqdm.tqdm(range(filesize), "Receiving... ", unit = "B", unit_scale = True, unit_divisor = 1024)
		with open("capturedScreenShots/" + datetime.datetime.now().strftime("%X") + ".png", "wb") as f:
			while True:
				block = self.conn.recv(self.BUFFER)
				if not block:
					break

				f.write(block)

				prgs.update(len(block))

		self.conn.close()
		self.s.close()

if __name__ == "__main__":
	receiver = ssdede("172.16.120.153", 6677)
	receiver.recieve()



