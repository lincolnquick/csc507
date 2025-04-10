"""
Filename: setup_and_verify.py
Author: Lincoln Quick
Course: CSC507 Foundations of Operating Systems
Date: April 6, 2025
Description: Automates the full setup process for the CSC507 portfolio project. 
Generates input files, builds billion-line datasets, verifies their correctness, 
and runs all performance comparisons. Confirms output accuracy and cleans up temporary files.
"""

import os
import subprocess
import sys
import glob

# Helper to ensure script is executable
def ensure_executable(script_name):
    if not os.path.exists(script_name):
        print(f"Error: {script_name} not found.")
        sys.exit(1)
    if not os.access(script_name, os.X_OK):
        print(f"Setting execute permission for {script_name}")
        subprocess.run(["chmod", "+x", script_name], check=True)

# Helper to run a shell script
def run_script(script_name):
    print(f"\nRunning {script_name}...")
    result = subprocess.run([f"./{script_name}"])
    if result.returncode != 0:
        print(f"Error running {script_name}.")
        sys.exit(1)

# Helper to verify word count
def verify_wc(file_path, expected_lines=None):
    print(f"\nVerifying line count in {file_path}...")
    result = subprocess.run(["wc", "-l", file_path], capture_output=True, text=True)
    print(result.stdout.strip())
    if expected_lines:
        count = int(result.stdout.strip().split()[0])
        if count != expected_lines:
            print(f"WARNING: Expected {expected_lines} lines but got {count}")

# Preview file contents
def preview_file(file_path):
    print(f"\nPreview of {file_path}:")
    print("First 5 lines:")
    subprocess.run(["head", "-5", file_path])
    print("\nLast 5 lines:")
    subprocess.run(["tail", "-5", file_path])

# Clean up temp files
def cleanup_temp_files():
    print("\nCleaning up temporary test files...")
    for pattern in ["test1.txt", "test2.txt", "totalfile_part_*.txt", 
                "hugefile*_part_*.txt", "*_chunk_*.txt"]:
        for file in glob.glob(pattern):
            try:
                os.remove(file)
                print(f"Deleted {file}")
            except Exception as e:
                print(f"Error deleting {file}: {e}")

# Clean up all output files
def cleanup_all_files():
    print("\nCleaning up all large input and output files...")
    patterns = [
        "file1.txt", "file2.txt",
        "hugefile1.txt", "hugefile2.txt",
        "totalfile_single.txt", "totalfile_multi.txt", "totalfile_parallel.txt"
    ]
    for pattern in patterns:
        try:
            os.remove(pattern)
            print(f"Deleted {pattern}")
        except Exception as e:
            print(f"Error deleting {pattern}: {e}")

def main():
    print("=== Setup and Verification Script ===")

    # Ensure shell scripts are present and executable
    for script in ["numbers.sh", "make_hugefiles.sh"]:
        ensure_executable(script)

    # Run number generation
    run_script("numbers.sh")

    # Run make_hugefiles
    run_script("make_hugefiles.sh")

    # Verify file1.txt and file2.txt line counts
    verify_wc("file1.txt", expected_lines=1_000_000)
    verify_wc("file2.txt", expected_lines=1_000_000)

    # Verify hugefile1.txt and hugefile2.txt line counts
    verify_wc("hugefile1.txt", expected_lines=1_000_000_000)
    verify_wc("hugefile2.txt", expected_lines=1_000_000_000)

    # Run compare_runtimes.py
    print("\nRunning compare_runtimes.py...")
    subprocess.run(["python3", "compare_runtimes.py"], check=True)

    # Verify and preview result files
    for fname in ["totalfile_single.txt", "totalfile_multi.txt", "totalfile_parallel.txt"]:
        if os.path.exists(fname):
            verify_wc(fname)
            preview_file(fname)
        else:
            print(f"WARNING: Output file {fname} not found.")

    cleanup_temp_files()

    if "--cleanup" in sys.argv:
        cleanup_all_files()
        print("All input and output files cleaned up.")
        
    print("\n=== All done! ===")

if __name__ == "__main__":
    main()