# This file is part of TBD Calculator.
#
# TBD Calculator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TBD Calculator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TBD Calculator. If not, see <https://www.gnu.org/licenses/>.
"""
@file math_test.py
@brief TDD tests for the math library.

@author Tomáš Španka (xspankt00)
@date April 13, 2024

@note Python3 doesn't use fixed size integers (there's no intmax) thus we
      *shouldn't* have to test large values.

@example
python math_test.py
"""

from math import *
import unittest
import math_lib as m


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(m.add(1, 2), 3)
        self.assertEqual(m.add(1, -2), -1)
        self.assertEqual(m.add(-1, -2), -3)

    def test_add_float(self):
        self.assertAlmostEqual(m.add(0.1, 0.2), 0.3)
        self.assertAlmostEqual(m.add(0.1, -0.2), -0.1)
        self.assertAlmostEqual(m.add(-0.1, -0.2), -0.3)


class TestSubtract(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(m.subtract(3, 1), 2)
        self.assertEqual(m.subtract(-2, 1), -3)
        self.assertEqual(m.subtract(2, -1), 3)

    def test_subtract_float(self):
        self.assertAlmostEqual(m.subtract(0.3, 0.1), 0.2)
        self.assertAlmostEqual(m.subtract(-0.2, 0.1), -0.3)
        self.assertAlmostEqual(m.subtract(0.2, -0.1), 0.3)


class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(m.multiply(1, 3), 3)
        self.assertEqual(m.multiply(3, 3), 9)
        self.assertEqual(m.multiply(0, 3), 0)

    def test_multiply_float(self):
        self.assertEqual(m.multiply(0.1, 0.3), 0.03)
        self.assertAlmostEqual(m.multiply(3, 0.3), 0.9)
        self.assertEqual(m.multiply(0.3, 0.3), 0.09)
        self.assertEqual(m.multiply(0.0, 3.0), 0)


class TestDivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(m.divide(3, 1), 3)
        self.assertEqual(m.divide(9, 3), 3)
        self.assertEqual(m.divide(9, 3), 3)

        # Division by zero
        self.assertIsNone(m.divide(3, 0))

    def test_divide_float(self):
        self.assertAlmostEqual(m.divide(0.3, 0.1), 3)
        self.assertAlmostEqual(m.divide(0.9, 3), 0.3)
        self.assertAlmostEqual(m.divide(0.9, 0.3), 3)

        # Division by zero
        self.assertIsNone(m.divide(3.0, 0.0))


class TestPower(unittest.TestCase):
    # m.sqrt(radicand, radical)
    def test_power(self):
        self.assertEqual(m.power(3, 0), 1)
        self.assertEqual(m.power(3, 1), 3)
        self.assertEqual(m.power(3, 2), 9)
        self.assertEqual(m.power(2, 4), 16)

    def test_power_float(self):
        self.assertEqual(m.power(0.3, 0), 1)
        self.assertEqual(m.power(0.3, 1), 0.3)
        self.assertAlmostEqual(m.power(0.3, 2), 0.09)
        self.assertAlmostEqual(m.power(0.2, 4), 0.0016)
        self.assertEqual(m.power(3, 0.5), sqrt(3))


class TestSqrt(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(m.sqrt(9, 2), 3)
        self.assertEqual(m.sqrt(8, 3), 2)
        self.assertEqual(m.sqrt(16, 4), 2)
        self.assertEqual(m.sqrt(0, 2), 0)
        # Negative numbers are ok with radicals greater than 2
        self.assertEqual(m.sqrt(-1, 3), -1)
        self.assertEqual(m.sqrt(2, -1), 0.5)

        self.assertIsNone(m.sqrt(3, 0))
        

    def test_sqrt_float(self):
        self.assertAlmostEqual(m.sqrt(9.0, 2), 3)
        self.assertAlmostEqual(m.sqrt(9.0, 2), 3)
        self.assertAlmostEqual(m.sqrt(8.0, 3), 2)
        self.assertAlmostEqual(m.sqrt(6.25, 2), 2.5)


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(m.factorial(1), 1)
        self.assertEqual(m.factorial(3), 6)

        self.assertIsNone(m.factorial(-1))

    def test_factorial_float(self):
        self.assertIsNone(m.factorial(0.1))
        self.assertIsNone(m.factorial(-0.1))


unittest.main()

# ********************     end of math_test.py file     ********************