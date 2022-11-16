from time import time

UNBOUNDED = -1

class Window:
  def __init__ (self, timeout=UNBOUNDED, max_size=UNBOUNDED):
    self.buf = {} # buffer/window 
    self.rto = {} # retransmission timeout
    self.max_size = max_size
    self.timeout = timeout

  def isFull (self):
    if self.max_size == UNBOUNDED:
      return False
    return len(self.buf) == self.max_size

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

  # return corresponding sequence numbers for segments that are expired
  def expiredSegments (self):
    curr_time = time ()
    expired_seq = []

    for seq_no in self.rto:
      if curr_time >= self.rto[seq_no]:
        expired_seq.append (seq_no)

    return expired_seq

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

  def print (self):
    string = ""
    for seq_no in self.buf:
      string += str (seq_no) + " "

    print (string)
