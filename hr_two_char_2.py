#!/bin/python

import sys

"""
https://www.hackerrank.com/challenges/two-characters
beabeefeab
"""


def make(a, b, s):
    p = []
    for x in s :
        if x == a or x == b:
            p.append(x)
    return "".join(p)

def check(t):
    for i in xrange(len(t)-1):
        if t[i] == t[i+1]: return False
    return True

def solve(n, s, cs):
    ans = 0
    for x in cs:
        for y in cs:
            if x == y: continue
            t = make(x, y, s)
            if check(t):
                ans = max(ans, len(t))

    print ans

def main():
    n = int(raw_input())
    s = raw_input()
    cs = set(s)
    solve(n, s, cs)

if __name__ == '__main__':
    main()
