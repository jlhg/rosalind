#!/usr/bin/env python2.7
#
# hamm.py
#
# Copyright (C) 2013, Jian-Long Huang
# Author: Jian-Long Huang (jianlong@ntu.edu.tw)
# Version: 0.2
# Created: 2013.1.11
#
# http://rosalind.info/problems/hamm/
#
# Algorithm example:
# http://en.wikipedia.org/wiki/Hamming_distance
#
# Usage: hamm.py <input>


def main(finput):
    """Evolution as a sequence of mistakes

    finput: input file with two lines of DNA strings
    """
    with open(finput, 'r') as fi:
        s1 = fi.readline().rstrip()
        s2 = fi.readline().rstrip()
        print(sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2)))


if __name__ == '__main__':
    import sys
    main(*sys.argv[1:])
