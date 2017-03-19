#!/bin/python 2.7

import sys

"""
https://www.hackerrank.com/challenges/caesar-cipher-1
"""

def encrypt(s, k):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    new_alph = list(alphabets)
    for ch in alphabets:
        old_index = alphabets.index(ch)
        index = alphabets.index(ch) + 1 + k
        if index > 26:
            index = index % 26
        new_alph[old_index] = alphabets[index-1]
    # print "new order: " + ''.join(new_alph)
    res = ''
    for ch in s:
        if ch.isalpha():
            ch_low = ch
            index = alphabets.index(ch_low.lower())
            res += (new_alph[index] if ch.islower() else new_alph[index].upper())
        else:
            res += ch
    print res


def main():
    n = int(raw_input().strip())
    s = raw_input().strip()
    k = int(raw_input().strip())
    encrypt(s, k)


if __name__ == '__main__':
    main()
