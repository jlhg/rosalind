#!/usr/bin/env python3
#
# grph.py
#
# Copyright (C) 2013, Jian-Long Huang
# Author: Jian-Long Huang (jianlong@ntu.edu.tw)
# Version: 0.1
# Created: 2013.1.12
#
# http://rosalind.info/problems/grph/
#
# Usage: grph.py <input> <output>

import sys

if __name__ == '__main__':
    dna = {}
    prefix = {}
    suffix = {}

    with open(sys.argv[1], 'r') as fin, open(sys.argv[2], 'w') as fw:
        for line in fin:
            line = line.rstrip()
            if line[0] == '>':
                header = line[1:]
                dna.update({line[1:]: ''})
            else:
                dna[header] = dna[header] + line

        for name, seq in dna.items():
            if seq[0:3] in prefix:
                prefix[seq[0:3]].append(name)
            else:
                prefix.update({seq[0:3]: [name]})
            if seq[-3:] in suffix:
                suffix[seq[-3:]].append(name)
            else:
                suffix.update({seq[-3:]: [name]})

        for trimer in suffix:
            if trimer in prefix:
                for h1 in suffix[trimer]:
                    for h2 in prefix[trimer]:
                        if h1 != h2:
                            fw.write(h1 + ' ' + h2 + '\n')
                            fw.flush()
