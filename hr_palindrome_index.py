#!/usr/bin/python

import sys

"""
https://www.hackerrank.com/challenges/palindrome-index

quyjjdcgsvvsgcdjjyq

"""


def check_palindrome(S, i, j):
    while i < j:
        if S[i] != S[j]:
            return False
        i += 1
        j -= 1
    return True

def main():
    T = int(raw_input().strip())
    for i in range(T):
        index = -1
        S = raw_input().strip()
        low = 0
        high = len(S) - 1
        while low <= high:
            if S[low] != S[high]:
                index = low if check_palindrome(S, low+1, high) else high
                break
            low += 1
            high -= 1

        print "{}".format(index)



if __name__ == '__main__':
    main()