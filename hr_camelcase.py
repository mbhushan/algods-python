#!/bin/python

import sys

"""
https://www.hackerrank.com/challenges/camelcase
"""

def main():
    text = raw_input().strip()
    word_count = 1
    for ch in text:
        if ch.isupper():
            word_count += 1
    print word_count


if __name__ == '__main__':
    main()
