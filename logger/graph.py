#!/usr/bin/env python3

import matplotlib.pyplot as plt
import sys

def main (file_name):
  f = open (file_name, "r")
  lines = f.readlines ()

  first = False
  offset = 0
  i = -1
  x = []
  y = []
  for line in lines:
    raw = line.split ()
    if len (raw) == 0:
      continue

    if "----start----" in raw[0]:
      x.append ([])
      y.append ([])
      i += 1
      first = True
      continue

    raw_time = raw[0]
    window_size = int (raw[1])
    
    time = raw_time.split (":") 
    time = float (time[0]) * 3600 + float (time[1]) * 60 + float (time[2])
    if first:
      offset = time
      first = False

    x[i].append (time - offset)
    y[i].append (window_size)

  
  for i in range (len (x)):
    plt.plot (x[i], y[i])
    plt.savefig ("output_window_size.png")



if __name__ == '__main__':
  main (sys.argv[1])
