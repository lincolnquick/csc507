#!/bin/bash

# Check if file1.txt exists
if [ ! -f file1.txt ]; then
	echo "file1.txt does not exist and is required to double numbers. Exiting."
	exit 1
fi

# Remove newfile1.txt if it already exists to avoid appending.
if [ -f newfile1.txt ]; then
	echo "Removing existing newfile1.txt to avoid appending."
	rm newfile1.txt
fi

echo "Starting to double numbers from file1.txt..."

SECONDS=0

while read -r number; do
	let "number *= 2"
	echo $number >> newfile1.txt
done < file1.txt

duration=$SECONDS
echo "Time elapsed: $duration seconds"
