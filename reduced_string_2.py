#!/bin/python
import sys

"""
https://www.hackerrank.com/challenges/reduced-string
"""


def main():
    s = raw_input().strip()
    while True:
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                s = s[:i] + s[i + 2:]
                break
        else:
            break
    print(s if s else "Empty String")

if __name__ == '__main__':
    main()