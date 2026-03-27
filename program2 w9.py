"""
Author: Abrielle Nyei
Date: 2026-03-26
Program: Random Number File Writer
Description: Writes user-specified amount of random numbers (1–500) to a file
"""

import random

def write_random_numbers(filename, amount):
    try:
        with open(filename, 'w') as file:
            for _ in range(amount):
                number = random.randint(1, 500)
                file.write(f"{number}\n")
        print(f"{amount} random numbers written to '{filename}'.")
    except IOError:
        print("Error: Could not write to the file.")


def main():
    try:
        amount = int(input("How many random numbers would you like to generate (1–1000)? "))

        if 1 <= amount <= 1000:
            write_random_numbers("random_numbers.txt", amount)
        else:
            print("Error: Please enter a number between 1 and 1000.")

    except ValueError:
        print("Error: Please enter a valid integer.")


if __name__ == "__main__":
    main()