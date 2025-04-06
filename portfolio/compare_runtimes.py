"""
Filename: compare_runtimes.py
Author: Lincoln Quick
Course: CSC507 Foundations of Operating Systems
Date: April 6, 2025
Description: Executes and compares the performance of three implementations (single-threaded,
multithreaded, and parallel multithreaded) and reports their execution times.
"""
import shutil
import os
import subprocess

from single_threaded_sum import add_files_single_thread
from multithreaded_sum import add_files_multithreaded, count_lines
from parallel_driver import run_parallel_driver


def prepare_test_files():
    shutil.copy("hugefile1.txt", "test1.txt")
    shutil.copy("hugefile2.txt", "test2.txt")


def compare_runtimes():
    print("=== Runtime Comparison Script ===\n")

    # Determine consistent line count
    print("Counting total lines in hugefile1.txt...")
    total_lines = count_lines("hugefile1.txt")
    print(f"Line count for testing: {total_lines}")

    # SINGLE-THREADED
    prepare_test_files()
    print("\nRunning single-threaded version...")
    t1 = add_files_single_thread("test1.txt", "test2.txt", "totalfile_single.txt")
    os.remove("test1.txt")
    os.remove("test2.txt")

    # MULTITHREADED
    prepare_test_files()
    print("\nRunning multithreaded version...")
    t2 = add_files_multithreaded("test1.txt", "test2.txt", "totalfile_multi.txt", total_lines=total_lines)
    os.remove("test1.txt")
    os.remove("test2.txt")

    # SPLIT FILES FOR PARALLEL TESTING
    print("\nSplitting files for parallel version...")
    subprocess.run(["python3", "split_files.py"], check=True)

    # PARALLEL MULTITHREADED
    print("\nRunning parallel multithreaded version (10 file pairs)...")
    t3 = run_parallel_driver()

    print("\n=== Results ===")
    print(f"Single-threaded:         {t1:.2f} seconds")
    print(f"Multithreaded:           {t2:.2f} seconds")
    print(f"Parallel multithreaded:  {t3:.2f} seconds")


if __name__ == "__main__":
    compare_runtimes()