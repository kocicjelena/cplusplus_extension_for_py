#!/usr/bin/python
#
# Copyright 2017 
#
import c_module
import os, sys
class CExtExample:

  def __init__(self):
      pass
  def run(self):
    print (c_module.calc_stat())
def main():
  sample = CExtExample()
  sample.run()


if __name__ == '__main__':
  main()
