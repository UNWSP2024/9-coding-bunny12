"""
Author: Abrielle Nyei
Date: 2026-03-26
Program: Item Counter
Description: Counts the number of names stored in names.txt
"""

def count_names(filename):
    try:
        with open(filename, 'r') as file:
            count = 0
            for line in file:
                if line.strip():  # Ignore blank lines
                    count += 1
            return count
    except IOError:
        print("Error: Could not read the file.")
        return None


def main():
    filename = "names.txt"
    total_names = count_names(filename)

    if total_names is not None:
        print(f"Total number of names in '{filename}': {total_names}")


if __name__ == "__main__":
    main()