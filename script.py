#!/usr/bin/env python3

import sys
from subprocess import call
from subprocess import Popen
import subprocess
from subprocess import run
from time import sleep
#config 1
#run (["netsim", "--bandwidth", "0.0566", "--latency", "100", "--drop", "1", "--limit", "50"])
#config 2
#run (["netsim", "--bandwidth", "100", "--latency", "15", "--drop", "0.001", "--limit", "500"])
#config 3
#run (["netsim", "--bandwidth", "1000", "--latency", "100", "--drop", "0.00001", "--limit", "1000"])
#config 4
#run (["netsim", "--bandwidth", "10000", "--latency", "1", "--drop", "0", "--limit", "50"])

def q1 ():
  call (["rm", "logger/log_window", "logger/log_tput"])
  call (["netsim", "--bandwidth", "10000", "--latency", "1", "--drop", "0", "--limit", "50"])
  call (["congestiontest", "--size", "large"])
  call (["netsim", "--bandwidth", "10000", "--latency", "1", "--drop", "0", "--limit", "10"])
  call (["congestiontest", "--size", "large"])

  call (["logger/graph.py", "logger/log_window", "logger/log_tput"])
  call (["mv", "output_window_size.png", "logger/config4_buffer_output_window_size.png"])
  call (["mv", "output_tput.png", "logger/config4_buffer_output_tput.png"])

def q2 ():
  call (["rm", "logger/log_window", "logger/log_tput"])
  call (["netsim", "--bandwidth", "10000", "--latency", "1", "--drop", "0", "--limit", "50"])
  call (["congestiontest", "--size", "large"])
  call (["netsim", "--bandwidth", "100", "--latency", "1", "--drop", "0", "--limit", "50"])
  call (["congestiontest", "--size", "large"])
  call (["netsim", "--bandwidth", "10000", "--latency", "10", "--drop", "0", "--limit", "50"])
  call (["congestiontest", "--size", "large"])

  call (["logger/graph.py", "logger/log_window", "logger/log_tput"])
  call (["mv", "output_window_size.png", "logger/config4_bandwidth_delay_output_window_size.png"])
  call (["mv", "output_tput.png", "logger/config4_bandwidth_delay_output_tput.png"])

def q3 ():
  call (["rm", "logger/log_window", "logger/log_tput"])
  call (["netsim", "--bandwidth", "10000", "--latency", "1", "--drop", "0", "--limit", "50"])
  call (["congestiontest", "--size", "large"])
  call (["netsim", "--bandwidth", "10000", "--latency", "1", "--drop", "10", "--limit", "50"])
  call (["congestiontest", "--size", "large"])

  call (["logger/graph.py", "logger/log_window", "logger/log_tput"])
  call (["mv", "output_window_size.png", "logger/config4_drop_output_window_size.png"])
  call (["mv", "output_tput.png", "logger/config4_drop_output_tput.png"])

def q4 ():
  call (["rm", "logger/log_window", "logger/log_tput"])
  call (["netsim", "--bandwidth", "10000", "--latency", "1", "--drop", "0", "--limit", "50"])
  run (["congestiontest", "--size", "huge"])
  run (["congestiontest", "--size", "huge"])
  run (["congestiontest", "--size", "huge"])
  run (["congestiontest", "--size", "huge"])
  sleep (5)
  call (["logger/graph.py", "logger/log_window", "logger/log_tput"])

def q5_1 ():
  call (["rm", "logger/log_window", "logger/log_tput"])
  call (["netsim", "--bandwidth", "0.0566", "--latency", "100", "--drop", "1", "--limit", "50"])
  run (["congestiontest", "--size", "large"])
  sleep (0.005)
  run (["congestiontest", "--size", "medium"])
  sleep (0.015)
  run (["congestiontest", "--size", "medium"])
  sleep (0.020)
  run (["congestiontest", "--size", "medium"])
  sleep (0.025)
  run (["congestiontest", "--size", "small"])

  sleep (5)
  call (["logger/graph.py", "logger/log_window", "logger/log_tput"])

def q5_2 ():
  call (["rm", "logger/log_window", "logger/log_tput"])
  call (["netsim", "--bandwidth", "100", "--latency", "15", "--drop", "0.001", "--limit", "500"])
  run (["congestiontest", "--size", "large"])
  sleep (0.005)
  run (["congestiontest", "--size", "medium"])
  sleep (0.015)
  run (["congestiontest", "--size", "medium"])
  sleep (0.020)
  run (["congestiontest", "--size", "medium"])
  sleep (0.025)
  run (["congestiontest", "--size", "small"])

  sleep (5)
  call (["logger/graph.py", "logger/log_window", "logger/log_tput"])

def q5_2 ():
  call (["rm", "logger/log_window", "logger/log_tput"])
  call (["netsim", "--bandwidth", "1000", "--latency", "100", "--drop", "0.00001", "--limit", "1000"])
  run (["congestiontest", "--size", "large"])
  sleep (0.005)
  run (["congestiontest", "--size", "medium"])
  sleep (0.015)
  run (["congestiontest", "--size", "medium"])
  sleep (0.020)
  run (["congestiontest", "--size", "medium"])
  sleep (0.025)
  run (["congestiontest", "--size", "small"])

  sleep (5)
  call (["logger/graph.py", "logger/log_window", "logger/log_tput"])

def main (num):
  
  #q1 ()
  #q2 ()
  #q3 ()
  q4 ()
  #q5_1 ()
  #q5_2 ()

if __name__ == '__main__':
  if (len (sys.argv) < 2):
    print ("usage: script number")
    exit (1)

  main (sys.argv[1])
