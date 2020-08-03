# !/usr/bin/env python

from scapy.all import *

pcap = rdpcap("ping-pong.pcapng")

packets = pcap[UDP]

for p in packets:
	if (p[IP].src == "127.0.0.1" and p[IP].dst == "127.0.0.1" ):
		try:
			# print str(hex(p[UDP].chksum))[2:].decode('hex')
			print(p[Raw].load.decode('utf-8'))
		except:
			continue