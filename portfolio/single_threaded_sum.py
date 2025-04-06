# This script reads two files, each containing a list of integers. 
# This script writes a new file where each line is the sum of the integers from the two files at the same index.
# It uses a single thread to perform the summation.

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
