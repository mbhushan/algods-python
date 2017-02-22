#!/bin/python

"""
https://www.hackerrank.com/challenges/mini-max-sum
"""

import sys


def main():
    a, b, c, d, e = raw_input().strip().split(' ')
    arr = [int(a), int(b), int(c), int(d), int(e)]
    min = sys.maxint
    max = -1 * (sys.maxint)
    sum = 0
    for i in arr:
        if i > max:
            max = i
        if i < min:
            min = i
        sum += i
    min_sum = sum - max
    max_sum = sum - min

    print "{} {}".format(min_sum, max_sum)


if __name__ == '__main__':
    main()

