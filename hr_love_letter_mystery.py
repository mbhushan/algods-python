#!/usr/bin/env python2.7

import sys
import math

"""
https://www.hackerrank.com/challenges/the-love-letter-mystery
"""


def main():
    T = int(raw_input().strip())
    for i in range(T):
        S = raw_input().strip()
        value = 0
        j = 0
        k = len(S) - 1
        while (j < k):
            value += abs(ord(S[j]) - ord(S[k]))
            j = j + 1
            k = k - 1
        print value




if __name__ == '__main__':
    main()