#!/bin/bash

sudo iptables -A FORWARD -p udp --dport 53 -j DROP


