#!/usr/bin/env python3
#
# subs.py
#
# Copyright (C) 2013, Jian-Long Huang
# Author: Jian-Long Huang (jianlong@ntu.edu.tw)
# Version: 0.1
# Created: 2013.1.11
#
# http://rosalind.info/problems/subs/
#
# Usage: subs.py <input> <output>

import sys

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as fin, open(sys.argv[2], 'w') as fw:

        string = fin.readline().rstrip()
        subs = fin.readline().rstrip()
        pos = []

        for i in range(0, len(string) - len(subs)):
            if string[i:i + len(subs)] == subs:
                pos.append(i + 1)

        fw.write(' '.join(map(str, pos)))
        fw.flush()
