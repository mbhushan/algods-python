#!/usr/bin/env python2.7

import sys
import re

"""
https://www.hackerrank.com/challenges/beautiful-binary-string
"""


def main():
    n = int(raw_input().strip())
    B = raw_input().strip()
    pat = "010"
    indices = [m.start() for m in re.finditer(pat, B)]
    # print "{0}".format(indices)
    print "{}".format(len(indices))

if __name__ == '__main__':
    main()