import dronekit
from dronekit import connect
import socket
import exceptions

#This functions performs error checks based on the input address of the vehicle

#Copy Paste to reuse in other files/modules
##
#Error handling
#from connection_check.py import connection_check
#connection_check(connection_string)



def connection_check(ipAddress):

	try:
		dronekit.connect(ipAddress, heartbeat_timeout=15)

	except socket.error:
		print 'No server exists'

	except exceptions.OSError as e:
		print 'No serial exists'

	except dronekit.APIException:
		print 'Timeout, no heartbeat in the last 15 seconds'

	except:
		print 'Some error occured'

#Example code to test if function working
#print "Start simulator (SITL)"
#import dronekit_sitl
#sitl = dronekit_sitl.start_default()
#connection_string = sitl.connection_string()
##Prints Connections String
#print("Connection to vehicle on: %s" % (connection_string))

#vehicle = connect(connection_string, wait_ready=True)

#calls function
#connection_check(connection_string)

