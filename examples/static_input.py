
import cookie

@cookie.cookie 
def main (name = None):
	name2 = input("name? ")
	if name == name2:
		print("checks out.")
	else:
		print("your names arent the same.")

if __name__ == "__main__":
	if cookie.is_cookie(main):
		main()
