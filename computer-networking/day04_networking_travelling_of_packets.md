# Complete Networking Learning Notes (Day 1--4)

------------------------------------------------------------------------

## Core Networking Flow

1.  Application creates data
2.  Routing table decides path
3.  ARP resolves MAC
4.  Frame sent
5.  Router forwards if remote

Golden Rule: Routing chooses path. ARP finds device.

------------------------------------------------------------------------

## Interfaces

Interface = network door of device

Types: - lo → loopback - eth0/wlan0 → physical - docker0 → virtual -
vEthernet → hypervisor

Command: ip addr

------------------------------------------------------------------------

## Loopback

127.0.0.1 = self communication\
Works without internet

------------------------------------------------------------------------

## Routing

Command: ip route

Default route = gateway used when destination unknown

------------------------------------------------------------------------

## ARP

Maps IP → MAC

Command: ip neigh

Steps: 1. Check ARP cache 2. If missing → broadcast 3. Target replies 4.
Cache stored

------------------------------------------------------------------------

## LAN vs Internet

Same subnet → direct send\
Different subnet → router

------------------------------------------------------------------------

## ARP Cache

Temporary memory of IP-MAC mappings.

Clear: ip neigh flush all

------------------------------------------------------------------------

## DNS → Routing → ARP Order

1.  Resolve domain to IP
2.  Choose route
3.  Resolve MAC

------------------------------------------------------------------------

## Ping

Uses ICMP\
Tests reachability only.

------------------------------------------------------------------------

## Traceroute

Shows path hop-by-hop using TTL.

TTL rule: Each router decreases TTL by 1.

------------------------------------------------------------------------

## Hops

Hop = router crossed.

------------------------------------------------------------------------

## Probes

Traceroute sends multiple packets per hop to measure latency.

------------------------------------------------------------------------

## Load Balancing Routers

Multiple routers at same hop = multiple possible paths.

------------------------------------------------------------------------

## NAT

One public IP shared by many devices.

Flow: Private IP → Router translates → Public IP → Internet

------------------------------------------------------------------------

## Public vs Private IP

Private ranges: 10.0.0.0/8\
172.16.0.0/12\
192.168.0.0/16

Public IP = internet-visible address.

------------------------------------------------------------------------

## Multicast

224.0.0.0 -- 239.255.255.255

Used for: - streaming - discovery - casting

------------------------------------------------------------------------

## Subnet Math

CIDR: /20

Formula: Hosts = 2\^(32-mask)

Example: /20 → 4096 addresses

------------------------------------------------------------------------

## Route Table Reading

Command: route print

Important entries: 0.0.0.0 → default route\
127.0.0.0 → loopback\
192.168.x.x → LAN\
172.x.x.x → virtual networks

------------------------------------------------------------------------

## Virtual Networks

Created by: - WSL - Docker - VM - Hypervisor

They create internal LANs inside your machine.

------------------------------------------------------------------------

## TCP vs ICMP

ICMP → ping\
TCP → web, apps

Ports belong to TCP/UDP, not ICMP.

------------------------------------------------------------------------

## TLS

Encryption layer securing communication.

HTTPS = HTTP + TLS

------------------------------------------------------------------------

## ISP

Internet Service Provider = company giving internet access.

Internet = global network of networks.

------------------------------------------------------------------------

## Checksum

Error detection value inside packet to verify integrity.

------------------------------------------------------------------------

## Practical Exercises

### Discover devices

Windows: for /L %i in (1,1,254) do @ping -n 1 192.168.29.%i \| find
"Reply"

Linux: for i in {1..254}; do ping -c1 192.168.1.\$i & done

------------------------------------------------------------------------

### Observe ARP

arp -a

------------------------------------------------------------------------

### Clear ARP + Relearn

arp -d \* ping targetIP arp -a

------------------------------------------------------------------------

### Run LAN Server

python -m http.server 8000 --bind 0.0.0.0

------------------------------------------------------------------------

### Check listening ports

netstat -ano \| find "8000"

------------------------------------------------------------------------

## Real Networking Observations Learned

✔ Ping success proves Layer 1--3 working\
✔ TTL reveals hop count\
✔ ARP proves local delivery\
✔ Multiple traceroute lines = multiple paths\
✔ Firewall can block service but not ping

------------------------------------------------------------------------

## Concept Check Questions

1.  Who replies to ARP?
2.  Why ARP not used across internet?
3.  Why TTL exists?
4.  Difference: route vs ARP?
5.  Why multiple IPs for same domain?
6.  Why ping works but website fails?
7.  What proves two devices are in same LAN?
8.  Why router needed for internet?
9.  What happens if default route deleted?
10. Why private IP exists?

------------------------------------------------------------------------

## Key Mental Model

Internet is not one network.

It is:

Network of Networks

Routers = intersections\
Packets = cars\
Routing table = GPS\
ARP = asking house number

------------------------------------------------------------------------

END OF NOTES
