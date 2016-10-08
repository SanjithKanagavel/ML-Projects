#
# Different pose testing
#
import myo as libmyo; libmyo.init('/Users/phil/Documents/sdk/myo.framework')
from time import sleep
from myo import  Hub, DeviceListener


class Listener(libmyo.DeviceListener):

	def on_pair(self, myo, timestamp, firmware_version):
		print("Hello, Myo!")
		myo.request_battery_level()

	def on_unpair(self, myo, timestamp):
		print("Goodbye, Myo !")

	def on_battery_level_received(self, myo, timestamp, level):
		print("Battery Level %s/100" % level)

	def on_pose(self, myo, timestamp, pose):
		if pose == libmyo.Pose.double_tap:
			print("Double tap")
		elif pose == libmyo.Pose.fingers_spread:
			print("Fingers Spread")
		elif pose == libmyo.Pose.fist:
			print("Fist")
		elif pose == libmyo.Pose.wave_in:
			print("Wave in")
		elif pose == libmyo.Pose.wave_out:
			print("Wave Out")



hub = libmyo.Hub()
hub.run(1000,Listener())
try:
   while True:
	sleep(0.5)
except KeyboardInterrupt:
	print('\nQuit')
finally:
	hub.shutdown()
