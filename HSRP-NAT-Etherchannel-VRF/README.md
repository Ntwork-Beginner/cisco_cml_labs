# 🛠️ HSRP + NAT + VRF + EtherChannel Lab (Cisco)

This lab demonstrates an enterprise-like setup using multiple key networking concepts such as high availability, logical segmentation, and redundancy.

## 📡 Topology Overview

![Topology]![topology sc](https://github.com/user-attachments/assets/d5f89468-e5bb-45d7-8f47-0a82eac3082d)

### 🔍 Core Features Implemented:
- 🔄 **HSRP**: High Availability between R1 and R2 with Virtual IP `192.168.1.1`
- 🌐 **NAT Overload**: Internet access for internal hosts via `ip nat inside`/`outside`
- 🧩 **VRF**: Traffic segmentation with two Virtual Routing and Forwarding instances
  - `D1_VRF`: 192.168.1.11/24
  - `D2_VRF`: 192.168.1.22/24
- 🔗 **EtherChannel**: Port-channel between switches for link redundancy

---

## 💻 Devices & Interfaces

| Device | Role                 | Interfaces Used   | Notes                          |
|--------|----------------------|-------------------|--------------------------------|
| R1     | Primary Edge Router  | e0/0, e0/1        | HSRP Priority                  |
| R2     | Secondary Router     | e0/0, e0/1        | HSRP Standby                   |
| SL2    | Switch Layer Core 1  | e0/2, e0/3, e0/4  | EtherChannel with SL2_2       |
| SL2_2  | Switch Layer Core 2  | e0/1, e0/3, e0/4  | EtherChannel with SL2         |
| VRF    | End User Gateway     | e0/0, e0/1        | Hosts in separate VRFs        |
| D1     | End Device (VRF 1)   | -                 | IP: 192.168.1.11               |
| D2     | End Device (VRF 2)   | -                 | IP: 192.168.1.22               |

---

## ⚙️ Configuration Highlights

### ✅ HSRP (on both routers)
```bash
standby 1 ip 192.168.1.1
