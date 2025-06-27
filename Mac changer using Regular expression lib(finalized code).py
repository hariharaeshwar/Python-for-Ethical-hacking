import subprocess
import optparse
import re # regular expression
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
#using re module we can specifically check the mac address 
def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    #instead of printing ifconfig
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig)) # for \w\w means mac address can be an alphabetic also (example : 00:1a:22:33:44:55)
    
    #using if statement we are checking whether the mac address is same or not
    if new_mac:
        return new_mac.group(0) #checking the new_mac of index(0)
        #actually we are returning this for return something we have to assign a variable to print    
    else:
        return None
# calling the fuction
Finalized_mac = control_new_mac(str(user_input.interface)) # we are assign a variable to print

if Finalized_mac == user_input.mac_address:
    print("Success!!")
else:
    print("Try Again Error!!")
