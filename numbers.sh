#!/bin/bash

# This script generates 1,000,000 random numbers and stores them in file1.txt, 
# and outputs the total time in seconds to run the script.

# First display system time
echo "Start time: $(date)"

SECONDS=0

rm -f  file1.txt

for ((i=1; i<1000000; i++))
do
   echo $RANDOM >> file1.txt
done

# Display elapsed seconds
echo "Script run time: $SECONDS seconds"

# Display system time after running
echo "End time: $(date)"

