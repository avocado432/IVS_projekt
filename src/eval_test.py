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
@file eval_test.py
@brief Tests for expression evaluation implemented in the math library.

@author Tomáš Španka (xspankt00)
@date April 14, 2024

@example
python eval_test.py
"""

import unittest
import math_lib as m

# Custom test case
class EvalTestCase(unittest.TestCase):
    def assertExprEquals(self, expression, expected_result):
        self.assertEqual(m.evaluate_expression(expression), expected_result)

    def assertExprAlmostEquals(self, expression, expected_result):
        self.assertAlmostEqual(m.evaluate_expression(expression), expected_result)

    def assertExprIsNone(self, expression):
        self.assertIsNone(m.evaluate_expression(expression))

class TestOperations(EvalTestCase):
    def test_add(self):
        self.assertExprEquals("1+2", 3)
        self.assertExprEquals("-1+2", 1)
        # Only one operand
        self.assertExprIsNone("1+")
        self.assertExprIsNone("+1")
        self.assertExprIsNone("-1+")
        

    def test_add_float(self):
        self.assertExprAlmostEquals("1.2+2.3", 3.5)
        self.assertExprAlmostEquals("-1.5+2.2", 0.7)
        # Invalid float
        #self.assertExprIsNone("1.+2")
        #self.assertExprIsNone("1+2.")
        #self.assertExprIsNone("1.+2.")
        # Only one operand
        self.assertExprIsNone("1.5+")
        self.assertExprIsNone("+1.5")
        self.assertExprIsNone("-1.5+")
        # One operand & invalid float
        self.assertExprIsNone("1.+")
        self.assertExprIsNone("-1.+")


    def test_subtract(self):
        self.assertExprEquals("2-1", 1)
        self.assertExprEquals("-1-2", -3)
        # Only one operand
        self.assertExprIsNone("1-")
        self.assertExprIsNone("-1-")
        

    def test_subtract_float(self):
        self.assertExprAlmostEquals("2.5-1.2", 1.3)
        self.assertExprAlmostEquals("-1.5-0.5", -2.0)
        # Invalid float
        #self.assertExprIsNone("1.-2")
        #self.assertExprIsNone("1-2.")
        #self.assertExprIsNone("1.-2.")
        # Only one operand
        self.assertExprIsNone("1.5-")
        self.assertExprIsNone("-1.5-")
        # One operand & invalid float
        self.assertExprIsNone("1-")
        self.assertExprIsNone("-1.-")


    def test_multiply(self):
        self.assertExprEquals("2*2", 4)
        self.assertExprEquals("-2*2", -4)
        self.assertExprEquals("2*-2", -4)
        self.assertExprEquals("-2*-2", 4)
        # Only one operand
        self.assertExprIsNone("1*")
        self.assertExprIsNone("*1")
        self.assertExprIsNone("-1*")
        

    def test_multiply_float(self):
        self.assertExprAlmostEquals("1.5*1.5", 2.25)
        self.assertExprAlmostEquals("-1.5*1.5", -2.25)
        self.assertExprAlmostEquals("1.5*-1.5", -2.25)
        self.assertExprAlmostEquals("-1.5*-1.5", 2.25)
        # Invalid float
        #self.assertExprIsNone("1.*2")
        #self.assertExprIsNone("1*2.")
        #self.assertExprIsNone("1.*2.")
        # Only one operand
        self.assertExprIsNone("1.5*")
        self.assertExprIsNone("*1.5")
        self.assertExprIsNone("-1.5*")
        # One operand & invalid float
        self.assertExprIsNone("1.*")
        self.assertExprIsNone("-1.*")
        

    def test_divide(self):
        self.assertExprEquals("4/2", 2)
        self.assertExprEquals("-4/2", -2)
        self.assertExprEquals("4/-2", -2)
        self.assertExprEquals("-4/-2", 2)
        # Only one operand
        self.assertExprIsNone("1/")
        self.assertExprIsNone("/1")
        self.assertExprIsNone("-1/")
        

    def test_divide_float(self):
        self.assertExprAlmostEquals("2.25/1.5", 1.5)
        self.assertExprAlmostEquals("-2.25/1.5", -1.5)
        self.assertExprAlmostEquals("2.25/-1.5", -1.5)
        self.assertExprAlmostEquals("-2.25/-1.5", 1.5)
        # Invalid float
        #self.assertExprIsNone("1./2")
        #self.assertExprIsNone("1/2.")
        #self.assertExprIsNone("1./2.")
        # Only one operand
        self.assertExprIsNone("1.5/")
        self.assertExprIsNone("/1.5")
        self.assertExprIsNone("-1.5/")
        # One operand & invalid float
        self.assertExprIsNone("1./")
        self.assertExprIsNone("-1./")

    def test_single_number(self):
        self.assertExprEquals("1", 1)
        self.assertExprEquals("-1", -1)
        self.assertExprAlmostEquals("1.5", 1.5)
        self.assertExprAlmostEquals("-1.5", -1.5)
        # Invalid float
        #self.assertExprIsNone("1.")
        #self.assertExprIsNone("1.5.")
        #self.assertExprIsNone("-1.")
        #self.assertExprIsNone("-1.5.")
        self.assertExprIsNone("")
        self.assertExprIsNone("   ")

class TestPemdas(EvalTestCase):
    pass

class TestBrackets(unittest.TestCase):
    pass

unittest.main()