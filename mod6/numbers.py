# This Python script generates 1000000 random numbers (0 - 32767, same as $RANDOM)
# and stores them in file2.txt. It also captures the elapsed time in seconds. 
# This script includes alternate implementations to improve execution time: 
# multithreading and multiprocessing.

import time
import sys
import random
import io
import multiprocessing

# Generate random numbers
def generate_numbers_chunk(count):
    return [str(random.randint(0, 32767)) + "\n" for _ in range(count)]

def generate_numbers_single_threaded(filename, count):
    start_time = time.time()
    
    with open(filename, "w", buffering=io.DEFAULT_BUFFER_SIZE) as f:
        for _ in range(count):
            f.write(str(random.randint(0, 32767)) + "\n")
    return time.time() - start_time

def generate_numbers_multithreaded(filename, count, num_threads):
    import threading
    
    start_time = time.time()
    
    chunk_size = count // num_threads
    results = []
    threads = []
    
    def worker():
        results.append([str(random.randint(0, 32767)) + "\n" for _ in range(chunk_size)])
    
    for _ in range(num_threads):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    with open(filename, "w", buffering=io.DEFAULT_BUFFER_SIZE) as f:
        for chunk in results:
            f.writelines(chunk)
    
    return time.time() - start_time
    
def generate_numbers_parallel(filename, count, num_processes):
    start_time = time.time()
    
    chunk_size = count // num_processes
    
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(generate_numbers_chunk, [chunk_size] * num_processes)
    
    with open(filename, "w", buffering=io.DEFAULT_BUFFER_SIZE) as f:
        for chunk in results:
            f.writelines(chunk)
    
    return time.time() - start_time


# Run all methods, record run times
if __name__ == "__main__":
    filename_single = "file2_single.txt"
    filename_multi = "file2_threaded.txt"
    filename_parallel = "file2_parallel.txt"
    
    # Default values
    count = 1_000_000
    num_threads = 2
    num_processes = 2
    
    # Accept an optional argument for count
    if len(sys.argv) > 1:
        print(f"Using provided count for random number generation: {sys.argv[1]}")
        count = int(sys.argv[1])
    
    print("Running random number generation tests...")
    
    #time_single = generate_numbers_single_threaded(filename_single, count)
    #print(f"Single-threaded execution time: {time_single:.4f} seconds")
    
    #time_multi = generate_numbers_multithreaded(filename_multi, count, num_threads)
    #print(f"Multi-threaded execution time: {time_multi:.4f} seconds")
    
    time_parallel = generate_numbers_parallel(filename_parallel, count, num_processes)
    print(f"Multi-processing execution time: {time_parallel:.4f} seconds")

