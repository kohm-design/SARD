from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time
##

#Starting simulator
print "Start simulator (SITL)"
import dronekit_sitl
sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()
#Prints Connections String
print("Connection to vehicle on: %s" % (connection_string))

vehicle = connect(connection_string, wait_ready=True)

import argparse #what is argparse??
parser = argparse.ArgumentParser()
#adds argument connect to connect the ip address
parser.add_argument('--connect', default = 'tcp:127.0.0.1:5760') 
#change ip address to the Pi's
#127.0.0.1.14500 is a simulate vehicle's ip address
args = parser.parse_args()


#Connect to the Drone Vehicle
#Prints parsed connection argument
print 'Connecting to drone on : %s' % args.connect
#Checks Baud Rate and wait_ready to see if it can connect
#Defines subclass vehicle
vehicle = connect(args.connect, baud = 57600, wait_ready = True)



#Defines Function 'arm_and_takeoff' that takes userspecified 
#target altitude and prints stuff to arm and cause the drone to takeoff
#def arm_and_takeoff(aTargetAltitude):
	
##Commented out function call
#Prearm checks
print "Drone pre-arm checks"
#Error checks if autopilot is ready
#If autopilot not ready, time.sleep
while not vehicle.is_armable:
	print "Waiting for vehicle to initialise..."
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
vehicle.simple_takeoff(20)

#Checks if vehicle has reach the specificed altitude
while True: 
	print "Altitude: ", vehicle.location.global_relative_frame.alt
	#Goes to just below altitude and then breaks from the function
	if vehicle.location.global_relative_frame.alt>=20*0.95:
		print "Reached target altitude"
		break
	time.sleep(1)




#calls the arm_and_takeoff function previously defined
#arm_and_takeoff(20)
	
print("Take off complete")

#Waits and hovers for 10 seconds
time.sleep(10)

#Prints that landing is starting and changes the mode to LAND
print("Landing Initiating")
vehicle.mode = VehicleMode("LAND")
	
#Lastly, closes vehicle subclass reference
vehicle.close()

#shut down sitl simulator
sitl.stop()
print("Test Take off and Land Complete")
