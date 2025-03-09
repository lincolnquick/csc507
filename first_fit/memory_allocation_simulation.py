"""
memory_allocation_simulation.py

Lincoln Quick
CSC 507: Foundations of Operating Systems
CSU Global
Dr. Jessica Schwartz
Date: March 9, 2025


Memory Allocation Simulation using First-Fit and Best-Fit Algorithms

This script simulates the memory allocation process using First-Fit and Best-Fit algorithms.

The First-Fit algorithm allocates the first available memory block that is large enough to hold the process.

The Best-Fit algorithm allocates the smallest available memory block that is large enough to hold the process.

The simulation takes a list of available memory blocks and a list of process sizes as input and returns the allocation of processes to memory blocks.
"""

def first_fit(blocks, processes):
    """ 
    First-Fit Memory Allocation Algorithm
    
    Parameters:
    blocks (list): List of available memory blocks
    processes (list): List of process sizes
   
     Returns:
    list: List of block indices allocated to each process
    """

    allocation = [-1] * len(processes) # Track which block each process gets

    for pid, process_size in enumerate(processes):
        for bid, block_size in enumerate(blocks):
            if block_size >= process_size:
                allocation[pid] = bid # Allocate block bid to process pid
                blocks[bid] -= process_size # Reduce available size in block
                break # Move to next process
    return allocation

def best_fit(blocks, processes):
    """
    Best-Fit Memory Allocation Algorithm
    
    Parameters:
    blocks (list): List of available memory blocks
    processes (list): List of process sizes
       
     Returns:
     list: List of block indices allocated to each process
     """
    allocation = [-1] * len(processes) # Track which block each process gets

    for pid, process_size in enumerate(processes):
        best_idx = -1
        for bid, block_size in enumerate(blocks):
            if block_size >= process_size:
                if best_idx == -1 or block_size < blocks[best_idx]:
                    best_idx = bid
        
        if best_idx != -1:
            allocation[pid] = best_idx
            blocks[best_idx] -= process_size
    return allocation

def display_allocation(processes, allocation):
    """
    
    Display the allocation of processes to memory blocks
    
    Parameters:
    processes (list): List of process sizes
    allocation (list): List of block indices allocated to each process
    """

    print("Process No.\tProcess Size\tBlock No.")

    for pid, process_size in enumerate(processes):
        if allocation[pid] != -1:
            print(f"{pid+1}\t\t{process_size}\t\t{allocation[pid]+1}")
        else:
            print(f"{pid+1}\t\t{process_size}\t\tNot Allocated")

def main():
    """
    Main function to test the First-Fit and Best-Fit Memory Allocation Algorithms
    """
    # Sample data
    memory_blocks = [100, 400, 300, 700, 900, 200]
    process_sizes = [214, 426, 507, 909, 300, 999]

    print("=== First-Fit Allocation ===")
    first_fit_blocks = memory_blocks.copy()
    ff_allocation = first_fit(first_fit_blocks, process_sizes)
    display_allocation(process_sizes, ff_allocation)

    print("=== Best-Fit Allocation ===")
    best_fit_blocks = memory_blocks.copy()
    bf_allocation = best_fit(best_fit_blocks, process_sizes)
    display_allocation(process_sizes, bf_allocation)

if __name__ == "__main__":
    main()
