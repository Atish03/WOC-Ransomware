import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import time

class edFile:
	def __init__(self, key):
		#convert our key to 256 bit hash
		self.key = hashlib.sha256(key.encode()).digest()

		#blocksize of AES i.e 128 bit
		self.block_s = AES.block_size

	#pad the file content to fit the block_size
	def padIt(self, file):
		content = open(file, "rb").read()
		tChars = self.block_s - (len(content) % self.block_s)
		return content + bytes(chr(tChars) * tChars, "utf-8")

	def unpadIt(self, text):
		return text[:text[-1] * -1]

	def encrypt(self, file):
		padded = self.padIt(file)
		#initialize a vector of size as the block_size
		starting_vector = Random.new().read(self.block_s)
		cipher = AES.new(self.key, AES.MODE_CBC, starting_vector)
		return b64encode(starting_vector + cipher.encrypt(padded)).decode("utf-8")

	def decrypt(self, encryption):
		decoded = b64decode(encryption)
		vector = decoded[:self.block_s]
		cipher = AES.new(self.key, AES.MODE_CBC, vector)
		return self.unpadIt(cipher.decrypt(decoded[self.block_s:]))






