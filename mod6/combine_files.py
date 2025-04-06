import sys

def combine_files(num_parts, final_output):
    with open(final_output, 'w') as outfile:
        for i in range(num_parts):
            part_file = f'newfile_part_{i + 1}.txt'
            with open(part_file, 'r') as infile:
                outfile.writelines(infile.readlines())
    
    print(f"Combined {num_parts} files into {final_output}.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_parts = int(sys.argv[1])
    else:
        num_parts = 10
    combine_files(num_parts, 'newfile1_combined.txt')



