from __future__ import print_function
import shutil
import collections
import sys
import myo
import threading
import numpy as np
import time
import os.path
from sys import argv
from threading import Thread

class MyoListener(myo.DeviceListener):
  def __init__(self, queue_size=8):
    self.lock = threading.Lock()
    self.emg_data_queue = collections.deque(maxlen=queue_size)

  def on_connect(self, device, timestamp, firmware_version):
    device.set_stream_emg(myo.StreamEmg.enabled)

  def on_emg_data(self, device, timestamp, emg_data):
    with self.lock:
      self.emg_data_queue.append(emg_data)

  def get_emg_data(self):
    with self.lock:
      return np.array(self.emg_data_queue).flatten()

def loopFun(i,listener,target):
    print("Starting %d sample in 5 seconds" % i)
    for j in range(100):
        target.write(str(listener.get_emg_data()))
        target.write("\n\n")
    print("finished %d sampling" % i)

myo.init()
hub = myo.Hub()

try:

  listener = MyoListener()
  hub.run(200, listener)
  print("Myo Listener started")
  parentDir = "recordedData/"
  gesture_name = input("Enter gesture name :")
  no_samples = int(input("Number of samples to be taken :"))
  parentDir = parentDir + gesture_name + "/"
  print("Recordings will be stored in :" + parentDir)

  if not os.path.exists(parentDir):
      os.makedirs(parentDir)
  else:
      shutil.rmtree(parentDir)
      os.makedirs(parentDir)

  for i in range(no_samples):
    targetFile = open(parentDir+gesture_name+str(i)+".txt", "w+")
    targetFile.truncate()
    for j in range(1000):
        sys.stdout.flush()
        print("Recordings Data "+ str(j) +"for sample " + str(i+1)+"...")
        targetFile.write(str(listener.get_emg_data()))
        time.sleep(0.01)
        targetFile.write("\n")

finally:
  hub.shutdown()
