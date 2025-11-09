# Python for Ethical Hacking

> kali linux automation, attacks, security — small collection of Python tools and PoCs

---

## Table of contents

* [Project overview](#project-overview)
* [Repository structure](#repository-structure)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [How to use — quick examples](#how-to-use---quick-examples)
* [Projects (what I built)](#projects-what-i-built)
* [Security & legal notice](#security--legal-notice)
* [How to contribute / add new projects](#how-to-contribute--add-new-projects)
* [Development notes & learning outcomes](#development-notes--learning-outcomes)
* [Contact / Author](#contact--author)
  

---

## Project overview

This repository collects small Python tools, scripts and proofs-of-concept I developed while learning and experimenting with network security on Kali Linux. The code demonstrates automated tasks (MAC changer, network scanner) and network attack techniques used for educational, research and lab purposes.

> ⚠️ Only run these tools in isolated lab environments or on systems where you have explicit permission to test.

---

## Repository structure

```
Python-for-Ethical-hacking/
├─ MITM/              # man‑in‑the‑middle related scripts (PoCs)
├─ Mac Changer/       # scripts that change network interface MAC address
├─ Network_Scanner/   # network discovery and port scanning scripts
├─ PacketListener/    # passive packet capture, filtering and pcap export scripts
├─ Keylogger/         # educational keylogger PoCs demonstrating keyboard event capture (for lab/defensive research only)
└─ README.md          # this file
```

> If your repo contains additional files or folders, update this section accordingly.

---

## Prerequisites

* Linux (Kali or any distro with `ip`/`ifconfig`/`iwconfig` tools)
* Python 3.8+
* `pip` for installing dependencies
* Common Python libraries used in networking and input-capture tools: `scapy`, `pcapy` (or `pyshark`/`pylibpcap`), `netifaces`, `pynput` or `keyboard` for keylogger PoCs, `requests`, `socket` (standard lib)
* Root/administrative privileges for low-level network operations and for accessing input devices (e.g. `/dev/input/*`) when testing keylogger examples.

Install system packages (example for Debian/Kali):

```bash
sudo apt update && sudo apt install -y python3 python3-pip net-tools iproute2 libpcap-dev
```

Install Python packages:

```bash
python3 -m pip install --user scapy netifaces pcapy pynput keyboard
```

````

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/hariharaeshwar/Python-for-Ethical-hacking.git
cd Python-for-Ethical-hacking
````

2. Inspect each project folder and read project-specific instructions (usually at top of file or an inline comment).

---

## How to use — quick examples

Below are suggested usage examples. Replace `<script.py>` and arguments with the actual filenames present in each folder.

### Run a network scanner (example)

```bash
sudo python3 Network_Scanner/scan_network.py --target 192.168.1.0/24
```

### Change MAC address (example)

```bash
sudo python3 "Mac Changer/mac_changer.py" --interface wlan0 --mac 00:11:22:33:44:55
```

### PacketListener — capture and save packets (example)

```bash
# Start a passive packet listener and write to capture.pcap
sudo python3 PacketListener/packet_listener.py --iface eth0 --filter "tcp port 80" --out capture.pcap

# Example: display a short summary of live traffic
sudo python3 PacketListener/packet_listener.py --iface wlan0 --summary
```

### Keylogger — educational capture example (example)

```bash
# Many keylogger PoCs require root to read input devices. Run only in a lab VM.
sudo python3 Keylogger/keylogger.py --duration 60 --out keys.txt

# Or run a keyboard event monitor that prints events to stdout
sudo python3 Keylogger/monitor_keys.py --iface none
```

### MITM proof-of-concept (example)

```bash
# MITM scripts usually require scapy and ip_forward enabled
sudo sysctl -w net.ipv4.ip_forward=1
sudo python3 MITM/mitm_poC.py --iface eth0 --target 192.168.1.5
```

Adapt the commands to the real filenames and options in each folder.

---

## Projects (what I built)

Below are short, resume‑friendly one‑line descriptions for each folder — replace or expand as needed.

* **MITM/** — Man‑in‑the‑middle PoCs using raw packets (Scapy) and IP forwarding. Demonstrates packet sniffing and traffic manipulation for lab exercises.
* **Mac Changer/** — Simple automation to change the MAC address of a network interface to a user-specified address or a randomized value.
* **Network_Scanner/** — Scripts for host discovery and port scanning (ICMP ping sweep, TCP connect scans) to enumerate devices in a network.
* **PacketListener/** — Passive packet capture and analysis scripts (using Scapy/pcapy), useful for understanding protocols and traffic flows in a controlled lab. Includes filters, summaries and optional PCAP export.
* **Keylogger/** — Educational keylogger proof‑of‑concepts that demonstrate keyboard event capture for defensive research and detection testing only. Includes explanations on detection, defenses, and safe lab usage.

---

## Security & legal notice

These tools are intended for educational use only. Misusing them against systems for which you do not have authorization is illegal and unethical. I take no responsibility for any misuse.

**Special notice about Keyloggers and PacketListeners:**

* **Keyloggers** are high-risk tools: they capture sensitive input (passwords, private messages). Only run keylogger code in isolated lab environments (VMs or controlled test machines) and never on systems that you do not own or have explicit written permission to test. Include detailed notes in the Keylogger folder describing how to detect and remove such tools, and how defenders can monitor for suspicious processes and `/dev/input` access.
* **PacketListeners** can capture sensitive network traffic. Use capture filters, avoid unnecessary data retention, and sanitize or delete captures that include credentials or PII.

Always run tests in isolated and legal environments (local VMs, lab networks, deliberately vulnerable targets like intentionally configured VMs). If you plan to publish demonstrations, sanitize outputs and avoid sharing real sensitive data.

---

## How to contribute / add new projects

1. Add a new folder with a clear name and include a `README.md` inside that folder explaining purpose and usage.
2. Keep scripts simple and documented: include `--help` and a short docstring at the top.
3. Use descriptive commit messages and consider tagging major milestones.

---

## Development notes & learning outcomes

You can use the following short checklist in your personal profile or CV:

* Built Python scripts for network discovery, MAC manipulation, and MITM PoCs using Scapy and system network utilities.
* Practiced safe lab testing on Kali Linux; learned packet crafting and network automation.

---

## Contact / Author

Hariharaeshwar K — feel free to open issues or contact me via GitHub profile.


