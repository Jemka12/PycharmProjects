#!/usr/bin/env python
import netfilterqueue
import subprocess


def process_packet(packet):
    print(packet)
    packet.accept()


try:
    subprocess.call("iptables -I OUTPUT -j NFQUEUE --queue-num 0", shell=True)
    subprocess.call("iptables -I INPUT -j NFQUEUE --queue-num 0", shell=True)
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()
except KeyboardInterrupt:
    subprocess.call("iptables --flush", shell=True)