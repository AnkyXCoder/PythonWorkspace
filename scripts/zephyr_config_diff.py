import sys
import shutil

def read_lines(filename):
    """ Read Lines from file """
    with open(filename, 'r') as file:
        return set(line for line in file.readlines() if not line.startswith("#"))

def update_input_file(input_filename, reference_filename):
    """ Update Input file """
    input_lines = read_lines(input_filename)
    reference_lines = read_lines(reference_filename)
    common_lines = input_lines.intersection(reference_lines)

    updated_input_lines = input_lines.difference(common_lines)
    updated_reference_lines = reference_lines.difference(common_lines)

    with open(input_filename, 'w') as file:
        file.writelines(updated_input_lines)

    with open(reference_filename, 'w') as file:
        file.writelines(updated_reference_lines)

def main():
    """ Main function """
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <reference_file>")
        sys.exit(1)

    input_filename = sys.argv[1]
    reference_filename = sys.argv[2]

    try:
        shutil.copyfile(input_filename, "input.txt")
        shutil.copyfile(reference_filename, "reference.txt")
    except IOError as e:
        print(f"Error: {e}")
        sys.exit(1)

    update_input_file("input.txt", "reference.txt")

if __name__ == "__main__":
    main()
