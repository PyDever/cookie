
# Usage Examples #

## Hello, Cookie!
Using cookie is literally easier than counting to one hundred. 
Observe this simple example:
```python
import cookie

@cookie.cookie
def main (name=None, age=None):
	if name and number:
		print("Hello, " + name + ".")
		print("I see you are " + age + " years old.")

if __name__ == "__main__":
	main()
```
now we can run our app the following ways:
```
$ python test.py --name Kaleb -a 15
$ python test.py --help
$ python test.py -n Kaleb --age 15
$ python test.py -n Kaleb -a 15
```

## Multiple Arguments
We can use `.split(',')` to split whatever argument.
```
import cookie
import math

@cookie.crumble
def main (numbers=None, ehco=None):
	results = []
	numbers = numbers.split(',')
	for number in numbers:
		number = int(number)
		fact = math.factorial(number)
		if echo == True:
			print(fact)
		else:
			pass

if __name__ == "__main__":
	main()
```
now we can run our app like this:
```
$ python test.py -n 5,6,7 -e True
120
720
5040

$ python test.py -n 5,6,7 -e False
```


