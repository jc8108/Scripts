# Check if the correct number of arguments is provided
if ($args.Count -ne 3) {
    Write-Host "Usage: ./volwrap.ps1 DIR DMP Win10XXX
Example: ./volwrap.sh my-plugins memory.dmp Win10xxxxx"
    exit
}

# Assign arguments to variables
$DIR = $args[0]
$DMP = $args[1]
$PROFILE = $args[2]

# Run the initial kdbgscan command
python vol.py --plugins=$DIR -f $DMP --profile=$PROFILE kdbgscan

# Prompt user for the KDBG offset
$OFFSET = Read-Host "Enter the KDBG offset (e.g., 0x123456)"

# Check if the 'output' directory exists; if not, create it
if (-not (Test-Path -Path "output" -PathType Container)) {
    New-Item -ItemType Directory -Force -Path "output"
}

# Extract the base name of the DMP file without extension
$DMP_BASE = [System.IO.Path]::GetFileNameWithoutExtension($DMP)

# List of commands to run
$commands = @(
    "pslist"
    "pstree"
    "psxview"
    "psinfo"
    "getsids"
    "netscan"
    "Winesap"
    "mftparser"
)

# Loop over the commands and run each one, saving output to the appropriate file
foreach ($cmd in $commands) {
    $OUTPUT_FILE = "output\$DMP_BASE-$cmd.txt"
    python vol.py --plugins=$DIR -f $DMP --profile=$PROFILE -g $OFFSET $cmd | Out-File -FilePath $OUTPUT_FILE -Encoding utf8
    Write-Host "Output saved to $OUTPUT_FILE"
}
