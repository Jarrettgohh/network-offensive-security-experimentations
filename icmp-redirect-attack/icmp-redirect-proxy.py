#!/bin/bash/python3

import socket
import scapy

HOST = "127.0.0.1"  
PORT = 8000  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()

    with conn:
        print(f"Connected by {addr}")

        while True:
            data = conn.recv(1024)

            if not data:
                break

            #
            # received data
            #

            print(data)


            
            #conn.sendall(data)
