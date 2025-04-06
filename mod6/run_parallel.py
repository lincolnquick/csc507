import time
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

def process_file(part_num, batch_size=1000):
    """
    Processes a file part by reading numbers, doubling them, and writing the results.
    Uses buffered reading/writing with batching for efficiency.
    """
    input_file = f'file_part_{part_num}.txt'
    output_file = f'newfile_part_{part_num}.txt'

    try:
        with open(input_file, 'r', buffering=1024*1024) as infile, \
             open(output_file, 'w', buffering=1024*1024) as outfile:

            buffer = []
            for line in infile:
                number = int(line.strip())
                doubled = number * 2
                buffer.append(f"{doubled}\n")

                # Write in batches
                if len(buffer) >= batch_size:
                    outfile.writelines(buffer)
                    buffer.clear()

            # Write any remaining lines
            if buffer:
                outfile.writelines(buffer)

        # Optional debug
        # print(f"Finished processing {input_file}")

    except Exception as e:
        print(f"Error processing {input_file}: {e}")

def run_parallel_threads(num_parts, max_workers=None):
    """
    Runs parallel file processing using a ThreadPoolExecutor.
    Limits concurrent threads to max_workers if specified.
    """
    start_time = time.perf_counter()

    # If not specified, default to the number of CPU cores
    if not max_workers:
        import multiprocessing
        max_workers = multiprocessing.cpu_count()

    print(f"Starting threaded processing with {max_workers} workers...")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_file, i + 1) for i in range(num_parts)]

        # Optional: wait for all futures to complete and handle exceptions
        for future in as_completed(futures):
            if future.exception() is not None:
                print(f"Thread raised an exception: {future.exception()}")

    end_time = time.perf_counter()
    total_time = end_time - start_time
    print(f"Threaded processing ({num_parts} parts, {max_workers} workers) completed in {total_time:.4f} seconds.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_parts = int(sys.argv[1])
    else:
        num_parts = 10  # default splits

    run_parallel_threads(num_parts, max_workers=8)  