#!/usr/bin/env python3
#
# rna.py
#
# Copyright (C) 2013, Jian-Long Huang
# Author: Jian-Long Huang (jianlong@ntu.edu.tw)
# Version: 0.1
#
# http://rosalind.info/problems/rna/
#
# Usage: rna.py <input> <output>

import sys

if __name__ == '__main__':

    table = str.maketrans("Tt", "Uu")

    with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w') as fw:
        for c in f.read():
            fw.write(c.translate(table))
        fw.flush
