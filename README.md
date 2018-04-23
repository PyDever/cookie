# Cookie
 [![Build status](https://ci.appveyor.com/api/projects/status/pjxh5g91jpbh7t84?svg=true)](https://ci.appveyor.com/project/tygerbytes/resourcefitness) 
[![Coveralls](https://coveralls.io/repos/github/tygerbytes/ResourceFitness/badge.svg?branch=master)](https://coveralls.io/github/tygerbytes/ResourceFitness?branch=master) 

<img src="https://openclipart.org/download/249534/1464300474.svg" width=80><img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" width="230"/>

**Version 1.0**

Cookie is a simple argument parser for Python 3 that turns 
functions into full-blow command line argument parsers without
you even knowing!

## installation
```
$ pip install -r requires.txt
$ python setup.py install
```
see `docs` for more info.

## usage
```python
import cookie

@cookie.cookie
def main (name=None):
  print("hello, " + name)
  
main()
```
see `examples` for more info.

## documentation
see `docs` for documentation.
it needs work. contributions are welcome.

## changelog
see `changelog.txt` for the changelog.

