#!/usr/bin/python3 

import socket
import sys
import struct

try:
    s = socket.socket(socket.AF_INET
                      , socket.SOCK_RAW
                      , socket.IPPROTO_TCP
                      )

except (socket.error, msg):
    print(msg)
    sys.exit()


try:

    while True:
        packet = s.recv(65565)
        print(packet)

except KeyboardInterrupt:
    sys.exit()




