#!/bin/bash
# creating directory for scans

echo -e "Usage: jmap.sh <IP> skip(optional to skip scanning all UDP ports)\n"
if [ "$(id -u)" -ne 0 ];
        then echo "Not root. Exiting."
        exit
fi

if [ ! -d "nmap-scans-$1" ]; then
        mkdir nmap-scans-$1
fi

cd nmap-scans-$1

if [ ! -d "tmp" ]; then
        mkdir tmp
fi

echo -e "[+]+ Scanning for quick wins..\n"
nmap -sS -O -p80,443,21,23,88,139,445,8080 -sV -Pn $1

echo -e "\n[+] Scanning all ports... this may take a while."
nmap -T4 -p- -Pn $1 | grep open | cut -d "/" -f1 > tmp/open-ports.txt

# creating nmap readable ports file
tr '\n' ',' < tmp/open-ports.txt > tmp/open-nmap.txt
truncate -s -1 tmp/open-nmap.txt

nmap -sV -sC -sS -Pn --traceroute --version-all -p$(cat tmp/open-nmap.txt) $1 -oN nmap-tcp.all
grep open nmap-tcp.all > nmap-versions-tcp

echo -e "\n[+] TCP scans complete. Running UDP scans now... this will take a while.\n"

nmap -sU -sV -Pn -p7,69,88,111,123,161,162,3702,5353,10161,10162,44818,47808 -T4 $1 -oN tmp/nmap-udp.init1
nmap -sU -sV -Pn --top-ports 100 -T4 $1 -oN tmp/nmap-udp.init2

# creating files with only ports and version info
cat tmp/nmap-udp.init1 tmp/nmap-udp.init2 > nmap-udp.init
grep "open " nmap-udp.init > tmp/nmap-versions-udp
sort -u tmp/nmap-versions-udp > nmap-versions-udp

echo -e "[+] Initial UDP scans are complete. Scanning all UDP ports now unless skipped. \n"

if [[ "$2" == "skip" ]]; then
        cat nmap-versions-tcp nmap-versions-udp > nmap-versions.txt
        rm nmap-versions-tcp 
        rm nmap-versions-udp
        echo "[+] Scans completed."
        exit
fi

nmap -sU -p- -Pn T4 $1 -oN tmp/nmap-udp.all

cat tmp/nmap-udp.all | grep "open " cut -d "/" -f1 > tmp/open-ports-udp.txt
tr '\n' ',' < tmp/open-ports-udp.txt > tmp/open-nmap-udp.txt
truncate -s -1 tmp/open-nmap-udp.txt

nmap -sU -sV -Pn --version-all -p$(cat tmp/open-nmap-udp.txt) $1 -oN nmap-udp.all

# cleaning up
grep "open " nmap-udp.all > nmap-versions-udp
cat nmap-versions-tcp nmap-versions-udp > nmap-versions
sort -u nmap-versions > nmap-versions.txt
rm nmap-versions
rm nmap-versions-tcp 
rm nmap-versions-udp

echo "[+] All scans complete."
