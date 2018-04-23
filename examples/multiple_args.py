
from cookie import cookie, crumble

# this simple cookie file uses classes and other things

""" 
use @crumble for small main functions
use @cookie for larger more complex functions
"""

errors = {
	"noargs": "cookie: no arguments provided.",
	"invalid": "cookie: invalid arguments given."
}

# simple factorial funciton using reccursion
def factorial (n):
	if n == 0:
		return 1
	else:
		return n * (factorial(n-1))

# now we can bake our cookie
@cookie
def main_method (numbers=None):
	global errors
	if not errors:

		print("cookie: please provide error frame.")

	elif numbers and errors:

		for number in numbers.split(','):

			# assert that number is integer type
			number = int(number)

			# call non-baked function, or "dough"
			print(factorial(number))

	else:
		print(errors['noargs'])

# application starter boilerplate using standard dunders
if __name__ == "__main__":
	main_method()


