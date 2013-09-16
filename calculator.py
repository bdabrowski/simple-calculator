# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from argparse import ArgumentParser, SUPPRESS

from parser import Parser

version = '0.0.1'

description = """\
Simple Calculator.
"""

if __name__ == '__main__':
    parser = ArgumentParser(description='Calculate result of simple mathematical operations',
                            argument_default=SUPPRESS)
    parser.add_argument('--question',
                        help='String with operations to calculate. Note that '
                             'numbers like -7 will be -7 but numbers like +7 '
                             'will be 7. Use spaces to separate numbers from'
                             ' signs.')

    args = parser.parse_args()

    parser = Parser()
    parser.open(args.question)
    parser.read()

    print(parser.compute())

