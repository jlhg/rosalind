#!/usr/bin/env python3
#
# dna.py
#
# Copyright (C) 2013, Jian-Long Huang
# Author: Jian-Long Huang (jianlong@ntu.edu.tw)
# Version: 0.1
#
# http://rosalind.info/problems/dna/
#
# Usage: dna.py <input>

import sys

if __name__ == '__main__':
    nucl = {'A': 0, 'a': 0, 'C': 0, 'c': 0,
            'G': 0, 'g': 0, 'T': 0, 't': 0}

    with open(sys.argv[1], 'r') as f:
        for c in f.read():
            if c in nucl:
                nucl[c] += 1

    print("%d %d %d %d" % (nucl['A'] + nucl['a'], nucl['C'] + nucl['c'],
                           nucl['G'] + nucl['g'], nucl['T'] + nucl['t']))
