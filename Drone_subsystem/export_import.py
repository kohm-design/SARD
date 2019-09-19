#importing and exporting files for mission use

from dronekit import connect, Command
import time

import argparse parser = argparse.ArgumentParser(desription = 'Importing and eporting mission files using dronekit.')
parser.add_argument('--connect', help = "Vehicle connection target string. If no connection string specified by user, then SITL automatically started and utilized instead.")

args = parser.parse_args()

connection_string = args.connect
sitl = None

if not connection_string:
	import dronekit-sitl
	sitl = dronekit_sitl.start_default()
	connection_string = sitl.connection_string()


print('Connection to vehilce  on this address: %s' % connection_string)
vehicle = connect(connection_string, wait_ready = True)

while not vehicle.is_armable:
	print 'Waiting for vehilce to initialize...'
	time.sleep(1)


