import subprocess
import time
import os

def run_command(description, command):
    print(f"\n=== {description} ===")
    start = time.perf_counter()

    subprocess.run(command, shell=True, check=True)

    end = time.perf_counter()
    print(f"{description} completed in {end - start:.4f} seconds.\n")

def generate_input_file(count, filename):
    print(f"\nGenerating {count} random numbers in {filename}...")
    # Call numbers.py in parallel mode for faster generation
    subprocess.run(f"python3 numbers.py", shell=True, check=True)
    # Rename the desired file to file1.txt
    os.rename("file2_parallel.txt", filename)
    print(f"Generated {filename}.\n")

def run_double_numbers(filename):
    print("\n--- Running double_numbers.py (single file processing) ---")
    subprocess.run(f"cp {filename} file1.txt", shell=True, check=True)
    subprocess.run("python3 double_numbers.py", shell=True, check=True)

def split_and_parallel_process(filename, parts):
    print(f"\n--- Splitting {filename} into {parts} parts ---")
    subprocess.run(f"cp {filename} file1.txt", shell=True, check=True)
    
    # Split the file into N parts
    subprocess.run(f"python3 split_file.py {parts}", shell=True, check=True)
    
    # Run parallel processing
    subprocess.run(f"python3 run_parallel.py {parts}", shell=True, check=True)
    
    # Combine the results
    subprocess.run(f"python3 combine_files.py {parts} newfile1_combined_{parts}_parts.txt", shell=True, check=True)

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

        # Step 1: Generate file1.txt
        generate_input_file(test["count"], test["filename"])

        # Step 2: Run double_numbers.py (method1/method2/method3)
        run_double_numbers(test["filename"])

        # Step 3: Run split/parallel/combine workflows
        for split_count in splits:
            split_and_parallel_process(test["filename"], split_count)

    print("\nAll experiments completed!")

if __name__ == "__main__":
    main()