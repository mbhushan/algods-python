#!/usr/bin/python

import sys

"""
https://www.hackerrank.com/challenges/pangrams
"""

def main():
    text = raw_input().strip()
    char_set = set()
    found = False
    for ch in text:
        ch = ch.lower()
        if ch.isalpha() and ch not in char_set:
            char_set.add(ch)
        if len(char_set) == 26:
            print "pangram"
            found = True
            break
    if not found:
        print "not pangram"

if __name__ == '__main__':
    main()