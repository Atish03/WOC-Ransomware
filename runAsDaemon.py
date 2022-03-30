import daemon
import time

def main():
	for _ in range(100):
		time.sleep(5)
		print("hello world")

with daemon.DaemonContext():
	main()
