#!/usr/bin/env python3

import matplotlib.pyplot as plt
import sys

def windowGraph (file_name):
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

  plt.clf () 
  for i in range (len (x)):
    plt.plot (x[i], y[i], label = ("Sender %d" % i))
    plt.title ("Window size vs Time")
    plt.xlabel ("Time (second)")
    plt.ylabel ("Window size (segment)")
    plt.legend (loc="upper right")
    plt.savefig ("output_window_size.png")

  f.close ()

def tputGraph (file_name):
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

    if "----begin----" in raw[0]:
      x.append ([])
      y.append ([])
      i += 1
      first = True
      continue

    raw_time = raw[0]
    written_bytes = float (raw[1])
    
    time = raw_time.split (":") 
    time = float (time[0]) * 3600 + float (time[1]) * 60 + float (time[2])
    if first:
      offset = time
      first = False

    time = time - offset
    if time > 0:
      x[i].append (time)
      y[i].append ((written_bytes / 1024) / time)

  plt.clf () 
  for i in range (len (x)):
    plt.plot (x[i], y[i])
    plt.plot (x[i], y[i], label = ("Receiver %d" % i))
    plt.title ("Throughput per flow vs Time")
    plt.xlabel ("Time (second)")
    plt.ylabel ("Throughput (KB)")
    plt.legend (loc="upper left")
    plt.savefig ("output_tput.png")

  f.close ()


def main (argv):
  if len (argv) != 3:
    print ("Usage: graph <window_log> <tput_log>")
    exit (0)

  windowGraph (argv[1])
  tputGraph (argv[2])

if __name__ == '__main__':
  main (sys.argv)
