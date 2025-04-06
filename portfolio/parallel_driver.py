"""
Filename: parallel_driver.py
Author: Lincoln Quick
Course: CSC507 Foundations of Operating Systems
Date: April 6, 2025
Description: This script runs the multithreaded summation on 10 file pairs in parallel using multiprocessing,
and merges the results into a final output file.
"""
from multiprocessing import Process
from multithreaded_sum import add_files_multithreaded, count_lines
import os
import time

def process_pair(part_id):
    file1 = f"hugefile1_part_{part_id}.txt"
    file2 = f"hugefile2_part_{part_id}.txt"
    output = f"totalfile_part_{part_id}.txt"
    output_prefix = f"part{part_id}"

    total_lines = count_lines(file1)
    add_files_multithreaded(file1, file2, output, total_lines=total_lines, output_prefix=output_prefix)

def merge_final_output(num_parts, final_output):
    with open(final_output, 'w') as outfile:
        for i in range(1, num_parts + 1):
            part_file = f"totalfile_part_{i}.txt"
            with open(part_file, 'r') as infile:
                outfile.writelines(infile.readlines())
            os.remove(part_file)

def run_parallel_driver():
    start_time = time.time()
    num_parts = 10
    processes = []

    print("Starting parallel processing of 10 file pairs...")

    for i in range(1, num_parts + 1):
        p = Process(target=process_pair, args=(i,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print("Merging final output...")
    merge_final_output(num_parts, "totalfile_parallel.txt")

    elapsed = time.time() - start_time
    print(f"\nTotal parallel processing time: {elapsed:.2f} seconds")
    return elapsed