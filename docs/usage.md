
# Usage Examples #
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
okay... now what? well, hop over to your copy
of the shell and run your python file:
```
python my_cookie.py
```
you get nothing. huh. try running and asking for help.
```
python my_cookie.py --help

Usage: my_cookie.py [-n NAME | --name NAME] 
		    [-a AGE | --age AGE]
```
Wow! Cookie automatically generated a help page.
You can also invoke this piece of art with:
```
python my_cookie.py -h
```
According to our help page, I need to use `-n` or `--name`
to pass my name and `-a` or `--age` to pass my age.
```
python my_cookie.py --name Programmer -a 15

Hello, Programmer.
I see you are 15 years old.
```
Wow! Just using the `@cookie.cookie` method decorator converts
a standard python funciton into a command line argument parser!
