#!/bin/python

import sys

"""
https://www.hackerrank.com/challenges/designer-pdf-viewer
"""


def main():
    h = map(int, raw_input().strip().split(' '))
    word = raw_input().strip()
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    max_ht = -1 * sys.maxint
    for s in word:
        index = alphabets.index(s)
        ht = h[index]
        if ht > max_ht:
            max_ht = ht
    result = len(word) * max_ht
    print result


if __name__ == '__main__':
    main()