#!/bin/python

import sys

"""
https://www.hackerrank.com/challenges/gem-stones
"""

def main():
    T = int(raw_input().strip())
    S = raw_input().strip()
    for i in range(T-1):
        T = raw_input().strip()
        S = [val for val in T if val in S]
    print "{}".format(len(set(S)))


if __name__ == '__main__':
    main()