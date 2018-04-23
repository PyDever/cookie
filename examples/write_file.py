
import cookie

@cookie.cookie 
def main (message = None, filename = None):
	if message and filename:
		with open(filename, 'w') as fileObject:
			fileObject.write(message)
			fileObject.close()
			print("wrote to file " + filename)
	else:
		pass

if __name__ == "__main__":
	main()

