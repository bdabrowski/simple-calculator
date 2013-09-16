# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from parser import Parser
from operators import Operator


class TestParser(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_add_operator(self):

        class Power(Operator):
            sign = '^'

            def calculate(self, first_number, second_number):
                return first_number ** second_number

        parser = Parser()
        parser.add_operator(Power())
        parser.open('2 + 2 - 2 * 2 / 2 ^ 2')
        parser.read()

        self.assertEqual(parser.compute(), 4)

    def compute_1(self):
        parser = Parser()
        parser.open('-1111112 + 2.11 - 2.32 * 200')
        parser.read()

        self.assertEqual(parser.compute(), -1111573.89)

    def compute_2(self):
        parser = Parser()
        parser.open('+ 2.11 - 2.32 * 200')

        self.assertRaises(AttributeError, parser.read, ())

    def test_is_number(self):
        parser = Parser()

        self.assertTrue(parser.is_number('7'))
        self.assertTrue(parser.is_number('1.7'))
        self.assertTrue(parser.is_number('-700000'))
        self.assertFalse(parser.is_number(','))
        self.assertFalse(parser.is_number('+'))
        self.assertFalse(parser.is_number('asdfsd'))

    def test_is_operator(self):
        parser = Parser()
        self.assertTrue(parser.is_operator('*'))
        self.assertTrue(parser.is_operator('-'))
        self.assertTrue(parser.is_operator('+'))
        self.assertFalse(parser.is_operator('+7'))
        self.assertFalse(parser.is_operator('a'))
        self.assertFalse(parser.is_operator('asdfsd'))

    def test_group_operations(self):
        parser = Parser()
        groups = parser.group_operations(['1', '+', '2', '-', '3', '*', '4',
                                          '/', '5', '+', '6'])
        self.assertEqual(groups, ['1', ['+', '2'], ['-', '3'], ['*', '4'],
                                  ['/', '5'], ['+', '6']])

if __name__ == '__main__':
    unittest.main()