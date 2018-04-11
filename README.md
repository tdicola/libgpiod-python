# libgpiod-python

Simple SWIG-based Python wrapper around the libgpiod modern Linux GPIO character device library.  Directly wraps the libgpiod library from: https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/

## Installation

You must have both libgpiod and SWIG installed then run the following SWIG
command to generate the wrapper:

    swig3.0 -python -I/usr/local/include libgpiod.i

Now use Python's standard setup.py commands to build and install the extension
and module:

    python3 setup.py build_ext
    python3 setup.py install
