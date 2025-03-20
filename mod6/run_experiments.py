import subprocess
import time
import os
import sys

# Redirect print output to both terminal and a text file
class Logger(object):
    def __init__(self, filename):
        self.terminal = sys.stdout
        self.log = open(filename, "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        self.terminal.flush()
        self.log.flush()

# Replace stdout with logger
sys.stdout = Logger("experiment_results.txt")

results_summary = {}

def check_or_generate_file(count, filename):
    """
    Check if filename exists and has exactly 'count' lines.
    If not, regenerate it with 'numbers.py' and rename the output.
    """
    if os.path.exists(filename):
        print(f"Found existing {filename}. Verifying line count...")
        with open(filename, 'r') as f:
            line_count = sum(1 for _ in f)
        if line_count == count:
            print(f"{filename} has correct line count ({line_count} lines). No regeneration needed.")
            return
        else:
            print(f"{filename} has incorrect line count ({line_count} lines). Regenerating...")
    else:
        print(f"{filename} not found. Generating new file...")

    # Generate random numbers using numbers.py (parallel for speed)
    print(f"Generating {count} random numbers into file2_parallel.txt...")
    subprocess.run("python3 numbers.py", shell=True, check=True)

    # Rename file2_parallel.txt to desired filename
    if os.path.exists("file2_parallel.txt"):
        os.rename("file2_parallel.txt", filename)
        print(f"Renamed file2_parallel.txt to {filename}.")
    else:
        print("Error: file2_parallel.txt was not created.")
        exit(1)

def run_double_numbers(filename):
    print("\n--- Running double_numbers.py (single file processing) ---")
    # Copy the file to file1.txt, because double_numbers.py expects that filename
    subprocess.run(f"cp {filename} file1.txt", shell=True, check=True)
    subprocess.run("python3 double_numbers.py", shell=True, check=True)

def split_and_parallel_process(filename, parts, results_summary):
    print(f"\n--- Splitting {filename} into {parts} parts ---")

    start_time = time.perf_counter()  # Start timing the whole operation

    try:
        # Copy the file to file1.txt because split_file.py expects that filename
        subprocess.run(f"cp {filename} file1.txt", shell=True, check=True)

        # Split the file into N parts
        subprocess.run(f"python3 split_file.py file1.txt {parts}", shell=True, check=True)

        # Run parallel processing
        subprocess.run(f"python3 run_parallel.py {parts}", shell=True, check=True)

        # Combine the results
        subprocess.run(f"python3 combine_files.py {parts} newfile1_combined_{parts}_parts.txt", shell=True, check=True)

        # Measure total elapsed time
        elapsed_time = time.perf_counter() - start_time

        # Add to the summary results dictionary
        results_summary[f"{filename} split {parts} parts"] = elapsed_time

        print(f"\n--- Completed {parts}-part process for {filename} in {elapsed_time:.4f} seconds ---")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred during the split/parallel/combine process: {e}")

def main():
    test_cases = [
        {"count": 1_000_000, "description": "1 Million Lines", "filename": "file1_1M.txt"},
        {"count": 10_000_000, "description": "10 Million Lines", "filename": "file1_10M.txt"}
    ]

    splits = [10, 2, 5, 20]

    for test in test_cases:
        print(f"\n============================")
        print(f"Testing {test['description']}")
        print(f"============================\n")

        # Step 1: Ensure file1_XM.txt exists and has the correct number of lines
        check_or_generate_file(test["count"], test["filename"])

        # Step 2: Run double_numbers.py (single file processing)
        run_double_numbers(test["filename"])

        # Step 3: Run split/parallel/combine workflows
        for split_count in splits:
            split_and_parallel_process(test["filename"], split_count, results_summary)

    print("\nAll experiments completed!")

    print("\n=====================================")
    print("Summary of Results (Time in Seconds)")
    print("=====================================\n")

    for test, elapsed in results_summary.items():
        print(f"{test}: {elapsed:.4f} seconds")

if __name__ == "__main__":
    main()