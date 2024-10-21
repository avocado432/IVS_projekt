#!/usr/bin/env python
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
@file math_lib.py

@brief Math library for school project - implementation of calculator.
@author Tereza Lapčíková (xlapci03)
@author Tereza Magerková (xmager00)
@author Tomáš Španka (xspankt00)
@date April 13, 2024

@example
python3 math_lib.py
"""
import re

def is_valid_type(*a):
    """
    @brief Check the types of given parameters.
    @param a One or more objects which type will be checked.
    @return True If all the parameters are of type int or float, otherwise False.
    """
    if len(a) == 1:
        if type(a[0]) == int or type(a[0]) == float:
            return True
        else:
            return False
    for t in a:
        return is_valid_type(t)

def add(a, b):
    """
    @brief Check the type of parameters and calculate their addition.
    @param a Augend
    @param b Addend
    @return a + b The result of the addition of parameters a and b.
    """
    if is_valid_type(a, b) == False:
        return None
    return round(a, 16) + round(b, 16)

def subtract(a, b):
    """
    @brief Check the type of parameters and calculate their subtraction.
    @param a Minuend
    @param b Subtrahend
    @return a - b The result of the subtraction of parameters a and b.
    """
    if is_valid_type(a, b) == False:
        return None
    return round(a, 16) - round(b, 16)

def multiply(a, b):
    """
    @brief Check the type of parameters and calculate their multiplication.
    @param a Multiplicand
    @param b Multiplier
    @return a * b The result of the multiplication of parameters a and b.
    """
    if is_valid_type(a, b) == False:
        return None
    return round(a, 16) * round(b, 16)

def divide(a, b):
    """
    @brief Check the type of parameters and calculate their division.
    @param a Dividend
    @param b Divisor
    @return a / b The result of the division of parameters a and b.
    """
    if is_valid_type(a) == False:
        return None
    if b == 0:
        return None
    return round(a, 16) / round(b, 16)

def factorial(number):
    """
    @brief Calculate the factorial of the input number.
    @param number The input number.
    @return result The factorial of input number.
    """
    result = 1
    if type(number) != int:
        return None
    if number < 0:
        return None
    elif number > 1:
        result = number * factorial(number - 1)
    return result

def power(number1, number2):
    """
    Calculate the power of a number.
    @param number1 The base number (the number being raised to a power).
    @param number2 The exponent number (the power to which the base is raised).
    @return 'number1' raised to the power of 'number2'.
    """
    return number1 ** number2

def sqrt(number1, number2):
    """
    @brief Calculates the nth root of a number
    @param number1 Radicand
    @param number2 Degree
    @return 'number2' root of 'number1'

    """
    negative = False
    if number1 == 0:
        return 0
    if number2 == 0:
        return None
    #negative degree must be a whole number
    if number2 < 0 and not number2 % 1 == 0:
        return None
    #for negative radicand only odd whole number degree is defined
    if number1 < 0 and number2 % 2 != 1:
        return None
    if number1 < 0:
        number1 = -number1
        negative = True

    root = number1 ** (1 / number2)
    if negative:
        return -root
    else:
        return root


def precedence(operator):
    """
    @brief Evaluate precedence of the operator.
    @param operator The operator of given expression.
    @return number Evaluated operator precedence, where number in [0, 1, 2, 3]

    @cite Geeks for Geeks: Inspired by https://www.geeksforgeeks.org/expression-evaluation/
    """
    if operator == '+' or operator == '-':
        return 1
    if operator == '*' or operator == '/':
        return 2
    if operator == '!' or operator == '√' or operator == '^':
        return 3
    return 0

def apply_operator(a, b, operator):
    """
    @brief Apply operator on the input operands.
    @param a Left input operand (on the left side of the operand).
    @param b Right input operand.
    @operator Input operator
    @return operation Result of the operation with the input operands.
    
    @cite Geeks for Geeks: Inspired by https://www.geeksforgeeks.org/expression-evaluation/
    """
    if operator == '+': return add(a, b)
    if operator == '-': return subtract(a, b)
    if operator == '*': return multiply(a, b)
    if operator == '/': return divide(a, b)
    if operator == '!': return factorial(a)
    if operator == '√': return sqrt(b, a)
    if operator == '^': return pow(a, b)

def get_operands(operator, values_stack):
    """
    @brief Get operands of the operation from stack.
    @param operator The input operator.
    @param values_stack The stack with the operands.
    @operator Input operator
    @return value1, value2 The left operand of the operation, otherwise
    @return None
    
    @cite Geeks for Geeks: Inspired by https://www.geeksforgeeks.org/expression-evaluation/
    """
    if operator != '!':
        try:
            value2 = values_stack.pop()
        except IndexError:
            return None, None
    else:
        value2 = None
    try:
        value1 = values_stack.pop()
    except IndexError:
        return None, None

    return value1, value2

def replace_negatives(expression):
    """
    @brief Replace negative numbers with '0 - number'.
    @param expression The input mathematical expression.
    @return expression The edited mathematical expression.
    """
    pattern_start = r'^-(\d+(\.\d+)?|(\(([^)]+)\))?)'
    pattern_non_digit = r'(?<=\D)-(\d+(\.\d+)?|(\(([^)]+)\))?)'

    def replace_match(match):
        """
        @brief Replace patterns matching with regex with string '(0 + match)'.
        @param match matching pattern
        @return match_replace match edited to desired outcome
        """
        if match.start() > 0 and expression[match.start() - 1] == ')':
            return match.group()
        match_replace = '(0' + match.group() + ')'
        return match_replace
    
    expression = re.sub(pattern_start, replace_match, expression)
    expression = re.sub(pattern_non_digit, replace_match, expression)
    
    return expression

def evaluate_expression(expression):
    """
    @brief Evaluate the input expression.
    @param expression The input expression
    @return values_stack[-1] Result of the evaluated expression, otherwise
    @return None

    @cite Geeks for Geeks: Inspired by https://www.geeksforgeeks.org/expression-evaluation/
    """
    expression = expression.replace(" ", "")
    if len(expression) == 0:
        return None
    expression = replace_negatives(expression)
    values_stack = []
    operators_stack = []
    char = 0
    while char < len(expression):
        if expression[char] == ' ': #skip whitespace
            char += 1
            continue
        elif expression[char] == '(':
            operators_stack.append(expression[char])
        elif expression[char].isdigit():
            value = 0
            is_float = False
            decimal_count = 0
            while (char < len(expression) and (expression[char].isdigit() or expression[char] == '.')):
                if expression[char] == '.':
                    is_float = True
                    value = float(value)
                elif is_float == True:
                    decimal_count += 1
                    value = value + float(expression[char])/(10**(decimal_count))
                else:
                    value = (value * 10) + int(expression[char]) #combine the series of digits into a number
                char += 1
            values_stack.append(value)
            char -= 1
        elif expression[char] == ')':
            while len(operators_stack) != 0 and operators_stack[-1] != '(':
                try:
                    operator = operators_stack.pop()
                except IndexError:
                    return None
                value1, value2 = get_operands(operator, values_stack)
                if value1 == None:
                    return None
                res = apply_operator(value1, value2, operator)
                if(res == None):
                    return None
                else:
                    values_stack.append(apply_operator(value1, value2, operator))
            try:
                operators_stack.pop()
            except IndexError:
                return None
        else:
            while ((len(operators_stack) != 0) and (precedence(operators_stack[-1])) >= precedence(expression[char])):
                try:
                    operator = operators_stack.pop()
                except IndexError:
                    return None
                value1, value2 = get_operands(operator, values_stack)
                if value1 == None:
                    return None
                res = apply_operator(value1, value2, operator)
                if(res == None):
                    return None
                else:
                    values_stack.append(apply_operator(value1, value2, operator))
            operators_stack.append(expression[char])
        char += 1

    while len(operators_stack) != 0:
        try:
            operator = operators_stack.pop()
        except IndexError:
            return None
        value1, value2 = get_operands(operator, values_stack)
        if value1 == None:
            return None
        res = apply_operator(value1, value2, operator)
        if(res == None):
            return None
        else:
            values_stack.append(apply_operator(value1, value2, operator))
    
    return values_stack[-1]

#******************** end of math_lib.py file *************************