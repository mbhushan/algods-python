#!/bin/python

import sys

"""
https://www.hackerrank.com/challenges/two-characters
beabeefeab
"""


def get_indices(text, ch):
    return [i for i, ltr in enumerate(text) if ltr == ch]


def check_alternate(ch1_indices, ch2_indices):
    ch1_len = len(ch1_indices)
    ch2_len = len(ch2_indices)
    if (abs(ch1_len - ch2_len) > 1):
        return False
    arr = []
    i, j = 0, 0
    index = 0
    ans = True

    while (i < ch1_len and j < ch2_len):
        if (index%2 == 0):
            if len(arr) > 0 and ch1_indices[i] < arr[-1]:
                ans = False
            arr.append(ch1_indices[i])
            i += 1
        else:
            if len(arr) > 0 and ch2_indices[j] < arr[-1]:
                ans = False
            arr.append(ch2_indices[j])
            j += 1
        index += 1
    # print"i: {}, j: {}".format(i, j)
    if i < ch1_len-1 and ch1_indices[i+1] < arr[-1]:
        ans = False
    if j < ch2_len-1 and ch2_indices[j+1] < arr[-1]:
        ans = False
    # print "ans: {}".format(ans)
    # print arr
    return (ch1_len + ch2_len) if ans else 0

def main():
    #s_len = int(raw_input().strip())
    s = raw_input().strip()
    charset = ''.join(set(s))
    # print "charset: " + charset
    max_len = 0
    for i in range(0, len(charset)-1):
        ch1_indices = get_indices(s, charset[i])
        ch2_indices = get_indices(s, charset[i+1])

        # print "ch1 indices: {}".format(ch1_indices)
        # print "ch2 indices: {}".format(ch2_indices)
        curr_len = check_alternate(ch1_indices, ch2_indices) if ch1_indices[0] < ch2_indices[0] else check_alternate(ch2_indices, ch1_indices)
        if curr_len > max_len:
            max_len = curr_len
    print max_len


if __name__ == '__main__':
    main()