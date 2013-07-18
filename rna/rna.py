#!/usr/bin/env python2.7
#
# rna.py
#
# Copyright (C) 2013, Jian-Long Huang
# Author: Jian-Long Huang (jianlong@ntu.edu.tw)
# Version: 0.2
#
# http://rosalind.info/problems/rna/
#
# Usage: rna.py <input> <output>

from string import maketrans


def main(finput, foutput):
    """Transcribing DNA into RNA

    finput: input file that conains a DNA string
    foutput: output file
    """
    table = maketrans('Tt', 'Uu')

    with open(finput, 'r') as fi, open(foutput, 'w') as fo:
        fo.write(fi.read().translate(table))
        fo.flush()


if __name__ == '__main__':
    import sys
    main(*sys.argv[1:])
