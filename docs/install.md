
# installation options 

### installing using setup file
Cookie aims to be dynamic and contained. For this reason, it uses the standard
Python 3 installation package file `setup.py`. This one file contains all the 
installation information the package needs, pre-built! To install the entire
Cookie package, run this command:
```
python setup.py install 
```

### building project from source
Alternatively, if you are using a UNIX-based system with an older
version of Python, feel free to build the entire project from
source. 

First of all, we need to install all requirements listed
in the file `requires.txt`. Next, we need to build a tarball.
```
pip install -r requires.txt
python setup.py sdist
```
After you have completed the first two steps, navigate
to `/dist` and make sure `Cookie.tar.gz` exists.
Go ahead and unpack it and move the `cookie` folder to
the following directory:
```
/usr/lib/python3/dist-packages/
```
There you go!
