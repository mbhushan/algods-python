#!/bin/python

import sys

"""
 https://www.hackerrank.com/challenges/apple-and-orange
"""


def main():
    s, t = raw_input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = raw_input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = raw_input().strip().split(' ')
    m, n = [int(m), int(n)]
    apples = map(int, raw_input().strip().split(' '))
    oranges = map(int, raw_input().strip().split(' '))

    apple_op, orange_op = 0, 0
    for app in apples:
        x = app + a
        if x >= s and x <= t:
            apple_op += 1
    for orng in oranges:
        x = orng + b
        if x >= s and x <= t:
            orange_op += 1
    print str(apple_op)
    print str(orange_op)


if __name__ == '__main__':
    main()