# Python for Ethical Hacking

Kali-focused Python scripts for network reconnaissance, MAC address management, and man-in-the-middle (MITM) experiments.  
This repository contains small tools and learning projects implemented in Python to automate common tasks in penetration testing labs (for ethical, legal use only).

> **Important:** Only run these scripts in controlled lab environments or on systems you own or have explicit permission to test. Misuse may be illegal.

---

## Contents

- `Network_Scanner/` — lightweight network discovery and port scanning scripts.
- `Mac Changer/` — scripts to display and change the MAC address.
- `MITM/` — proof-of-concept MITM automation (e.g., ARP spoofing/packet forwarding) for learning.

*(Each folder contains Python scripts and README-style comments. See each folder for usage examples.)*

---

## Features (high level)

- Network discovery (ping sweep, host detection)
- Port scanning (TCP SYN/connect scans)
- MAC address change and restoration
- ARP spoofing and traffic forwarding for lab MITM tests

---

## Prerequisites

- Python 3.8+  
- Linux (Kali recommended) — some scripts require `root` privileges and Linux network tooling.
- Python packages (install from `requirements.txt` — see below)

Example:
```bash
# from repository root
python3 -m pip install -r requirements.txt
