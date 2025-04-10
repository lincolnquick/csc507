import sys

def split_file(input_file, num_parts):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
        
    total_lines = len(lines)
    chunk_size = total_lines // num_parts
    remainder = total_lines % num_parts
    
    for i in range(num_parts):
        part_lines = lines[i * chunk_size : (i+1) * chunk_size]
        if i == num_parts - 1:
            part_lines += lines[-remainder:]
            
        with open(f'file_part_{i + 1}.txt', 'w') as part_file:
            part_file.writelines(part_lines)
        
    print(f"Split {total_lines} lines into {num_parts} files.")
        
if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("Usage: python split_file.py <input_file> <num_parts>")
        sys.exit(1)
    input_file = sys.argv[1]
    num_parts = int(sys.argv[2])

    split_file(input_file, num_parts)

