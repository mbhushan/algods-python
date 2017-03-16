#!/bin/python

import sys

"""
https://www.hackerrank.com/challenges/weighted-uniform-string
"""


def factors(n):
    """
    Returns the factors of a number n
    :param n:
    :return: a list of factors
    """
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def check_weight(s, x):
    fs = factors(x)
    i, j = 0, len(fs)-1


def main():
    s = raw_input().strip()
    n = int(raw_input().strip())
    for a0 in xrange(n):
        x = int(raw_input().strip())

if __name__ == '__main__':
    main()
