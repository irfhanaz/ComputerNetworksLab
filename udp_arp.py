from getmac import get_mac_address
import os
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("IP Address:", ip_address)
cmd = "ping " + ip_address
print(os.system(cmd))
print("\nHardware Address is: " + ip_address + ":")
print("The MAC address is: " + get_mac_address(ip=ip_address) + ":")