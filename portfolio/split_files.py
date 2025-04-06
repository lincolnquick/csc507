def split_file(input_path, output_base, num_parts):
    import math

    # First pass: count total lines
    print(f"Counting lines in {input_path}...")
    with open(input_path, 'r') as infile:
        total_lines = sum(1 for _ in infile)

    lines_per_file = math.ceil(total_lines / num_parts)
    print(f"{total_lines} total lines, ~{lines_per_file} per file")

    with open(input_path, 'r') as infile:
        for part in range(1, num_parts + 1):
            output_path = f"{output_base}_part_{part}.txt"
            with open(output_path, 'w') as outfile:
                for _ in range(lines_per_file):
                    line = infile.readline()
                    if not line:
                        break
                    outfile.write(line)

    print(f"Finished splitting {input_path} into {num_parts} parts.")

if __name__ == "__main__":
    split_file("hugefile1.txt", "hugefile1", 10)
    split_file("hugefile2.txt", "hugefile2", 10)