import subprocess
import optparse
# using optparse library we are creating a user input statement

opt_object = optparse.OptionParser() # initializing
opt_object.add_option("-i","--interface",dest="interface",help="interface to change!") # dest=destination
opt_object.add_option("-m","--mac",dest="mac_address",help="New mac address")

# printing the user input values
print(opt_object.parse_args())

# handling tuples
(user_input,arguments) = opt_object.parse_args()

# Printing separating
print(user_input.interface)
print(user_input.mac_address)

# we can assign in this formate also but we are giving that as user input 
#interface = "wlan0"
#mac_address = "00:11:22:33:44:55"
user_interface= user_input.interface
user_mac_address = user_input.mac_address

subprocess.call(["sudo","ifconfig",user_interface,"down"])
subprocess.call(["sudo","ifconfig",user_interface,"hw","ether",user_mac_address])
subprocess.call(["sudo","ifconfig",user_interface,"up"])
