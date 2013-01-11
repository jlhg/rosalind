#!/usr/bin/env python3
#
# hamm.py
#
# Copyright (C) 2013, Jian-Long Huang
# Author: Jian-Long Huang (jianlong@ntu.edu.tw)
# Version: 0.1
# Created: 2013.1.11
#
# http://rosalind.info/problems/hamm/
#
# Algorithm example:
# http://en.wikipedia.org/wiki/Hamming_distance
#
# Usage: hamm.py <input>

import sys

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as fin:
        s1 = fin.readline().rstrip()
        s2 = fin.readline().rstrip()
        print(sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2)))
