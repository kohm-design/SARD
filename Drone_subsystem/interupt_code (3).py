# Interrupt Code when get image positive

# If image positive value is true, then modify mission

#dronekit python code for simple goto
#goes to specified GPS coordinates and altitude

import time
from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil

import argparse
parser = argparse.ArgumentParser(description = 'Commands drone using vehicle.simple_goto.')
parser.add_argument('--connect', help = "Vehicle connection target string. If no connection string specified by user, then SITL automatically started and utilized instead.")

args = parser.parse_args()
connection_string = args.connect
#declares sitl as none first 
sitl = None

#Checks if parser has worked and connected to a real vehicle
#If not, connects to sitl

if not connection_string:
	import dronekit_sitl
	sitl = dronekit_sitl.start_default()
	connection_string = sitl.connection_string()
	
print('Connecting to vehicle on this address: %s ' % connection_string)
vehicle = connect(connection_string, wait_ready = True)

image_hit = 0

#Defines Function 'arm_and_takeoff' that takes user specified 
#target altitude and prints stuff to arm and cause the drone to takeoff

#This is done using the vehicle.armed and vehicle.simple_takeoff commands

#Here I redefine the arm_and_takeoff function, should be able to declare in own file to call but keep getting a error where vehicle needs to be defined globally

def arm_and_takeoff(aTargetAltitude):
	from dronekit import connect, VehicleMode, LocationGlobalRelative
	from pymavlink import mavutil
	import time

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

#Calls arm_and_takeoff
arm_and_takeoff(20)

vehicle.airspeed = 3
print("Setting default/target arispeed to: %s" % vehicle.airspeed)

print("Moving towards first point...")
pt1 = LocationGlobalRelative(-35.361354, 149.165218, 20)
vehicle.simple_goto(pt1)

#for loop to move towards point 1 for 30 seconds
#prints global gps location as it moves

#alter to move until it reaches that coordinate!!!!
n = 0
for n in range(0,5):
	print("Vehicle Global Location %s" % vehicle.location.global_frame)
	time.sleep(6)

print("Moving towards second point at ground speed of 10 m/s...")
pt2 = LocationGlobalRelative(-35.363244, 149.168801, 20)
vehicle.simple_goto(pt2, groundspeed = 10)

n = 0
for n in range(0,5):
	print("Vehicle Global Location %s" % vehicle.location.global_frame)
	time.sleep(6)

#same for point 2

while not image_hit:
	print("Waiting for postivie image of human.....")
	time.sleep(15)
	#eventually will put if statement based on data from the FliR
	image_hit = 1

print('HUMAN DETECT BEEP BOOP')


print("Returing to Lauch (RTL)")
vehicle.mode = VehicleMode("RTL")

#add part to wait till vehicle at launch point

#closes vehicle object
vehicle.close()
print("Vehicle obeject closed")

#shuts down simulator if running
if sitl:
	sitl.stop()

