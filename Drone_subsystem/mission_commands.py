# Mission Protocol Code
# *Insert Description Here*

from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time

# Connect to Vehicle
#Starting simulator
print "Start simulator (SITL)"
import dronekit_sitl
sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()
#Prints Connections String
print("Connection to vehicle on: %s" % (connection_string))

vehicle = connect(connection_string, wait_ready=True)


# First downloads current mission

# Downloads vehicle waypoints (called commands in code)
# Then waits until download is complete
cmds = vehicle.commands
cmds.download()
cmds.wait_ready()

# Useful commands
# clear vehicle.commands and uploads commands to the vehicle
# cmds.clear()
# cmds.upload()

# creating and adding commands to the mission
# commands added to mission using ' add() '
# commands are sent to the vehicle using ' upload() '


# UNDERSTAND THIS AND WILL PROBS CHANGE FOR SURE
# dronekit.Command( target_system, target_component, seq, fram, command, current, autocontinue, param1, param2, param3, param4, x, y, z)

# target_system - set to any ID (DroneKit changes the value to the MAVLink ID of the connected vehicle before the commands is sent)
# target_component - component id message is intended for (0 is broadcast in most cases)
# seq  - sequence number within the mission (should be set to 0)
# frame - frame of reference used for location parameters
#		  most case frame will be mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT
# command - specific mission command to preform, see DroneKit documentation for command list if needed.
# current and autocontinue - just need to set to zero
# param1, param2, param3, param4 - command specific parameters
# x, y, z - command specific used for latitude(x), longtitude(y), altitude(z)

cmd1 = command( 0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, 0, 10)
cmd2 = Command( 0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, 10, 10, 10)
# cmd3 = ....
# add commands as needed, run with existing commands before add more.

cmds.add(cmd1)
print 'Added Waypoint 1'
cmds.add(cmd2)
print 'Added Waypoint 2'

cmds.upload()
print 'Commands Uploaded'
