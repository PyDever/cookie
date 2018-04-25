from distutils.core import setup

setup(
    name='cookie',
    version='2.0dev',
    author='Kaleb R. Horvath',
    url='https://github.com/PyDever/cookie',
    packages=['cookie'],
    test_suite='tests.test',
    license='BSD',
    long_description=open('README.md').read(),
)

