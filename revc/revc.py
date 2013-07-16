#!/usr/bin/env python2.7
#
# revc.py
#
# Copyright (C) 2013, Jian-Long Huang
# Author: Jian-Long Huang (jianlong@ntu.edu.tw)
# Version: 0.2

from string import maketrans


def main(finput, foutput):
    """Complementing a strand of DNA

    finput: input file that conains a DNA string
    foutput: output file
    """
    table = maketrans('ATCG', 'TAGC')

    with open(finput, 'r') as fi, open(foutput, 'w') as fo:
        seq_rc = fi.read().rstrip().translate(table)
        fo.write(seq_rc[::-1])
        fo.flush()


if __name__ == '__main__':
    import sys
    main(*sys.argv[1:])
