import scapy.all as scapy
import optparse
#Arp request
#Broadcast
#Response

def user_input():
    object = optparse.OptionParser() # Create an OptionParser object to handle command line options
    object.add_option("-i", "--ip", dest="ip_address", help="Enter the IP address range to scan") # Add an option for the user to specify the IP address range
    (options, arguments) = object.parse_args() # Parse the command line arguments

    if not options.ip_address: # Check if the user provided an IP address range
        print("[-] Please specify an IP address range using -i or --ip option")
    return options.ip_address # Return the specified IP address range

# Function to scan the network for active devices
# It takes an IP address range as input and sends ARP requests to discover devices
# The function prints a summary of the devices that responded to the ARP requests

def scan_network(ip_address):
    Arp_request = scapy.ARP(pdst=ip_address) # Create an ARP request for the specified IP range
    Broad_cast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # Create an Ethernet frame for broadcasting
    combined_packet = Broad_cast/Arp_request # Combine the Ether and ARP request
    (answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1) # Send the packet and receive answered and unanswered lists

    #print(list(answered_list)) # Print the list of answered packets (it will not show the devices that responded)

    answered_list.summary() # Print a summary of the answered packets

user_ip_address = user_input() # Get the user input for the IP address range
scan_network(user_ip_address) # Call the function to scan the network with the specified IP address range