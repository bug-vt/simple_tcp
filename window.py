import datetime
from time import time

UNBOUNDED = -1
UNUSED = -1

class Window:
  def __init__ (self, segment_size=UNUSED, timeout=UNBOUNDED, max_size=UNBOUNDED):
    self.buf = {} # buffer/window 
    self.rto = {} # retransmission timeout
    self.max_size = max_size
    self.timeout = timeout
    self.slow_start = True
    self.segment_size = segment_size
    self.log = "----start----\n"
    self.log += datetime.datetime.now().strftime("%H:%M:%S.%f") + " 1\n"

  def isFull (self):
    if self.max_size == UNBOUNDED:
      return False
    return len(self.buf) >= self.max_size

  def isEmpty (self):
    return len(self.buf) == 0

  def get (self, seq_no):
    return self.buf.get (seq_no)
  
  # Add segment to the buffer
  def add (self, seq_no, segment):
    self.buf[seq_no] = segment
    self.rto[seq_no] = time () + self.timeout

  def resetRTO (self, seq_no):
    self.rto[seq_no] = time () + self.timeout

  # return first expired segment 
  def expiredSegment (self):
    curr_time = time ()
    for seq_no in sorted (self.rto):
      if curr_time > self.rto[seq_no]:
        return seq_no

    return None 

  # Remove all segments that have sequence number 
  # less than or equal to ack number from the window (cumulative ACKs).
  def remove (self, ack_num):
    delivered_seq_no = []
    delivered_data = []
    for seq_no in self.buf:
      if seq_no <= ack_num:
        delivered_seq_no.append (seq_no)

    for seq_no in delivered_seq_no:
      delivered_data.append (self.buf.pop (seq_no))
      self.rto.pop (seq_no)

    return delivered_data 

  def growWindow (self):
    if self.slow_start:
      self.max_size *= 2
    else:
      self.max_size += 1

    self.log += datetime.datetime.now().strftime("%H:%M:%S.%f") + " " + str(self.max_size) + "\n"

  def shrinkWindow (self):
    self.max_size //= 2
    if self.max_size == 0:
      self.max_size = 1
    self.slow_start = False
    self.log += datetime.datetime.now().strftime("%H:%M:%S.%f") + " " + str(self.max_size) + "\n"

  def print (self):
    string = ""
    for seq_no in self.buf:
      string += str (seq_no) + " "

    print (string)

  def writeLog (self, log_file):
    f = open (log_file, "a")
    f.write (self.log)
    f.write ("\n")
    f.close ()

