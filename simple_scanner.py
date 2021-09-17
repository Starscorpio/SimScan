import sys
import socket
from datetime import datetime

#Defining target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #converting hostname to IP address
else:
		print("Not enough or too much arguments")
		print("Use: python3 %s <ip>")

#Adding a banner and name
print("-" * 50)
print("Scanning started for host: " + target)
print("Time of scan: "+ str(datetime.now()))
print("-" * 50)
print("/" + "-" * 5 + " " * 10 + "kdjdkfj")

try:
		for port in range(1,65535):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			result = s.connect_ex((target, port)) #returns error if any
			try:
				service = socket.getservbyport(port, 'tcp') #get service name running on port
				#banner = s.send('howareyou\r\n')
				#bannerrecv = s.recv(100)
			except:
				continue
			if result == 0:
					print("Port {} is open".format(port))
					print("Service running on the port is " + service) 
					#print(port)
					#print(bannerrecv)

			s.close()

except KeyboardInterrupt:
		print("\nKeyboard Interrupt: Closing program")
		sys.exit()

except socket.gaierror:
		print("Not able to resolve your hostname: Please provide a new hostname")
		sys.exit()

except socket.error:
		print("Couldn't connect to the damn server")
		sys.exit()
