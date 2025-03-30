#!/bin/bash

# This script generates two files, each with 1 million random numbers: 
# file1.txt and file2.txt.

# First display system time
echo "Start time: $(date)"
SECONDS=0

rm -f  file1.txt file2.txt

for ((i=1; i<=1000000; i++))
do
   echo $RANDOM >> file1.txt
   echo $RANDOM >> file2.txt
done

# Display elapsed seconds
echo "Script run time: $SECONDS seconds"

# Display system time after running
echo "End time: $(date)"

