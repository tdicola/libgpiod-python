%module libgpiod
%{
#include "gpiod.h"
%}

// Define the __attribute__ macro because SWIG doesn't know of its existence
// and gets confused.
#define __attribute__(x)

%include "gpiod.h"
