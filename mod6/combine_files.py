def combine_files(num_parts, final_output):
    with open(final_output, 'w') as outfile:
        for i in range(num_parts):
            part_file = f'newfile_part_{i + 1}.txt'
            with open(part_file, 'r') as infile:
                outfile.writelines(infile.readlines())
    
    print(f"Combined {num_parts} files into {final_output}.")

if __name__ == "__main__":
    combine_files(10, 'newfile1_combined.txt')



