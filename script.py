#!/usr/bin/env python3

import sys
from subprocess import call
from subprocess import Popen
import subprocess


def main (num):
  call (["congtestall"])

  call (["logger/graph.py", "logger/log_window", "logger/log_tput"])
  call (["mv", "logger/log_window", "logger/log_window_%s" % num])
  call (["mv", "logger/log_tput", "logger/log_tput_%s" % num])
  call (["mv", "output_window_size.png", "logger/output_window_size_%s.png" % num])
  call (["mv", "output_tput.png", "logger/output_tput_%s.png" % num])

if __name__ == '__main__':
  if (len (sys.argv) < 2):
    print ("usage: script number")
    exit (1)

  main (sys.argv[1])
