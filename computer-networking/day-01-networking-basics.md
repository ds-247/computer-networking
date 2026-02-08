# Day 1 – Networking Basics: Your Machine as a Networked System

## Objective
Understand how a single machine participates in networking using:
- Interfaces
- IP addresses
- Routing rules

No theory-first approach. Everything observed via Linux commands.

---

## 1. Network Interface

A **network interface** is a communication endpoint (door) through which a machine sends or receives data.

### Examples:
- `lo` → loopback (internal)
- `wlan0 / wlp*` → Wi-Fi
- `eth0 / enp*` → Ethernet
- `docker0` → Docker virtual bridge
- `tun0` → VPN interface

> Data must exit via an interface. No interface = no communication.

---

## 2. Loopback Interface (`lo`)

- Used for **internal communication**
- IP range: `127.0.0.0/8`
- Common IP: `127.0.0.1`

### Key Properties:
- Traffic never leaves the machine
- No router involved
- Works even without internet or Wi-Fi

### Use cases:
- Backend ↔ Frontend on same machine
- Local databases
- Microservices communication

---

## 3. IP Address

An **IP address** is an identity assigned to an interface within a network.

Important:
- One machine → multiple interfaces
- One interface → multiple IPs (possible)
- IP ≠ machine

Example:
```bash
ip addr show wlp2s0
```

---

## 4. Routing Table

The routing table decides **where packets go**.

View it using:
```bash
ip route
```

### Default Route:
```text
default via 192.168.1.1 dev wlp2s0
```

Meaning:
- If destination is unknown → send to gateway
- Only one default route exists to avoid ambiguity

---

## 5. Route Decision Simulation

Check how the kernel routes traffic:
```bash
ip route get 8.8.8.8
```

Shows:
- Interface used
- Gateway chosen
- Source IP

---

## 6. Practical Commands Used

### List interfaces:
```bash
ip link
ip -br link
```

### Show IPs:
```bash
ip addr
ip -br addr
```

### Show routing rules:
```bash
ip route
```

### Test connectivity:
```bash
ping 8.8.8.8
```

---

## 7. Important Observations

- `lo` cannot send traffic to the internet
- Removing default route breaks internet, not local networking
- Routers are always the first hop for internet traffic
- Virtual interfaces behave like real ones

---

## 8. Cross-Questions & Answers

**Q: Can loopback traffic use default gateway?**  
A: No. Loopback traffic never leaves the machine.

**Q: Does localhost work without Wi-Fi?**  
A: Yes.

**Q: Why Docker creates `docker0`?**  
A: To provide a virtual network bridge for containers.

**Q: Why VPN creates a new interface?**  
A: To reroute traffic through an encrypted tunnel using a new default path.

---
