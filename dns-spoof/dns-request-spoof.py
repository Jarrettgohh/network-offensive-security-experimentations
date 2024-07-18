#!/usr/bin/python3

from scapy.all import *


ip=IP()
ip.src='192.168.1.22'
ip.dst='192.168.1.77'


udp=UDP(dport=53)
dns=DNS()

#print(ip.display())
#print(udp.display())
#print(dns.display())


send(ip/udp/dns)


