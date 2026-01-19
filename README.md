# SysDoctor 🩺

SysDoctor is a simple, cross-platform CLI tool to quickly check your system’s health.

I built this after running into high CPU and memory usage issues on my own machine and realizing how inconvenient it is to jump between multiple commands to understand what’s going on.

SysDoctor brings the most useful system information into one clean command.

---

## Features

- Shows top CPU-consuming processes
- Displays memory and swap usage
- Shows system temperature (Linux only)
- Clean and readable terminal output
- Works on Linux, macOS, and Windows

---

## Requirements

- Python3 3.8+
- pip3

---

## Installation

Clone the repository:

```bash
git clone https://github.com/sm-maya/sysdoctor.git
cd sysdoctor
pip3 install psutil rich click
python3 cli.py scan

🩺 Linux System Doctor Scan

Top CPU Processes
...

Memory used: 65%
Swap used: 10%

Temperatures:
  coretemp Core 0: 62°C


