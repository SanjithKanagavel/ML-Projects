from __future__ import print_function
import shutil
import pickle
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
      self.emg_data_queue.append(list(emg_data))

  def get_emg_data(self):
    with self.lock:
      return self.emg_data_queue

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
    targetFile = open(parentDir+gesture_name+str(i)+".p", "wb")
    targetFile.truncate()
    results = [0,0,0,0,0,0,0,0]
    for j in range(1000):
        sys.stdout.flush()
        print("Recordings Data "+ str(j) +"for sample " + str(i+1)+"...")
        print(results)
        results = np.vstack([results, listener.get_emg_data()])
        time.sleep(0.01)
    pickle.dump( results, targetFile )

finally:
  hub.shutdown()
