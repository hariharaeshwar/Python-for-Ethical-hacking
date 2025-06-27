import subprocess
#Initially we running the commmand in terminal by using subprocess library
#Changing Mac address(like in terminal)

subprocess.call(["sudo","ifconfig","wlan0","down"])
subprocess.call(["sudo","ifconfig","wlan0","hw","ether","00:11:22:33:22:44"])
subprocess.call(["sudo","ifconfig","wlan0","up"])

print("Your mac address is changed")