
from __future__ import print_function
import collections
import myo
import threading
from sys import argv
from threading import Thread
import time

class MyListener(myo.DeviceListener):
  def __init__(self, queue_size=8):
    self.lock = threading.Lock()
    self.emg_data_queue = collections.deque(maxlen=queue_size)

  def on_connect(self, device, timestamp, firmware_version):
    device.set_stream_emg(myo.StreamEmg.enabled)

  def on_emg_data(self, device, timestamp, emg_data):
    with self.lock:
      self.emg_data_queue.append((timestamp, emg_data))

  def get_emg_data(self):
    with self.lock:
      return list(self.emg_data_queue)

def loopFun(i,listener,target):
    print("Starting %d sample in 5 seconds" % i)
    for j in range(100):
        target.write(str(listener.get_emg_data()))
        target.write("\n\n")
    print("finished %d sampling" % i)

myo.init()
hub = myo.Hub()

# data.txt - Hand open
# data1.txt - Fist close
# data2.txt - Single Finger
# data3.txt - Two Finger
# data4.txt - Three Finger

try:
  target = open("t4_data4.txt", "w")
  target.truncate()
  listener = MyListener()
  hub.run(200, listener)
  time.sleep(3)
  
  for i in range(10): #Take 10 samples
    print("---Sample %d START---" % i)
    time.sleep(5)
    target.write("\n---Sample %d START---\n" % i)
    for j in range(100):
        target.write(str(listener.get_emg_data()))
        target.write("\n\n")
    target.write("\n---Sample %d END---\n" % i)
    print("---Sample %d END---" % i)

finally:
  hub.shutdown()
