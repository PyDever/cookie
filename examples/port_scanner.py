
import cookie
import socket

@cookie.cookie
def main (address = None, ports = None):

	# turn ports string argument into list of strings
	ports = ports.split(',')

	if ports and address:
		# before anything, we must turn ports into numeric list
		ports = [int(port) for port in ports]
	else:
		pass

	# now we must make a simple port scanning class
	class PortScanner (object):
		def __init__ (self, address_string, ports_list):
			self.address_string = address_string
			self.ports_list = ports_list

		def scan (self):
			# create socket object
			socketObject = socket.socket(2,1) # AF_INET
			for port in self.ports_list:
				try:
					socketObject.connect((self.address_string,
						port))
					print (port, " open")
				except socket.error:
					print (port, " closed")

	# create instance of our class
	if ports is not None:
		portScanner = PortScanner(str(address), ports)
		portScanner.scan()
	else:
		print("No ports given.")

if __name__ == "__main__":
	main()

