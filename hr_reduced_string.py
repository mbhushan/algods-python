#!/bin/python

import sys


"""
https://www.hackerrank.com/challenges/reduced-string
s = "aaabccddd"
"""

def main():
    word = raw_input().strip()
    is_reduced = True
    iteration = 0
    while is_reduced:
        index = 0
        is_reduced = False
        prev, curr = word[index], word[index]
        count = 0
        wlen = len(word)
        result = ''
        while index < wlen:
            curr = word[index]
            if prev == curr:
                count += 1
            else:
                if count%2 == 1:
                    result += prev
                if count > 1:
                    is_reduced = True
                prev = curr
                count = 1
            index += 1
        if count%2 == 1:
            result += prev
        is_reduced = True if count > 1 else is_reduced

        # print "iter: {} => {}".format(iteration, result)
        iteration += 1
        if len(result) <= 1:
            is_reduced = False
        word = result
    if len(result) >= 1:
        print result
    else:
        print "Empty String"




if __name__ == '__main__':
    main()
