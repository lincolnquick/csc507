#!/bin/bash

# This script multiplies file1.txt and file2.txt by 1000 to make billion-line files.

echo "Creating hugefile1.txt and hugefile2.txt..."

for i in {1..1000}
do
    cat file1.txt >> hugefile1.txt
    cat file2.txt >> hugefile2.txt
done

echo "Done!"