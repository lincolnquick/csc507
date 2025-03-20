# CSC507 - Module 6: Real-Time Process Scheduling Experiment

## Overview
This project evaluates different methods of processing large files by doubling numeric values in each line. The experiment tests single-process execution and parallel processing with different file splits to simulate real-time scheduling scenarios.

## Files
- `numbers.py` - Generates random numbers into an input file.
- `double_numbers.py` - Contains three methods for doubling numbers in a file.
- `split_file.py` - Splits an input file into multiple parts.
- `run_parallel.py` - Processes each file part in parallel using multiprocessing.
- `combine_files.py` - Combines processed file parts into a single output file.
- `run_experiments.py` - Automates the experiments, running all tests and saving results.

## How to Run
From the `mod6` directory:
```bash
python3 run_experiments.py