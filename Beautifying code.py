import subprocess
import optparse
# creating a function 
def get_user_input():
    opt_object = optparse.OptionParser() # initializing
    opt_object.add_option("-i","--interface",dest="interface",help="interface to change!") # dest=destination
    opt_object.add_option("-m","--mac",dest="mac_address",help="New mac address")

# instead of printing we are returning
    return opt_object.parse_args()

# creating another fuction
def mac_changer(user_interface,user_mac_address):
    subprocess.call(["sudo","ifconfig",user_interface,"down"])
    subprocess.call(["sudo","ifconfig",user_interface,"hw","ether",user_mac_address])
    subprocess.call(["sudo","ifconfig",user_interface,"up"])

print("My Mac changer started!!")
# Calling that function , Handling tuples 
(user_input,arguments) = get_user_input()
# Calling another function with an arguments(values)
mac_changer(user_input.interface,user_input.mac_address)

print(f"Mac address is changed to {user_input.mac_address}")

#you can also specify the interface details using subprocess
#Creating another func to print the output interface details
def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    print(ifconfig)

# calling the fuction
control_new_mac(user_input.interface)