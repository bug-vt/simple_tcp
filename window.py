from time import time

UNBOUNDED = -1

class Window:
  def __init__ (self, timeout=UNBOUNDED, max_size=UNBOUNDED):
    self.buf = {} # buffer/window 
    self.rto = {} # retransmission timeout
    self.max_size = max_size
    self.timeout = timeout
    self.periodic_check = 0

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

  # return corresponding sequence numbers for segments that are expired
  def expiredSegments (self):
    curr_time = time ()
    expired_seq = []

    if curr_time >= self.periodic_check:
      for seq_no in self.rto:
        if curr_time >= self.rto[seq_no]:
          expired_seq.append (seq_no)

      self.periodic_check = curr_time + 1 

    return expired_seq

  # Remove all segments that have sequence number 
  # less than or equal to ack number from the window (cumulative ACKs).
  def remove (self, ack_no):
    delivered_seq_no = []
    delivered_data = []
    for seq_no in self.buf:
      if seq_no <= ack_no:
        delivered_seq_no.append (seq_no)

    for seq_no in delivered_seq_no:
      delivered_data.append (self.buf.pop (seq_no))
      self.rto.pop (seq_no)

    return delivered_data 
