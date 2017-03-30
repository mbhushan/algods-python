#!/usr/bin/python

import sys

"""
https://www.hackerrank.com/challenges/anagram
"""


def get_changes_req(S):
    n = len(S)
    mid = n / 2
    low = S[0:mid]
    high = S[mid:n]
    freq = {}
    result = mid
    for i in low:
        count = 0
        if i in freq:
            count = freq[i]
        freq[i] = count + 1
    for j in high:
        if j in freq:
            count = freq[j]
            if count == 1:
                del freq[j]
            else:
                freq[j] = count-1
            result = result - 1
    print str(result)


def main():
    T = int(raw_input().strip())
    for i in range(T):
        S = raw_input().strip()
        n = len(S)
        if n % 2 == 1:
            print "-1"
        x = get_changes_req(S)

if __name__ == '__main__':
    main()
