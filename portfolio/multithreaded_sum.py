import threading
import time
import os

OUTPUT_BASE = "chunk_output"
BUFFER_SIZE = 10000  # number of lines to process in one batch

def count_lines(file_path):
    with open(file_path, 'r') as f:
        return sum(1 for _ in f)

def process_chunk(file1_path, file2_path, start_line, num_lines, thread_id):
    output_file = f"{OUTPUT_BASE}_{thread_id}.txt"

    with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
        for _ in range(start_line):
            f1.readline()
            f2.readline()

        with open(output_file, 'w') as out:
            buffer = []
            lines_processed = 0

            while lines_processed < num_lines:
                batch_size = min(BUFFER_SIZE, num_lines - lines_processed)
                lines1 = [f1.readline() for _ in range(batch_size)]
                lines2 = [f2.readline() for _ in range(batch_size)]

                for l1, l2 in zip(lines1, lines2):
                    try:
                        total = int(l1.strip()) + int(l2.strip())
                        buffer.append(f"{total}\n")
                    except ValueError:
                        continue

                out.writelines(buffer)
                buffer.clear()
                lines_processed += batch_size

def merge_chunks(output_file, num_chunks):
    with open(output_file, 'w') as outfile:
        for i in range(num_chunks):
            chunk_file = f"{OUTPUT_BASE}_{i}.txt"
            with open(chunk_file, 'r') as infile:
                for line in infile:
                    outfile.write(line)
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

    threads = []
    for i in range(num_threads):
        start_line = i * chunk_size
        lines_for_thread = chunk_size if i < num_threads - 1 else total_lines - start_line

        t = threading.Thread(
            target=process_chunk,
            args=(file1_path, file2_path, start_line, lines_for_thread, i)
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    merge_chunks(output_path, num_threads)
    elapsed = time.time() - start_time
    print(f"Multithreaded sum completed in {elapsed:.2f} seconds")
    return elapsed

if __name__ == "__main__":
    add_files_multithreaded("hugefile1.txt", "hugefile2.txt", "totalfile.txt")