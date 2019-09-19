#Code from DBaldwin on GitHub
#URL: https://gist.github.com/dbaldwin/9185b702091148580fa836c1911f8735
#May need to modify, obviously, understand the code!!!!

#Need to test....

#I used this code from DBaldwin, Dronekit and other sources. Tried to learn from sources and write my own code based on previous code.

from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time

#Sets up argument parse
import argparse
parser = argparse.ArgumentParser(description = 'Commands drone to arm and takeoff.')
#Adds and argument connect, will be used in final version to connect to Pi
parser.add_argument('--connect', help = "Vehicle connection target string. If no connection string specified, SITL automatically started and utilized instead.")

#Checks if parser has worked and connected to a real vehicle
#If not, connects to sitl
args = parser.parse_args()
connection_string = args.connect
#declares sitl as none first 
sitl = None

if not connection_string:
	import dronekit_sitl
	sitl = dronekit_sitl.start_default()
	connection_string = sitl.connection_string()
	
print('Connecting to vehicle on this address: %s ' % connection_string)
vehicle = connect(connection_string, wait_ready = True)

#Function declaration for 'arm_and_takeoff'
#Checks the drone for arming and pre arming checks
#then arms the drone and takes off to the user specified altitude
def arm_and_takeoff(aTargetAltitude):
	#Prearm checks
	print "Drone pre-arm checks"
	#Error checks if autopilot is ready
	#If autopilot not ready, time.sleep
	while not vehicle.is_armable:
		print "Waiting for vehicle to initialize..."
		time.sleep(1)

	print "Arming motors"
	#Sets mode to GUIDED and arms vehicle	
	vehicle.mode = VehicleMode("GUIDED")
	vehicle.armed = True

	#Waits for vehicle to arm
	while not vehicle.armed:
		print "Waiting for arming..."
		time.sleep(1)


	print "Taking off!!"
	#calls reference to subclass ' vehicle '
	#calls function to take off based on user define altitude
	vehicle.simple_takeoff(aTargetAltitude)

	#Checks if vehicle has reach the specificed altitude
	while True: 
		print "Altitude: ", vehicle.location.global_relative_frame.alt
		#Goes to just below altitude and then breaks from the function
		if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95:
			print "Reached target altitude"
			break
		time.sleep(1)
#calls the arm_and_takeoff function previously defined in arm_and_takeoff.py

arm_and_takeoff(20)
	
print("Take off complete")

#Waits and hovers for 10 seconds
time.sleep(10)

#Prints that landing is starting and changes the mode to LAND
print("Landing Initiating")
vehicle.mode = VehicleMode("LAND")
	
#closes vehicle object
vehicle.close()
print 'Vehicle object closed'

#shut down sitl simulator
print 'Simulator shutting down'
sitl.stop()
print("Test Take off and Land Complete")
