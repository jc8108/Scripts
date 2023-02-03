#!/bin/bash
# $1 variable is for IP and $2 is for any additional flags you want to add
echo -e "[+]+ Scanning for quick wins..\n"
sudo nmap -sS -p80,443,21,23,88,139,445,8080 -sV $2 $1
echo "[+] Scanning all ports... this may take a while."
sudo nmap -T4 -p- $1 | grep "open " | cut -d "/" -f1 > open-ports.txt
# creating nmap readable ports file
tr '\n' ',' < open-ports.txt > ports-nmap.txt
truncate -s -1 ports-nmap.txt
echo -e "\n[+] Running in-depth check on open ports..\n"
sudo nmap -A -sS --version-all -p$(cat ports-nmap-tcp.txt) $2 $1 -oN nmap-tcp.all
grep "open " nmap-tcp.all > nmap-versions.txt
echo -e "\n[+] TCP scans complete. Running UDP scans now\n[+] Scanning top UDP ports and then all... this will take a while."
sudo nmap -sU -p- -T4 $1 -oN nmap-udp.init
cat nmap-udp.init | grep open cut -d "/" -f1 > open-ports-udp.txt
tr '\n' ',' < open-ports-udp.txt >> ports-nmap.txt
truncate -s -1 ports-nmap-udp.txt
nmap -sU -sV --version-all -p$(cat ports-nmap-udp.txt) $2 $1 -oN nmap-udp.all
grep "open " nmap-udp.all >> nmap-versions.txt
