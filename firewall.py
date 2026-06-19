import sys
import os
from scapy.all import sniff, IP, TCP, UDP

# Security Policy Rule Configurations
BLOCKED_IPS = ["192.168.1.50", "10.0.0.66", "185.220.101.1"]
BLOCKED_PORTS = [21, 23, 445] # FTP, Telnet, SMB

def packet_filter_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        
        # 1. Evaluate IP Rule Access Controls
        if src_ip in BLOCKED_IPS:
            print(f"[❌ DROP] FIREWALL ALERT: Blocked IP Connection Attempt from {src_ip}")
            return

        # 2. Evaluate Layer 4 Port Rule Controls
        if packet.haslayer(TCP):
            dst_port = packet[TCP].dport
            if dst_port in BLOCKED_PORTS:
                print(f"[❌ DROP] FIREWALL ALERT: Unauthorized TCP Port Access to Port {dst_port} by {src_ip}")
                return
            print(f"[✅ PASS] TCP Packet Allowed: {src_ip} -> {dst_ip}:{dst_port}")
                
        elif packet.haslayer(UDP):
            dst_port = packet[UDP].dport
            if dst_port in BLOCKED_PORTS:
                print(f"[❌ DROP] FIREWALL ALERT: Unauthorized UDP Port Access to Port {dst_port} by {src_ip}")
                return
            print(f"[✅ PASS] UDP Packet Allowed: {src_ip} -> {dst_ip}:{dst_port}")

if __name__ == "__main__":
    print("==========================================================")
    print("         HOST-BASED PERSONAL FIREWALL ENGINE            ")
    print("==========================================================")
    print(f"[🛡️] Active IP Blacklist Policies: {BLOCKED_IPS}")
    print(f"[🛡️] Active Port Inspection Policies: {BLOCKED_PORTS}")
    print("[*] Sniffing network interfaces for active traffic...\n")

    try:
        sniff(filter="ip", prn=packet_filter_callback, store=0)
    except PermissionError:
        print("[!] Privilege Error: Root/Administrator elevation required to run network hooks.")
        print("    Run your terminal as Administrator (Windows) or use 'sudo python firewall.py' (Linux/macOS).")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[-] Shield Down: Firewall monitoring stopped gracefully.")
        sys.exit(0)