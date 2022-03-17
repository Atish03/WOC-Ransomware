#nocode
from encrypt_file import edFile
import os, time

time.clock = time.time

ed = edFile("this_is_my_very_secure_key")

def encrypt_folder(folder):
	contents = os.listdir(folder)
	for c in contents:
		f = os.path.join(folder, c)
		if os.path.isfile(f):
			e = ed.encrypt(f)
			open(f, "wb").write(bytes(e, encoding = "utf-8"))
		else:
			encrypt_folder(f)

def decrypt_folder(folder):
	contents = os.listdir(folder)
	for c in contents:
		f = os.path.join(folder, c)
		if os.path.isfile(f):
			e = open(f, "rb").read().decode()
			try:
				d = ed.decrypt(e)
				open(f, "wb").write(d)
			except:
				pass
		else:
			decrypt_folder(f)