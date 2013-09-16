# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Add operators here


class Operator(object):
    """
    Interface for operators.

    Operator must be only one char long.
    """
    sign = None

    def __init__(self):
        if not self.sign:
            raise Exception('Operator sign is missing.')
        if len(self.sign) != 1:
            raise Exception('Operator sign must be 1 char long.')
        try:
            float(self.sign)
            raise Exception('Operator cannot be a number.')
        except ValueError:
            pass

    def calculate(self, first_number, second_number):
        pass


class Add(Operator):
    """
    Operator responsible for adding
    """
    sign = '+'

    def calculate(self, first_number, second_number):
        """
        Return sum of two numbers.
        """
        return first_number + second_number


class Subtract(Operator):
    """
    Operator responsible for subtracting.
    """
    sign = '-'

    def calculate(self, first_number, second_number):
        """
        Return distinction of two numbers.
        """
        return first_number - second_number


class Multiple(Operator):
    """
    Operator responsible for multiplication.
    """
    sign = '*'

    def calculate(self, first_number, second_number):
        """
        Return product of two numbers.
        """
        return first_number * second_number


class Divide(Operator):
    """
    Operator responsible for dividing.
    """
    sign = '/'

    def calculate(self, first_number, second_number):
        """
        Return quotient of two numbers.
        """
        return first_number / second_number