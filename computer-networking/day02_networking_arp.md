# Networking Notes --- Day 2

## Core Concepts Covered

### 1. ARP (Address Resolution Protocol)

-   Maps IP → MAC address
-   Works only inside a local network (LAN)
-   Uses broadcast to find device MAC
-   Stores results in ARP cache

------------------------------------------------------------------------

### 2. When ARP Runs

ARP runs only when - device needs MAC - MAC not present in cache

It does NOT run: - for every packet - periodically by default

------------------------------------------------------------------------

### 3. ARP Cache Behavior

-   Entries stored temporarily
-   Timeout varies (OS dependent)
-   Removed after expiry
-   Re‑requested when needed

Check cache: arp -a ip neigh

Clear cache: ip neigh flush all

------------------------------------------------------------------------

### 4. Local vs Internet Communication

Same LAN Device: 1. Checks ARP cache 2. If missing → Broadcast 3. Target
replies with MAC 4. Direct communication begins

------------------------------------------------------------------------

Internet Destination Device: 1. Sees destination not in local subnet 2.
Sends packet to default gateway 3. ARPs for router MAC (not destination
server)

Important: Your system never learns Google's MAC

------------------------------------------------------------------------

### 5. Router's Role

Router keeps: - ARP table (local devices) - Routing table (networks)

Router does not broadcast when reply arrives.\
It already knows which device to send data to.

------------------------------------------------------------------------

### 6. ARP vs Routing Table

  Feature    ARP Table        Routing Table
  ---------- ---------------- -------------------
  Purpose    IP→MAC mapping   Path selection
  Scope      Local LAN only   Entire networks
  Used for   Frame delivery   Packet forwarding

------------------------------------------------------------------------

### 7. Packet Flow Reality (Correct Model)

When reply comes from internet:

Server → Router → Your Device

Router: - checks destination IP - looks up MAC in its ARP table - sends
directly

No broadcast needed if cached.

------------------------------------------------------------------------

### 8. Commands Learned

Show neighbors: ip neigh

Scan LAN: for i in {1..254}; do ping -c1 -W1 192.168.1.\$i & done

Show routing table: ip route

Show interface info: ip addr

------------------------------------------------------------------------

### 9. Clarified Doubts

Does router broadcast replies?\
No.

Does ARP run continuously?\
No --- only when mapping missing.

Can MAC duplicate exist?\
Yes (spoofing / cloning).

Does ARP work across internet?\
No.

Does every device have ARP table?\
Yes --- every networked device maintains one.

Does pinging Google store its MAC?\
No --- only router MAC stored.

------------------------------------------------------------------------

### 10. Mental Model Rule (Important)

Always remember order:

Routing decides WHERE to send\
ARP decides WHO gets it locally

------------------------------------------------------------------------

# End of Day 2 Notes
