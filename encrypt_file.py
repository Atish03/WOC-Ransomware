import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

key = "this_is_a_key"

#blocksize of AES i.e 128 bit
block_s = AES.block_size

#convert our key to 256 bit hash
key = hashlib.sha256(key.encode()).digest()
