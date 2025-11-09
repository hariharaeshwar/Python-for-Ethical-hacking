import scapy.all as scapy
from scapy.layers import http

def packet_listener(interface):
    scapy.sniff(iface=interface,store=False,prn=packet_analyser)#prn calling back the function
# This script listens for HTTP packets on a specified network interface and prints the raw data of the packets.
def packet_analyser(packet):
    if packet.haslayer(http.HTTPRequest): # checking if the packet has HTTP Request layer
        if packet.haslayer(scapy.Raw): # checking if the packet has Raw layer
            print(packet[scapy.Raw].load)# printing the raw data of the packet

packet_listener("wlan0")