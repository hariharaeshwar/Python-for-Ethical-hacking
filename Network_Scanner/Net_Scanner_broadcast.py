import scapy.all as scapy

#Arp request
#Broadcast
#Response

Arp_request = scapy.ARP(pdst="192.168.31.1/24") # Create an ARP request for the specified IP range
Broad_cast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # Create an Ethernet frame for broadcasting
combined_packet = Broad_cast/Arp_request # Combine the Ether and ARP request
(answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1) # Send the packet and receive answered and unanswered lists

#print(list(answered_list)) # Print the list of answered packets

answered_list.summary() # Print a summary of the answered packets
