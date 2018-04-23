
import cookie

@cookie.cookie
def main (name=None, number=None):

	if name: 
		print("Why hello there " + name)
	else: 
		if number:
			print(int(number)*2)
		else:
			print("well roll me down!")

if __name__ == "__main__":
	main()
