# CSC507 Portfolio Project: Working with Big Data using Multithreading

**Course:** CSC 507 – Foundations of Operating Systems  
**Author:** Lincoln Quick  
**Instructor:** Dr. Jessica Schwartz  
**Date:** April 6, 2025

## Overview

This project demonstrates efficient techniques for processing massive datasets using multithreading and parallelism, as covered in **CSC507: Foundations of Operating Systems**. The task involves summing corresponding lines from two billion-line files and comparing performance across:

- A **single-threaded** implementation  
- A **multithreaded** implementation  
- A **parallel multithreaded** implementation using file splits and multiprocessing

## Project Goal

You are tasked with generating two files—`hugefile1.txt` and `hugefile2.txt`—each containing **1 billion lines** of random integers. These are then summed line-by-line into a third file, `totalfile.txt`, using different threading and parallelism techniques to assess performance.

This project aligns with the course objective of understanding **real-time process scheduling**, **kernel-mode vs user-mode execution**, and **multithreaded data handling in OS environments**.

---

## Components

| File                   | Purpose                                                                 |
|------------------------|-------------------------------------------------------------------------|
| `numbers.sh`           | Generates `file1.txt` and `file2.txt`, each with 1 million random integers |
| `make_hugefiles.sh`    | Multiplies `file1.txt` and `file2.txt` by 1000 to generate huge files   |
| `double_numbers.sh`    | Legacy shell script for doubling each line in `file1.txt`               |
| `single_threaded_sum.py` | Adds lines from two files using a single thread                       |
| `multithreaded_sum.py` | Adds lines using multithreading for better CPU utilization              |
| `split_files.py`       | Splits huge input files into 10 parts each                              |
| `parallel_driver.py`   | Runs 10 parallel processes for summing file chunks                      |
| `compare_runtimes.py`  | Benchmarks single, multithreaded, and parallel versions                 |
| `setup_and_verify.py`  | One-click setup, execution, and verification of outputs                 |
| `.gitignore`           | Ensures only source files are tracked by Git                           |

---

## How to Run the Project

### 1. Install Requirements

Ensure Python 3 and Bash are installed. No external packages are required.

### 2. Execute Setup Script

To run the full workflow:

```bash
python3 setup_and_verify.py
```

This will:

- Generate initial random number files
- Expand them to 1 billion lines
- Run all three implementations
- Verify correctness and print runtime comparisons

### 3. Optional: Run Individual Steps

```bash
bash numbers.sh
bash make_hugefiles.sh
python3 compare_runtimes.py
```

---

## Output Verification

The `setup_and_verify.py` script also:

- Verifies that all output files contain the expected number of lines
- Prints the first and last 10 lines of each output to confirm correct summation

---

## Notes

- **Storage**: Ensure at least 10–15 GB of free space
- **Runtime**: Expect up to 20+ minutes on slower machines (particularly for the multithreaded full pass)
- **Parallelism**: Multithreaded and parallel scripts automatically detect CPU cores for best performance