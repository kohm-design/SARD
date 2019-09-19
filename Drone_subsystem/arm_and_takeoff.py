#Should not need to import stuff since will always be called in another file

#Defines Function 'arm_and_takeoff' that takes user specified 
#target altitude and prints stuff to arm and cause the drone to takeoff

#This is done using the vehicle.armed and vehicle.simple_takeoff commands

def arm_and_takeoff(aTargetAltitude):
	from dronekit import connect, VehicleMode, LocationGlobalRelative
	from pymavlink import mavutil
	import time

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
	vehicle.simple_takeoff(aTargetAltitude)

	#Checks if vehicle has reach the specificed altitude
	while True: 
		print "Altitude: ", vehicle.location.global_relative_frame.alt
		#Goes to just below altitude and then breaks from the function
		if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95:
			print "Reached target altitude"
			break
		time.sleep(1)
