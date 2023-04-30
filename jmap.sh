#!/bin/bash

# usage
echo -e "Usage: sudo ./jmap.sh IP all (all is optional, if you want to scan all UDP ports)\n"

# checking if root
if [ "$(id -u)" -ne 0 ];
then echo “Not root. Exiting.”
exit
fi

# creating directory for scans
if [ ! -d "$1-nmap-scans" ]; then
    mkdir $1-nmap-scans
fi

cd $1-nmap-scans

# run quick TCP scans
echo -e "[+]+ Scanning for quick wins..\n"
nmap -p80,443,21,23,88,139,445,8080 -sV -Pn -sC $1 -oN tcp-quick.nmap

# run full TCP scans
echo -e "\n[+] Scanning all ports… this may take a while."
nmap -T4 -p- -Pn -sC -sV — traceroute — version-all $1 -oN tcp-all.nmap

# run top UDP sans
echo -e "\n[+] Scanning top UDP ports.. this will take a while."

nmap -sU -sV -Pn -p7,53,69,88,111,123,161,162,3702,5353,10161,10162,44818,47808 -T4 $1 -oN udp-top.nmap

nmap -sU -sV -Pn — top-ports 100 -T4 $1 >> udp-top.nmap

# check if we want to run full UDP scans
if [ "$2" == "all" ]; then
    echo -e "\n[+] Scanning all UDP ports. This will take forever."
    nmap -sU -p- -Pn T4 $1 -oN udp-all.nmap
fi

# create file with just open ports and version
cat * | grep "open " | tr -s " " | sort -u > open.nmap
