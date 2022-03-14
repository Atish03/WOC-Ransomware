import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

class encryptFile:
	def __init__(self, file, key):
		#convert our key to 256 bit hash
		self.key = hashlib.sha256(key.encode()).digest(); self.file = file

		#blocksize of AES i.e 128 bit
		self.block_s = AES.block_size

		#pad the file content to fit the block_size


