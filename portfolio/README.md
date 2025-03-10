# CSC507 Portfolio Project  
**Author:** Lincoln Quick  
**CSC507 – Foundations of Operating Systems**  
**Instructor:** Dr. Jessica Schwartz  

This directory includes scripts and documentation for the CSC507 Portfolio Project. The project processes large text files with one million random numbers and compares execution times between Bash and Python implementations.

## Contents
- `double_numbers.sh` – Bash script that reads `file1.txt`, doubles each number, and writes to `newfile1.txt`.
- `double_numbers.py` – Python script implementing three different methods for doubling numbers.
- `Makefile` – Automates running the scripts and cleaning generated files.

## Usage
Ensure `file1.txt` exists in this directory before running any scripts.

### Makefile Commands
- make run_bash_script      # Runs double_numbers.sh
- make run_python_methods   # Runs all three methods in double_numbers.py
- make clean                # Removes generated output files

## Notes
- Outputs include `newfile1.txt` (Bash) and `newfile1_methodX.txt` (Python methods 1, 2, and 3).
- Results include execution times for comparison and validation.

## License  
For educational use in CSU Global's CSC507 course.