
# installing cookie
<hr>

***Due to issues with PyPi, Cookie will not be pip installable for a while***
# standard installation
Cookie is designed to be scalable and contained. For this reason, I decided to use
`setuptools` as my installation method. `setuptools` should be
standard library. If you face issues, run this command.
```
pip install setuptools
```
Additionally, `setuptools` will be installed among other things if you
run this simple command.
```
pip install -r requires.txt
```
After you have confirmed that `setuptools` is installed, go ahead and download
the Cookie source code from github.
```
git clone https://github.com/PyDever/cookie
```
After you have grabbed the source, you need to install it.
```
python setup.py build
python setup.py install
```
Now you can import `cookie` from anywhere on your machine.

### remote installation
For my foreign friends, feel free to access a pypi mirror.
```
pip install
```

