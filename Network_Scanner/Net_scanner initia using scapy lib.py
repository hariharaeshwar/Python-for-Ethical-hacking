import scapy.all as scapy

#Arp request
#Broadcast
#Response

Arp_request = scapy.ARP(pdst="192.168.31.1/24") # Create an ARP request for the specified IP range
Broad_cast = scapy.Ether() #  Create an Ethernet frame for broadcasting
scapy.ls(scapy.ARP())
scapy.ls(scapy.Ether())
