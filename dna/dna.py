#!/usr/bin/env python
#
# dna.py
#
# Copyright (C) 2013, Jian-Long Huang
# Author: Jian-Long Huang (jianlong@ntu.edu.tw)
# Version: 0.2
#
# http://rosalind.info/problems/dna/
#
# Usage: dna.py <input>


def main(finput):
    """Counting DNA nucleotides

    finput: input file that contains a DNA string
    """
    nucl = {
        'A': 0, 'a': 0, 'C': 0, 'c': 0,
        'G': 0, 'g': 0, 'T': 0, 't': 0
    }

    with open(finput, 'r') as fi:
        for c in fi.read():
            if c in nucl:
                nucl[c] += 1

    num_a = nucl.get('A') + nucl.get('a')
    num_c = nucl.get('C') + nucl.get('c')
    num_g = nucl.get('G') + nucl.get('g')
    num_t = nucl.get('T') + nucl.get('t')

    print("%d %d %d %d" % (num_a, num_c, num_g, num_t))


if __name__ == '__main__':
    import sys
    main(sys.argv[1])
