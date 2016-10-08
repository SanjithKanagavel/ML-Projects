import sys
import myo as libmyo
from time import clock
from collections import deque
from myo import Hub

class EmgRate(libmyo.DeviceListener):

  __slots__ = 'times last_time n'.split()

  def __init__(self, n):
    super(EmgRate, self).__init__()
    self.times = deque()
    self.last_time = None
    self.n = int(n)

  @property
  def rate(self):
    if not self.times:
      return 0.0
    else:
      return 1.0 / (sum(self.times) / float(self.n))

  def on_pair(self, myo, *args):
    print("on_pair")

  def on_connect(self, myo, *args):
    print("on_connect")

  def on_arm_sync(self, myo, *args):
    print("on_arm_sync")
    myo.set_stream_emg(libmyo.StreamEmg.enabled)

  def on_emg_data(self, myo, timestamp, emg):
    t = clock()
    if self.last_time is not None:
      self.times.append(t - self.last_time)
      if len(self.times) > self.n:
        self.times.popleft()
    self.last_time = t

def main():
  libmyo.init('/Users/phil/Documents/sdk/myo.framework')
  hub = libmyo.Hub()
  listener = EmgRate(50)
  try:
    while True:
      hub.run_once(100, listener)
    #  print("\r\033[KEMG Rate:", listener.rate, end='')
      sys.stdout.flush()
  finally:
    hub.stop(True)
    hub.shutdown()


if __name__ == '__main__':
  main()
