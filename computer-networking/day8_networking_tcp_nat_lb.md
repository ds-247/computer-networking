# Day 8 -- Advanced Networking & Cloud Architecture

## 1. TCP Deep Dive

### Why TCP Needs Sequence Numbers

IP provides best-effort delivery. Packets may: - Arrive out of order -
Be lost - Be duplicated

TCP uses sequence numbers to: - Reorder packets - Detect loss - Enable
retransmission

------------------------------------------------------------------------

### ACK Loss Scenario

If data is received but ACK is lost: - Sender times out - Retransmits
data - Receiver discards duplicate - Sends ACK again

TCP is designed to handle duplicates safely.

------------------------------------------------------------------------

### Why UDP for Streaming?

-   No retransmission delay
-   Real-time priority over perfect reliability
-   Faster, lower overhead

------------------------------------------------------------------------

### Flow Control -- Sliding Window

Receiver advertises window size: - Prevents buffer overflow - Controls
how much sender can transmit

------------------------------------------------------------------------

### Congestion Control

TCP uses Slow Start: - Starts small - Gradually increases transmission
rate - Prevents congestion collapse

------------------------------------------------------------------------

## 2. netstat Analysis

### ESTABLISHED

Active connection.

### TIME_WAIT

Connection closed but waiting to ensure: - No delayed packets
interfere - Safe connection termination

### FIN_WAIT_1

Close initiated, waiting for acknowledgment.

------------------------------------------------------------------------

### Listening Ports

0.0.0.0 means: Listening on all network interfaces.

Important example ports: - 135 (Windows RPC) - 445 (SMB) - 3306 (MySQL)

Listening ≠ Exposed. Firewall determines exposure.

------------------------------------------------------------------------

## 3. NAT Explained

NAT allows: - Outbound initiated traffic - Response traffic

Blocks: - Unsolicited inbound traffic

Acts as connection tracker, not true firewall.

------------------------------------------------------------------------

## 4. Port Scanning Concept

Attackers use tools like: - Nmap - Masscan

They send SYN packets: - SYN-ACK → Port open - RST → Closed - No
response → Filtered

Only LISTENING ports are attack surface.

------------------------------------------------------------------------

## 5. Public vs Private IP

Private IP ranges (RFC1918): - 10.0.0.0/8 - 172.16.0.0/12 -
192.168.0.0/16

Not routable on public internet.

------------------------------------------------------------------------

## 6. AWS VPC Architecture

### Public Subnet

-   Has route to Internet Gateway (IGW)
-   Contains Load Balancer
-   Contains NAT Gateway

Route: 0.0.0.0/0 → IGW

------------------------------------------------------------------------

### Private Subnet

-   No direct IGW route
-   Route to NAT Gateway

Route: 0.0.0.0/0 → NAT Gateway

------------------------------------------------------------------------

## Traffic Flow

### Inbound

Client → IGW → Load Balancer → App Server

### Outbound

App Server → NAT Gateway → IGW → Internet

NAT allows outbound only.

------------------------------------------------------------------------

## 7. Internal VPC Routing

All subnets inside VPC can communicate via: Local route (e.g.,
10.0.0.0/16)

Load Balancer reaches App Server via private IP. NAT not involved in
internal routing.

------------------------------------------------------------------------

## 8. Security Best Practices

-   Only Load Balancer should have public IP
-   App Servers should be private
-   Databases should be private
-   Use Security Groups for controlled access

------------------------------------------------------------------------

## 9. Risk of Public IP on Private App

If App Server gets public IP: - Bypasses Load Balancer - Bypasses WAF -
Exposes attack surface - Enables lateral movement if compromised

Security principle: Reduce attack surface.

------------------------------------------------------------------------

# Day 8 Summary

You learned: - TCP reliability mechanisms - Flow & congestion control -
Port states & scanning - NAT mechanics - Public vs Private IP logic -
AWS VPC architecture - Inbound vs Outbound routing - Production security
layering

This completes Day 8 at infrastructure-architect level.
