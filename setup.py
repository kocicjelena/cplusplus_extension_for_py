#!/usr/bin/env python
import os
import sys
# To use a consistent encoding
from codecs import open
from os import path
from setuptools import setup, find_packages
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
#with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
#    long_description = f.read()
from distutils.core import Extension
from distutils.sysconfig import get_python_inc, get_python_lib

incdir =  [
    os.path.join(here, "cplusplus_extension_for_py"),
    get_python_lib(),
    get_python_inc(),
    os.path.join(get_python_lib(plat_specific=1), 'c_module')
]
#incdir = os.path.join(get_python_inc(plat_specific=1), 'Numerical')
#inpydir = os.path.join(get_python_lib(plat_specific=1), 'c_module')
#files = ["myimplementation/*"]
c_module_for_py = Extension('c_module',
include_dirs=[incdir],
							sources = ['c_module.c'])

setup(name = 'c_module',
      version = '1.0',
      description = 'C Extension',
      ext_modules = [c_module_for_py],
      entry_points={
        'console_scripts': [
            'myimplementation=myimplementation:main',
        ]
      },
     url='https://github.com/kocicjelena/cplusplus_extension_for_py',
	  test_suite = "test.myimplementation_unittest",
	author='jk',
      author_email='kocicjelena@gmail.com')
