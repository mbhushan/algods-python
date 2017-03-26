#!/usr/bin/python

import sys

"""
https://www.hackerrank.com/challenges/palindrome-index

quyjjdcgsvvsgcdjjyq

"""


def main():
    T = int(raw_input().strip())
    for i in range(T):
        index = -1
        S = raw_input().strip()
        low = 0
        high = len(S) - 1
        while low <= high:
            if S[low] != S[high]:
                index = high if S[low] == S[high-1] else low
                break
            low += 1
            high -= 1

        print "{}".format(index)


if __name__ == '__main__':
    main()