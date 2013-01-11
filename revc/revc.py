#!/usr/bin/env python3
#
# revc.py
#
# Copyright (C) 2013, Jian-Long Huang
# Author: Jian-Long Huang (jianlong@ntu.edu.tw)
# Version: 0.1

import sys

if __name__ == '__main__':
    table = str.maketrans('ATCG', 'TAGC')

    with open(sys.argv[1], 'r') as fin, open(sys.argv[2], 'w') as fw:
        sequence = fin.read().rstrip().translate(table)
        fw.write(sequence[::-1])
        fw.flush()
