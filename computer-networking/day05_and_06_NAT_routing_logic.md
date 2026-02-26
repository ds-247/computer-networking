# Networking Learning Notes — Day 5 & Day 6

---

# DAY 5 — ROUTING FUNDAMENTALS

## What is Routing?
Routing is the process of selecting a path for network traffic from source → destination across multiple networks.

Routers use **routing tables** to decide where to forward packets.

---

## Routing Algorithms

Routing algorithms decide **best path** based on metrics.

### Types

#### 1. Distance Vector
- Chooses path based on distance
- Router only knows neighbors
- Example logic: "Shortest hop count wins"

#### 2. Link State
- Builds full network topology map
- Calculates shortest path using algorithm like Dijkstra
- More accurate + faster convergence

#### 3. Path Vector
- Used on Internet scale
- Tracks full path (not just distance)
- Prevents loops

---

## Metrics Used in Routing Decisions

Routers don’t just pick shortest path randomly. They compare metrics:

Common metrics:
- Hop count
- Delay (latency)
- Bandwidth
- Reliability
- Load
- Cost

Lower metric = better path

---

## Route Selection Priority Order

When multiple routes exist:


Longest Prefix Match

Lowest Metric

Administrative Distance


---

### Longest Prefix Match Example

Routes:


192.168.0.0/16
192.168.1.0/24


Destination IP:

192.168.1.25


Router selects:


192.168.1.0/24


Reason: More specific match.

---

## Administrative Distance (AD)

Used when routes come from different routing protocols.

Lower AD = more trusted source.

Example:

| Source | AD |
|------|----|
Connected | 0 |
Static | 1 |
OSPF | 110 |
RIP | 120 |

---

## Traceroute Concept

Traceroute shows **path packets take** across routers.

Command:

Windows:

tracert 1.1.1.1


Linux/macOS:

traceroute 1.1.1.1


Shows:
- Each router hop
- Delay per hop
- Route path

---

## Hop

A **hop** = one router jump.

Example:
PC → Router → ISP → Backbone → Server  
= 4 hops

---

## Autonomous System (AS)

An AS is a network controlled by one organization.

Examples:
- ISP network
- Company network
- Cloud provider network

Each AS has unique **ASN number**.

---

## Interior vs Exterior Routing

### Interior Gateway Protocols (Inside one network)
Used within organization

Examples:
- OSPF
- RIP
- EIGRP

---

### Exterior Gateway Protocol (Between networks)

Used between different organizations.

Example:
- BGP

---

## Why Internet Uses BGP

Internet is made of thousands of networks.

Needs:
- Policy control
- Scalability
- Loop prevention

BGP provides:
- Path tracking
- AS path
- Policy routing

---

## BGP AS-PATH

BGP stores full list of AS networks a route passed through.

Purpose:
- Prevent loops
- Select best path

If router sees its own AS in path → rejects route.

---

---

# DAY 6 — PACKET FORWARDING + ARP + NAT

---

## Packet Forwarding Process

When sending packet to destination:


Step 1 → Check routing table
Step 2 → Find next hop IP
Step 3 → Find MAC of next hop
Step 4 → Send frame


---

## Important Concept: ARP Scope

ARP works **only inside local network (LAN)**.

ARP cannot cross routers.

---

### Then how router sends packets outside LAN?

It does:


ARP → only for NEXT HOP
NOT for final destination


Example:

Destination = Google server

Router does:
- Find ISP router IP
- ARP for ISP router MAC
- Send packet to ISP

---

## Key Rule

ARP is used for:

MAC of next hop


NOT:

MAC of final destination


---

## NAT (Network Address Translation)

Home routers use NAT.

Purpose:
- Allow many devices to share one public IP

---

### NAT Translation Example

Private network:


Laptop → 192.168.1.10
Phone → 192.168.1.20


Router public IP:

49.x.x.x


Router translates:


192.168.1.10 → 49.x.x.x


Internet only sees public IP.

---

## Types of NAT

| Type | Description |
|-----|-------------|
Static NAT | One private ↔ one public |
Dynamic NAT | Pool of public IPs |
PAT | Many devices share one public IP |

Home routers use:

PAT


---

## Home Router Role

Your home router performs:

- Routing
- NAT
- Firewall
- DHCP
- Wireless Access Point
- Switching

It is actually multiple devices combined.

---

## Real Packet Flow (Home Network → Internet)


Laptop → Router → ISP Router → Internet → Server


Router actions:
1. Replace source IP (NAT)
2. Recalculate checksum
3. Forward packet

---

## Why Router Recalculates Checksum?

Because it modified packet header (IP address change).

---

## Commands Practiced

### View Routing Table

route print


---

### See ARP Table

arp -a


---

### Trace Route

tracert 1.1.1.1


---

### Ping Device

ping <ip>


---

---

# QUESTIONS COVERED (SELF-CHECK)

---

### Concept Questions

1. Why doesn’t OSPF run on Internet?
2. Why does BGP track AS path?
3. What is a hop?
4. Why is longest prefix preferred?
5. Why ARP doesn’t work outside LAN?
6. How router finds MAC for internet packet?
7. Why NAT required?
8. Why router recalculates checksum?

---

### Scenario Questions

1. Two routes exist — which one router picks?
2. Traceroute shows fewer hops — what does it mean?
3. If ARP fails, can packet be sent?
4. Why local devices visible but internet ones not in ARP table?

---

---

# MENTAL MODEL SUMMARY

When sending packet:


Destination local?
YES → ARP destination → send
NO → ARP router → send


Router then repeats same logic.

---

---

# CURRENT SKILL LEVEL ACHIEVED

You now understand:

✔ Local network communication  
✔ Routing logic  
✔ Path selection  
✔ Metrics  
✔ BGP basics  
✔ ARP role  
✔ NAT role  
✔ Packet forwarding process  

This is already beyond beginner networking knowledge.

---

END OF DAY 5 & 6 NOTES