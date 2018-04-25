
# installing cookie
<hr>

***Due to issues with PyPi, Cookie will not be pip installable for a while***
# standard installation
Cookie is designed to be scalable and contained. For this reason, I decided to use
`distutils` as my installation method. `distutils` should be
standard library. If you face issues, run this command.
```
pip install distutils
```
After you have confirmed that `distutils` is installed, go ahead and download
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

