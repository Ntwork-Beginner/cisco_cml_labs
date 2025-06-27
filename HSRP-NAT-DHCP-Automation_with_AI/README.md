# Cisco CML: Redundant Network with HSRP, NAT, and DHCP

## 🧩 Topology Overview

This lab simulates a redundant network topology using:
- **HSRP** for gateway redundancy
- **NAT** for internet access
- **DHCP** for dynamic IP address allocation

![Network Topology]
![Screenshot 2025-06-15 192435](https://github.com/user-attachments/assets/ccc61c17-1199-4f58-9e72-f998a143115d)

---

## 📌 Devices and IP Configuration

### Routers:
- **R1**
  - `E0/0` → ISP1
  - `E0/1` → 172.16.1.2/24
  - **VIP**: 172.16.1.1 (HSRP)
  - **Loopback 0**: 10.1.1.1/24
- **R2**
  - `E0/0` → ISP2
  - `E0/1` → 172.16.1.3/24
  - **VIP**: 172.16.1.1 (HSRP)
  - **Loopback 0**: 20.1.1.1/24

### Switches:
- **S1 & S2**: Connect routers to PCs for internal network switching

### PCs:
- **PC1, PC2, PC3**
  - Interfaces: `E0`
  - Obtain IPs dynamically via DHCP

---

## 🛠️ Features Implemented

### 1. HSRP (Hot Standby Router Protocol)
- Ensures **gateway redundancy** between R1 and R2.
- Virtual IP: `172.16.1.1` used by all end devices.

### 2. NAT (Network Address Translation)
- Configured on both R1 and R2 to allow internet access for internal devices.
- **Overload NAT** used for multiple hosts sharing one public IP.

### 3. DHCP
- DHCP service configured on either R1/R2 to dynamically assign:
  - IP addresses
  - Subnet mask
  - Default gateway (VIP)
  - DNS servers (optional)

---

## 📥 Access Instructions

- Open this topology in **Cisco Modeling Labs (CML)**.
- Verify all nodes are started.
- Use console or VTY access to configure or monitor devices.
- PCs should receive IP addresses automatically and reach the internet via NAT.

---

## 🧪 Test Cases

- [ ] PCs receive IP from DHCP
- [ ] Ping from PCs to VIP (172.16.1.1)
- [ ] Internet access via NAT
- [ ] HSRP failover: Shut R1 and check R2 takes over

---

## 📎 Notes

- HSRP priority can be adjusted to control the active router.
- NAT ACL should match the correct internal subnet (e.g., 172.16.1.0/24).
- Optionally, DHCP could be offloaded to a dedicated server or use DHCP relay.

---

## 📁 Files

![Screenshot 2025-06-15 192411](https://github.com/user-attachments/assets/1ef8a906-7afa-4339-ae97-304f289c3ab6)
![Screenshot 2025-06-15 192435](https://github.com/user-attachments/assets/31ec770d-3305-47d9-ab38-ccf7c33fe7d5)

![Screenshot 2025-06-15 192335](https://github.com/user-attachments/assets/98212d16-2d63-409a-b7c5-13486c9ef0a0)
