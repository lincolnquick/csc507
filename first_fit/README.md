# First-Fit and Best-Fit Memory Allocation Simulation  
**Author:** Lincoln Quick  
**Course:** CSC507 – Foundations of Operating Systems  
**Instructor:** Dr. Jessica Schwartz  
**Date:** March 9, 2025  

## Overview  
This project simulates two classic memory allocation algorithms used in operating systems:  
- **First-Fit**: Allocates the first available memory block large enough to accommodate a process.  
- **Best-Fit**: Allocates the smallest available memory block that is large enough to accommodate a process.  

The simulation was developed in Python and demonstrates how each algorithm allocates memory blocks to processes of varying sizes. The program compares the results of First-Fit and Best-Fit using a sample dataset.

## Assignment Description  
**Critical Thinking Assignment (75 Points):**  
Simulate the First-Fit algorithm in allocating memory to processes. Test the algorithm with varying memory block sizes and process sizes. Compare the results with the Best-Fit algorithm and analyze situations where Best-Fit may be preferable.

## Files Included  
- `memory_allocation_simulation.py`: Python script implementing both First-Fit and Best-Fit algorithms.
- Screenshots: Demonstrate program execution and output (included in submission but not in this repo).
- Paper (separate document in submission): Explains the algorithms, includes comparisons, and cites references.

## Sample Input  
- Memory Blocks: `[100, 400, 300, 700, 900, 200]`  
- Process Sizes: `[214, 426, 507, 909, 300, 999]`  

## Sample Output  
```
=== First-Fit Allocation ===
Process No.     Process Size    Block No.
1               214             2
2               426             4
3               507             5
4               909             Not Allocated
5               300             3
6               999             Not Allocated

=== Best-Fit Allocation ===
Process No.     Process Size    Block No.
1               214             3
2               426             4
3               507             5
4               909             Not Allocated
5               300             5
6               999             Not Allocated
```

## How to Run the Program  
1. Ensure you have Python 3 installed.  
2. Run the script:  ```python3 memory_allocation_simulation.py```

## Purpose  
This simulation demonstrates the differences in allocation behavior between First-Fit and Best-Fit algorithms. It highlights the trade-offs between speed (First-Fit) and memory utilization efficiency (Best-Fit).

## License  
For educational use in CSU Global's CSC507 course.