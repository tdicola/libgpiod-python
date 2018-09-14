# libgpiod Python Wrapper
# Simple SWIG-based interface to the libgpiod library for modern Linux GPIO
# character device access.  Directly wraps the libgpiod library from:
#   https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/
# Author: Tony DiCola
from setuptools import setup, Extension


libgpiod_module = Extension('_libgpiod',
                            sources=['libgpiod.i'],
                            swig_opts=['-I/usr/include'],
                            libraries = ['gpiod'])

setup(
    name='libgpiod',
    version='0.1',
    description='Python interface to the libgpiod Linux GPIO character device library.',
    url='https://github.com/tdicola/libgpiod-python',
    author='Tony DiCola',
    author_email='tony@tonydicola.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    ext_modules=[libgpiod_module],
    py_modules=['libgpiod']
)
