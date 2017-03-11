#!/bin/python

"""
https://www.hackerrank.com/challenges/mars-exploration
SOSSPSSQSSOR
SOSOOSOSOSOSOSSOSOSOSOSOSOS
"""


def main():
    S = raw_input().strip()
    target = "SOS"
    count = 0
    for i in range(0, len(S)-2, 3):
        signal = S[i: i+3]
        if signal != target:
            for j in range(len(target)):
                if signal[j] != target[j]:
                    count += 1
    print count


if __name__ == '__main__':
    main()