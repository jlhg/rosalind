#!/usr/bin/env python3
#
# cons.py
#
# Copyright (C) 2013, Jian-Long Huang
# Author: Jian-Long Huang (jianlong@ntu.edu.tw)
# Version: 0.1
# Created: 2013.1.11
#
# http://rosalind.info/problems/cons/
#
# Usage: cons.py <input> <output>

import sys

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as fin, open(sys.argv[2], 'w') as fw:

        profile = {'A': [], 'C': [], 'G': [], 'T': []}
        consensus = []
        seqs = []

        for line in fin:
            seqs.append(line.rstrip())

        for i in zip(*seqs):
            profile['A'].append(i.count('A'))
            profile['C'].append(i.count('C'))
            profile['G'].append(i.count('G'))
            profile['T'].append(i.count('T'))
            consensus.append(max(i, key=i.count))

        fw.write(''.join(consensus) + '\n')
        fw.write('A: ' + ' '.join(map(str, profile['A'])) + '\n')
        fw.write('C: ' + ' '.join(map(str, profile['C'])) + '\n')
        fw.write('G: ' + ' '.join(map(str, profile['G'])) + '\n')
        fw.write('T: ' + ' '.join(map(str, profile['T'])) + '\n')
        fw.flush()
