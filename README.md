# Scripts
Just a place to store simple scripts.

--AutoHash-- A python script that takes one arguement when you run it: the filepath of a file that you want to obtain the MD5 and SHA256 hashes of.
You can then supply it a hash that you have to compare it against what it came up with to verify that they are both the same. 

--Jmap-- A bash script that runs different nmap scans. A short TCP scan, all TCP ports, a short UDP scan, and an optional all UDP port scan.

--ADNames-- A python script to take a list of names, and then create common first-last combinations used in Active Directory such as f.last or first.last

--good-bot-- Bash script that will wget a robots.txt file from a webpage, parse it, and then open up all those disallowed directories in Firefox.

--sweep.sh and whos-there.sh-- A ping and Nmap alternative that look to see what hosts are reachable.

# Tools
--PasswordAuditor-- A python program that searches in a password dump (I used rockyou.txt) for a supplied password to see if it is in there.
BYOPD (bring your own password dump). 

--BreachDefense-- A python game that loops until 1 of 2 outcomes is achieved- the hackers destroy your network or you defeat all the hackers.
Sometimes you win, sometimes you lose! As of now it takes no input, more of an experiment to play around with classes.

--SubnetMaskfinder-- A python program to help find subnet masks for class A, B, and C networks given the required hosts and subnets.

--SubnetTool-- A python program that outputs subnet info such as network address, and broadcast address given an IPv4 address
and either its CIDR notation or its subnet address.

--Webwrapper-- A bash script that takes a URL of a webshell, prompts you for a command, and then passes it to curl.
