
# Usage Examples #

## Hello, Cookie!
Using Cookie is very easy. Here is a simple hello cookie example.
```python
from cookie import Cookie

app = Cookie(__name__)

@app.cookie
def hello_cookie (name=None):
	if name is not None:
		print("Hello, " +name+"!")
		print("My name is Cookie!")
		
if __name__ == "__main__":
	hello_cookie()
```
no we can easily run this from the command line.
```
python hello_cookie.py --name kaleb

Hello, Kaleb!
My name is Cookie!
```
you can also just use `-n` for simplicity. Cookie automatically
generates help pages as well. 
```
python hello_cookie.py --help 

Usage: hello_cookie.py [-n NAME | --name NAME]
   		       [ -h | --help ]
```

## Packaging your app!
Cookie is designed to be scalable and contained. For this reason, the packaging
process is very very simple. Go ahead and create a folder structure similar
to this around your cookie app.
```
cookie-app/
	app/
	|-------hello_cookie.py
	|-------__init__.py
	
	tests/
	|-------test.py
	
	AUTHORS
	requires.txt
	setup.py
```
The most important file here is `requires.txt`. This will tell
the end user of your app what the dependencies are. This file should
look something like this.
```
cookie
example-package1
example-package2
```
The second most important file is `setup.py`. This will make your project installable. This file should
look someting like this.
```
from setuptools import setup
import os

setup(
    name='cookie-app',
    version='0.1dev',
    author='your name here',
    url='link to github repo',
    packages=['app'],
    test_suite='tests.test',
    license='BSD')
```
After you have completed the above, go ahead and make your own 
test in `tests/test.py`. Now that your structure is complete, put your
package on github. 

[Here](https://github.com/PyDever/cookie-app) is a perfect example of a cookie app.
