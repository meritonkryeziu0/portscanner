#!/usr/bin/env python

import socket
import time
import sys

start_time = time.time()

# For creativity

class xcolors:
	HEADER = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	RED = '\033[91m'
	ENDX = '\033[0m'
def main():
	# host = str(raw_input('Enter the host ip: '))

	try :
		if sys.argv[1] == "-h" or sys.argv[1] == "--help" or sys.argv[1] == "?":
			print "Usage: python port_scanner.py [HOST]"
		        print "Example: python port_scanner.py XX.XX.XX.XX "

	except IndexError:
		print "Usage: python port_scanner.py [HOST]"
		print "Example: python port_scanner.py XX.XX.XX.XX "



	def try_port(port):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(0.1)
		try:
			s.connect((sys.argv[1], port))
		except socket.error:
			return False
		try:
			data = s.recv(4096)
			s.close()
			return True
		except socket.timeout:
			s.close()
			return True

	# def timer():
	# 	now = time.localtime(time.time())
	# 	return now[5]
	def scan():
		found_ports = []
		timer = 0
		for port in range(1,65535):
			connected = try_port(port)
			if connected:
				found_ports.append(port)
		return found_ports 
	if scan() == "0":
		pass
	else:
		print "Open ports:"+ xcolors.RED + str(scan()) + xcolors.ENDX
		# print "Scan completes in : ["+xcolors.BLUE + str(default_timer()-start) +"]"+xcolors.ENDX

main()
print("Scan Finished in %s seconds" % (round((time.time() - start_time),4)))
