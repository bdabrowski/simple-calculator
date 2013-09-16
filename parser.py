# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from operators import Add, Subtract, Multiple, Divide


class Operation(object):
    """
    Operation Builds structure of calculation.
    almost every operation has parent so the parent result is first argument
    in next operation.

    ((((((1) + 2) - 3) * 4) / 5) + 6)

    It is possible to order input before calculation so data will
    start with multiplications and divisions.
    """
    def __init__(self, number, operator=None, parent=None):
        self.operator = operator
        self.number = number
        self.parent = parent

    def compute(self):
        if self.parent:
            return self.operator.calculate(float(self.parent.compute()),
                                           float(self.number))
        else:
            return self.number


class Parser(object):
    """
    Parser extracts data from raw string. Using is similar to file interface.

        >>> parser = Parser()
        >>> parser.open('1 + 2 * 5')
        >>> parser.read()

    The instance creates nested Operation objects and provide method to
    run calculation and return result.

        >>> parser.compute()
        15

    """
    def __init__(self):
        """
        Initialize data and add operators.
        """
        self.operators = {}
        self.operation_data = None
        self.mathematical_operation = None
        self.result = 0

        self.add_operator(Add())
        self.add_operator(Subtract())
        self.add_operator(Multiple())
        self.add_operator(Divide())

    def add_operator(self, operator):
        """
        Add valid operator to parser.
        """
        if not operator.sign or operator.sign in self.operators:
            raise AttributeError('Operator %s is invalid.' % operator)

        self.operators[operator.sign] = operator

    def open(self, data):
        """
        Load data to parser.
        """
        data = data.strip()
        chars = data.split()
        self.operation_data = self.group_operations(chars)

    def read(self):
        """
        Read data and transform to objects.
        """
        if not self.operation_data:
            raise Exception('Cannot read without opened set of data.')
        # It is possible to order data here to allow
        # ordering by operator '*' or '/' then '+' or '-'.

        for operation_desc in self.operation_data:
            if not self.mathematical_operation:
                self.mathematical_operation = Operation(number=operation_desc)
            else:
                self.mathematical_operation = \
                    Operation(number=operation_desc[1],
                              operator=self.operators[operation_desc[0]],
                              parent=self.mathematical_operation)

    def compute(self):
        """
        return result of mathematical operation parsed from string previously.
        """
        if not self.mathematical_operation:
            raise Exception('Cannot compute without ready loaded operations.')
        return self.mathematical_operation.compute()

    def is_number(self, string):
        """
        Return True if given argument is valid number.
        """
        try:
            float(string)
            return True
        except ValueError:
            return False

    def is_operator(self, operator):
        """
        Return True if given argument is valid operator.
        """
        if operator in self.operators:
            return True
        else:
            return False

    def group_operations(self, chars):
        """
        :chars - List of chars in proper other. (number, sign, number, sign,
                 number etc).
        Return list of operations with number and operator sign. First item is
        only number next are list of two items. (number, [sign, number], [sign,
        number] etc.).
        """
        skip_next = None
        result = []
        for index, item in enumerate(chars):
            if not skip_next:
                if index == 0:
                    if not self.is_number(item):
                        raise AttributeError('Mathematical operation has '
                                             'invalid format at char number: %s' % index)
                    result.append(item)
                else:
                    if not self.is_number(chars[index + 1]):
                        raise AttributeError('Mathematical operation has '
                                             'invalid format at char number: %s' % index)
                    if not self.is_operator(item):
                        raise AttributeError('Mathematical operation has '
                                             'invalid format at char number: %s' % index)
                    try:
                        result.append([item, chars[index + 1]])
                    except IndexError:
                        raise AttributeError('Mathematical operation has invalid'
                                             'format at char number: %s' % index)
                    skip_next = True
            else:
                skip_next = False

        return result
