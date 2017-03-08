#!/usr/bin/python

import sys

"""
https://www.hackerrank.com/challenges/funny-string
"""

def main():
    T = int(raw_input().strip())
    for i in range(T):
        S = raw_input().strip()
        R = S[::-1]
        funny = True
        n = len(S)
        for j in range(1, n):
            if abs(ord(S[j]) - ord(S[j-1])) != abs(ord(R[j]) - ord(R[j-1])):
                funny = False
                break
        if funny:
            print "Funny"
        else:
            print "Not Funny"


if __name__ == '__main__':
    main()
