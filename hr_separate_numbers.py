#!/bin/python

import sys

"""
https://www.hackerrank.com/challenges/separate-the-numbers
"""


def separate_numbers(s):
    print str(s)
    pass


def main():
    q = int(raw_input().strip())
    for a0 in xrange(q):
        s = raw_input().strip()
        separate_numbers(s)

if __name__ == '__main__':
    main()