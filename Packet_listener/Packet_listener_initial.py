import scapy.all as scapy
from scapy.layers import http
# we are creating a packet listener fuct using scapy.sniff (iface=interface, Store= storing or not (True or False), prn=callback function)
def packet_listener(interface):
    scapy.sniff(iface=interface,store=False,prn=packet_analyser)#prn calling back the function

def packet_analyser(packet):
    packet.show()

packet_listener("wlan0")