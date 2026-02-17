# Networking Notes --- Day 3 (Complete)

------------------------------------------------------------------------

## Quick Revision From Previous Days

Routing decides where packet goes.\
ARP decides who receives it locally.

------------------------------------------------------------------------

# 1. DNS (Domain Name System)

Purpose: Converts domain names into IP addresses.

Flow: Browser → OS → DNS cache → DNS server → IP returned → cached
locally

Commands: cat /etc/resolv.conf nslookup google.com dig google.com
resolvectl statistics

Facts: - DNS must happen before connection - Can resolve from cache or
remote server - Uses UDP usually

------------------------------------------------------------------------

# 2. Ports

IP = device\
Port = application

Common: HTTP 80\
HTTPS 443\
SSH 22\
MySQL 3306

Commands: ss -tuln lsof -i :3000

------------------------------------------------------------------------

# 3. TCP vs UDP vs ICMP

TCP → reliable + ordered\
UDP → fast + no guarantee\
ICMP → control protocol (ping)

ICMP has no ports.

------------------------------------------------------------------------

# 4. Why Ping Works Without Ports

ICMP uses identifier + sequence number.\
Kernel tracks request and reply mapping.

------------------------------------------------------------------------

# 5. TLS vs HTTPS vs VPN

TLS = encryption protocol\
HTTPS = HTTP + TLS\
VPN = encrypts whole device traffic

------------------------------------------------------------------------

# 6. HTTPS Session Steps

1 DNS 2 TCP handshake 3 TLS handshake 4 certificate 5 verification 6
keys 7 encrypted communication

------------------------------------------------------------------------

# 7. Private vs Public IP

Private ranges: 10.0.0.0 -- 10.255.255.255\
172.16.0.0 -- 172.31.255.255\
192.168.0.0 -- 192.168.255.255

Public IP = global unique address.

------------------------------------------------------------------------

# 8. ISP

Provides connection + public IP + routing.

Path: Device → Router → ISP → Internet

------------------------------------------------------------------------

# 9. Virtual Network

Software‑created network inside machine.

Structure: Internet → Router → Laptop → Virtual layer → Terminal

ARP broadcast stays inside virtual network.

------------------------------------------------------------------------

# 10. eth0 Instead of wlan0 Means

Likely inside: WSL / Docker / VM / container

------------------------------------------------------------------------

# 11. Diagnostic Commands

ip link\
ip route\
ps aux \| grep vpn

------------------------------------------------------------------------

# 12. CIDR + Subnet Math

Example: 172.21.41.45/20\
Mask = 255.255.240.0

Block size: 256 − 240 = 16

Range example: 32--47

Gateway + IP in same range → same subnet.

------------------------------------------------------------------------

# 13. Terminology

Network = whole system\
Subnet = division\
Host = device

------------------------------------------------------------------------

# 14. ARP Scope

ARP broadcasts only inside subnet.

Never goes to internet or ISP.

------------------------------------------------------------------------

# 15. Subnet Size Reality

Capacity ≠ actual devices.

------------------------------------------------------------------------

# 16. Core Mental Model

DNS → Routing → ARP → Port → Protocol

------------------------------------------------------------------------

# 17. All Questions Covered

-   ARP cache behavior
-   ping vs browser difference
-   ICMP no ports
-   kernel reply routing
-   TLS vs VPN
-   enterprise network meaning
-   virtual network concept
-   eth0 reason
-   VPN detection
-   CIDR math
-   subnet validation
-   gateway logic
-   ISP vs router
-   private IP meaning
-   ARP broadcast limits
-   WiFi + virtual network coexistence

------------------------------------------------------------------------

# 18. Correct Packet Order

ping google.com →

1 DNS\
2 Routing\
3 ARP\
4 Send

------------------------------------------------------------------------

# End
