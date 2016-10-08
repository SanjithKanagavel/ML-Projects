#
#Testing basics of myo connected and myo disconnected states
#

from time import sleep
from myo import init, Hub, DeviceListener

class Listener(DeviceListener):

	def on_pair(self, myo, timestamp, firmware_version):
		print("Hello, Myo!")
	
	def on_unpair(self, myo, timestamp):
		print("Goodbye, Myo !")

init('/Users/phil/Documents/sdk/myo.framework')
hub = Hub()
hub.run(1000,Listener())
try:
   while True:
	sleep(0.5)
except KeyboardInterrupt:
	print('\nQuit')
finally:
	hub.shutdown() 
