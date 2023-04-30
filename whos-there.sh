nmap -sn $1 | grep "Nmap scan report for" | cut -d " " -f5 > hosts.txt
echo "The following hosts are up:"
cat hosts.txt
