#!/usr/bin/env python2.7
#
# gc.py
#
# Copyright (C) 2013, Jian-Long Huang
# Author: Jian-Long Huang (jianlong@ntu.edu.tw)
# Version: 0.2
# Created: 2013.1.11
#
# http://rosalind.info/problems/gc/
#
# usage: gc.py <input>


def calc_gc(seq):
    """Computing GC content

    seq: string
    """
    return (seq.count('C') + seq.count('G')) / float(len(seq))


def main(finput):
    """Computing GC content and print the result of highest GC-content

    finput: input file with fasta format
    """
    with open(finput, 'r') as fi:
        seq = {}
        for line in fi:
            if (line[0] == '>'):
                header = line.strip()[1:]
                seq.update({header: []})
            else:
                seq[header].append(line.strip())

        max_gc_header = None
        max_gc = 0

        for h, s in seq.items():
            gc = calc_gc(''.join(s))
            if gc > max_gc:
                max_gc_header = h
                max_gc = gc

        print(max_gc_header)
        print('%.6f' % (max_gc * 100))


if __name__ == '__main__':
    import sys
    main(*sys.argv[1:])
