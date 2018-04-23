
import cookie

@cookie.cookie
def main(name=None, age=None):
	can_drink = False
	if name and age:
		if int(age) >= 21:
			can_drink = True
		else:
			can_drink = False 
		if can_drink:
			print("Hi there " + name + "! Grab a cold one.")
		else:
			print("Hi there " + name + "! Want a soda good buddy?")
	else:
		pass 

if __name__ == "__main__":
	main()

