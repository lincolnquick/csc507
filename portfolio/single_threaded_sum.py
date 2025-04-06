"""
Filename: single_threaded_sum.py
Author: Lincoln Quick
Course: CSC507 Foundations of Operating Systems
Date: April 6, 2025
Description: This script reads two large files line by line, adds corresponding numbers from each file,
and writes the result to a new file using a single thread.
"""

import time

def add_files_single_thread(file1, file2, output):
    import time
    start = time.time()

    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output, 'w') as out:
        for l1, l2 in zip(f1, f2):
            try:
                total = int(l1.strip()) + int(l2.strip())
                out.write(f"{total}\n")
            except ValueError:
                continue

    elapsed = time.time() - start
    print(f"Single-threaded sum completed in {elapsed:.2f} seconds")
    return elapsed

if __name__ == "__main__":
    add_files_single_thread('hugefile1.txt', 'hugefile2.txt', 'totalfile.txt')
