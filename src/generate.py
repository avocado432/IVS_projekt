#!/usr/bin/env python
"""
@file generate.py
@brief Script for generating a list of random numbers

Generates a list of specified length containing numbers of specified size.
The list is printed on stdout as a space-separated string, to ensure
compatability with stddev.py.

@file stddev.py

@author Tomáš Španka (xspankt00)
@date April 14, 2024

@example
# Generate a list of 5 numbers from the interval <-10,10>
./generate.py -c 5 -s 4

# Generate a list of numbers and pipe it into stddev.py
./generate.py | ./stddev.py

# Generate a list of numbers and pipe it into stddev.py,\
print the generated numbers
./generate.py -l | ./stddev.py
"""

import argparse
from random import randint
from sys import stderr

# ============ [ Parse args ] ============
parser = argparse.ArgumentParser(description='Generate list of random numbers')
parser.add_argument('-c', type=int, help='Number count (default: 10)')
parser.add_argument('-s', type=int, help='Number size (default: 2) - example:\
                     -s 2 = <-10, 10>')
parser.add_argument('-l', action='store_true', help='List generated numbers\
                    in stderr (useful when piping)')

args = parser.parse_args()

count = args.c if args.c is not None else 10
size = args.s if args.s is not None else 2

# ========= [ Generate numbers ] =========
int_start = -10 ** (size-1)
int_end = 10 ** (size-1)

# Generate the numbers and convert them into a space separated string
numbers = ' '.join([str(randint(int_start, int_end)) for _ in range(count)])

# Print to stderr to allow piping the numbers
stderr.write(f"generate.py: Generating {count} numbers ranging from "
             f"{int_start} to {int_end}...\n")
stderr.write(numbers + "\n") if args.l else None

print(numbers)

# ******************** end of generate.py file *************************
