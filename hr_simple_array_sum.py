#!/bin/python

import sys


def main():
    n = int(raw_input().strip())
    arr = map(int,raw_input().strip().split(' '))
    sum = 0
    for i in arr:
        sum += i
    print "total sum: {}".format(sum)

if __name__ == '__main__':
    main()
