"""
Author: Abrielle Nyei
Date: 2026-03-26
Program: Average Numbers
Description: Reads integers from numbers.txt and calculates their total
"""

def calculate_total(filename):
    total = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    number = int(line.strip())
                    total += number
                except ValueError:
                    print(f"Warning: Skipping invalid value '{line.strip()}'")

        return total

    except IOError:
        print("Error: Could not read the file.")
        return None


def main():
    filename = "numbers.txt"
    total = calculate_total(filename)

    if total is not None:
        print(f"Total of all numbers in '{filename}': {total}")


if __name__ == "__main__":
    main()