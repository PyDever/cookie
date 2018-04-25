
# installing cookie
<hr>

### standard installation
Cookie is designed to be scalable and contained. For this reason, I decided to use
`setuptools` as my installation method. `setuptools` should be
standard library. If you face issues, run this command.
```
pip install setuptools
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

