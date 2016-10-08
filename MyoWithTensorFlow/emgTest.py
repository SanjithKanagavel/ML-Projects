import sys
import myo as libmyo; libmyo.init('/Users/phil/Documents/sdk/myo.framework')
from time import clock
from collections import deque


class EmgRate(libmyo.DeviceListener):

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
    print(emg)

def main():
  hub = libmyo.Hub()
  listener = EmgRate()
  try:
    while True:
      hub.run_once(100, listener)
      #print("EMG Rate: %s", listener.rate)
      sys.stdout.flush()

  except KeyboardInterrupt:
	print('\nQuit')

  finally:
    hub.stop(True)
    hub.shutdown()


if __name__ == '__main__':
  main()
