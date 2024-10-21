#!/usr/bin/env python
"""
@file stddev.py
@brief Standard deviation script

This program calculates the standard deviation of a set of numbers provided
in stdin. The numbers should be separated by spaces.

The program is used for performance analysis. The calculations are done using
functions from the math_lib library.

You can use the 'generate.py' script to generate a set of random numbers
for this program.
@file generate.py

@author Tomáš Španka (xspankt00)
@date April 13, 2024

@example
python stddev.py < data.txt
"""

from sys import path
path.append('../src/')
import math_lib as m

@profile
def standard_deviation():

    x = [int(i) for i in input().split()]
    N = len(x)

    mean = m.divide(1, N)
    mean = m.multiply(mean, sum(x))

    s = sum([m.power(x[i], 2) for i in range(0, N)])
    tmp = m.power(mean, 2)
    tmp = m.multiply(N, tmp)
    s = m.subtract(s, tmp)
    tmp = (m.multiply(m.divide(1, m.subtract(N, 1)), s))
    s = m.sqrt(tmp, 2)

    print(s)

if __name__ == '__main__':
    standard_deviation()
# ******************** end of profiling.py file *************************
