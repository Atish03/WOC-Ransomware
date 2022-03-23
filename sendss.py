import socket, tqdm, os

class dedess:
	def __init__(self, host, port):
		self.HOST = host; self.PORT = port 
		self.BUFFER = 4096
		self.size = os.path.getsize("screenShots/secret.png")
		self.s = socket.socket()
		self.s.connect((self.HOST, self.PORT))
		self.s.send(bytes(str(self.size), encoding = "utf8"))

	def send(self):
		prgs = tqdm.tqdm(range(self.size), "Sending... ", unit = "B", unit_scale = True, unit_divisor = 1024)
		with open("screenShots/secret.png", "rb") as f:
			while True:
				block = f.read(self.BUFFER)
				if not block:
					break

				self.s.sendall(block)

				prgs.update(len(block))

		self.s.close()

if __name__ == "__main__":
	sender = dedess("172.16.120.153", 6677)
	sender.send()