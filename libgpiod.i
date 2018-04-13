%module libgpiod
%{
#include "gpiod.h"
%}

// Define the __attribute__ macro because SWIG doesn't know of its existence
// and gets confused.
#define __attribute__(x)

// This is really ugly to manually define the timespec type from time.h
// however SWIG can't process the file.  This seems like a shocking omission
// or problem with SWIG and any interface to POSIX libraries--something is
// clearly not right and needs to be investigated (cannot find any info online
// about this issue).  For now just force the timespec type to be defined
// using basic types.
struct timespec
{
  long tv_sec;
  long tv_nsec;
};

%include "gpiod.h"
