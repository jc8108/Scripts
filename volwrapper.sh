#!/bin/bash

# Check if correct number of arguments provided
if [ "$#" -ne 3 ]; then
    echo "Usage: ./volwrap.sh <plugin-directory> <memory dump file> <memory profile>
Example: ./volwrap.sh my-plugins memory.dmp Win10xxxxx"
    exit 1
fi

# Assign arguments to variables
DIR=$1
DMP=$2
PROFILE=$3

# Run the initial kdbgscan command
python vol.py --plugins="$DIR" -f "$DMP" --profile="$PROFILE" kdbgscan

# Prompt user for the KDBG offset
read -p "Enter the KDBG offset (e.g., 0x123456): " OFFSET

# Check if the 'output' directory exists; if not, create it
if [ ! -d "output" ]; then
    mkdir output
fi

# List of commands to run
commands=(
    "pslist"
    "pstree"
    "psxview"
    "psinfo"
    "getsids"
    "netscan"
    "winesap"
    "mftparser"
)

# Extract the base name of the DMP file without extension
DMP_BASE=$(basename "$DMP" | sed 's/\(.*\)\..*/\1/')

# Loop over the commands and run each one, saving output to the appropriate file
for cmd in "${commands[@]}"; do
    OUTPUT_FILE="output/${DMP_BASE}-${cmd}.txt"
    python vol.py --plugins="$DIR" -f "$DMP" --profile="$PROFILE" -g "$OFFSET" "$cmd" > "$OUTPUT_FILE"
    echo "Output saved to $OUTPUT_FILE"
done
