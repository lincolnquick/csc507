import os
import time
import io
from concurrent.futures import ThreadPoolExecutor

OUTPUT_BASE = "chunk_output"

def count_lines(file_path):
    with open(file_path, 'r') as f:
        return sum(1 for _ in f)

def process_chunk(file1_path, file2_path, start_line, num_lines, thread_id):
    output_file = f"{OUTPUT_BASE}_{thread_id}.txt"

    with open(file1_path, 'r', buffering=io.DEFAULT_BUFFER_SIZE) as f1, \
         open(file2_path, 'r', buffering=io.DEFAULT_BUFFER_SIZE) as f2:

        # Skip lines up to the chunk start
        for _ in range(start_line):
            f1.readline()
            f2.readline()

        with open(output_file, 'w', buffering=io.DEFAULT_BUFFER_SIZE) as out:
            for _ in range(num_lines):
                line1 = f1.readline()
                line2 = f2.readline()
                if not line1 or not line2:
                    break
                try:
                    num1 = int(line1.strip())
                    num2 = int(line2.strip())
                    out.write(f"{num1 + num2}\n")
                except ValueError:
                    continue

def merge_chunks(output_file, num_chunks):
    with open(output_file, 'w', buffering=io.DEFAULT_BUFFER_SIZE) as outfile:
        for i in range(num_chunks):
            chunk_file = f"{OUTPUT_BASE}_{i}.txt"
            with open(chunk_file, 'r', buffering=io.DEFAULT_BUFFER_SIZE) as infile:
                outfile.writelines(infile)
            os.remove(chunk_file)

def add_files_multithreaded(file1_path, file2_path, output_path, total_lines=None):
    start_time = time.time()

    if total_lines is None:
        print("Counting total lines in input file...")
        total_lines = count_lines(file1_path)

    num_threads = os.cpu_count() or 4
    chunk_size = total_lines // num_threads

    print(f"Total lines: {total_lines}")
    print(f"Using {num_threads} threads with {chunk_size} lines each.")

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for i in range(num_threads):
            start_line = i * chunk_size
            lines_for_thread = chunk_size if i < num_threads - 1 else total_lines - start_line

            futures.append(
                executor.submit(
                    process_chunk,
                    file1_path,
                    file2_path,
                    start_line,
                    lines_for_thread,
                    i
                )
            )

        # Wait for all threads to complete
        for future in futures:
            future.result()

    merge_chunks(output_path, num_threads)
    elapsed = time.time() - start_time
    print(f"Multithreaded sum completed in {elapsed:.2f} seconds")
    return elapsed

if __name__ == "__main__":
    add_files_multithreaded("hugefile1.txt", "hugefile2.txt", "totalfile.txt")