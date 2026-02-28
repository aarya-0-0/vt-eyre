# VT-Eyre: VirusTotal CLI & GUI Scanner

VT-Eyre is a lightweight Python tool that allows you to scan URLs and files for malicious content using the VirusTotal API. It provides both a command-line interface (CLI) and a graphical interface (GUI) for ease of use.

---

## Features

- Scan URLs for malware and suspicious content.
- Scan files for malicious behavior.
- Supports custom backend server URLs.
- CLI tool for terminal users.
- Simple GUI for desktop users.
- Displays a clear summary of scan results: Malicious, Suspicious, Harmless, Undetected.

---
## Scan Files
command: vt-eyre --file malicious.txt

---
## Scan url 
command: vt-eyre --url example.com

## Installation

Install VT-Eyre via pip:

```bash
pip install vt-eyre==0.8.0

