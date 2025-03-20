import time
import multiprocessing

def process_file(part_num):
    input_file = f'file_part_{part_num}.txt'
    output_file = f'newfile_part_{part_num}.txt'
    
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            number = int(line.strip())
            doubled = number * 2
            outfile.write(f"{doubled}\n")
    
    print(f"Finished processing {input_file}.")
    
    def run_parallel(num_parts):
        start_time = time.perf_counter()
        
        processes = []
        
        for i in range(num_parts):
            p = multiprocessing.Process(target=process_file, args=(i + 1,))
            processes.append(p)
            p.start()
        
        for p in processes:
            p.join()
        
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"Parallel processing ({num_parts} parts) completed in {total_time:.4f} seconds.")
        
if __name__ == "__main__":
    run_parallel(10)
