import time
import os
import sys

def check_input_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: '{file_path}' not found. Exiting.")
        sys.exit(1)


def method1_read_all():
    input_file = "file1.txt"
    output_file = "newfile1_all.txt"
    
    check_input_file(input_file)
    
    start = time.time()
    
    with open(input_file, 'r') as f:
        numbers = f.readlines()
        
    doubled_numbers = [str(int(num.strip()) * 2) for num in numbers]
    
    with open(output_file, 'w') as f:
        f.write('\n'.join(doubled_numbers) + "\n")
    
    end = time.time()
    print(f"Method 1 (Read all at once): {end - start:.4f} seconds.")
    
def method2_read_line_by_line():
    input_file = "file1.txt"
    output_file = "newfile1_line_by_line.txt"
    
    check_input_file(input_file)
    
    start = time.time()
    
    with open(input_file, 'r') as infile, open(output_file, "w") as outfile:
        for line in infile:
            number = int(line.strip()) * 2
            outfile.write(f"{number}\n")
    
    end = time.time()
    print(f"Method 2 (Read line by line): {end - start:.4f} seconds.")
    
def method3_split_in_two():
    input_file = "file1.txt"
    output_file = "newfile1_split.txt"
    
    check_input_file(input_file)
    
    start = time.time()
    
    with open(input_file, "r") as f:
        numbers = f.readlines()
    
    mid_index = len(numbers) // 2
    first_half = numbers[:mid_index]
    second_half = numbers[mid_index:]
    
    doubled_numbers_first = [str(int(num.strip()) * 2) for num in first_half]
    doubled_numbers_second = [str(int(num.strip()) * 2) for num in second_half]
    
    with open(output_file, "w") as f:
        f.write("\n".join(doubled_numbers_first) + "\n")
        f.write("\n".join(doubled_numbers_second) + "\n")
    
    end = time.time()
    print(f"Method 3 (Split in two): {end - start:.4f} seconds.")
    
def run_all():
    method1_read_all()
    method2_read_line_by_line()
    method3_split_in_two()
    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_all()
    else:
        method2_read_line_by_line()  # Default to method 2 if no argument provided

