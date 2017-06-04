#!/usr/bin/env python
import os
import sys
from distutils.core import setup, Extension
from distutils.sysconfig import get_python_inc, get_python_lib
incdir = os.path.join(get_python_inc(plat_specific=1), 'Numerical')
#inpydir = os.path.join(get_python_lib(plat_specific=1), 'c_module')
#files = ["myimplementation/*"]
c_module_for_py = Extension('c_module',
include_dirs=[incdir],
							sources = ['c_module.c'])

setup(name = 'c_module',
      version = '1.0',
      description = 'C Extension',
      ext_modules = [c_module_for_py],
      py_modules=['myimplementation'],
      url='https://github.com/kocicjelena/cplusplus_extension_for_py',
	  test_suite = "test.myimplementation_unittest",
	  scripts = ["runner"],
      author='jk',
      author_email='kocicjelena at gmail dot com')
