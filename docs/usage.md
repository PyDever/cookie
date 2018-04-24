
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

## Multiple Arguments & No Echo
We can use `.split(',')` to split whatever argument.
```python
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

## Cookie & Crumble
notice how we use `@cookie.cookie` and `@cookie.crumble`. the latter should be used
for smaller application and the first should be used for more complex, less-scalable
methods and functions.

## Advanced Application
in the `examples` folder, I have included an advanced example. it is a simple port scanner
that allows you to pass an address and a list of ports to be scanned.
```shell
$ python port_scanner.py --address "127.0.0.1" --ports 22,34,80,443,667

22 closed
34 open
80 closed
443 closed
667 open
```

## Conclusion
the posibilities with this library are literally endless. you can not only
do actions with the arguments, you can use them to control the actions like
we did with `--echo`. You can make those arguments filenames and other things.

i encourage you to be creative with this module and use it to its full potential!
