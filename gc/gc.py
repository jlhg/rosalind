#!/usr/bin/env python3
#
# gc.py
#
# Copyright (C) 2013, Jian-Long Huang
# Author: Jian-Long Huang (jianlong@ntu.edu.tw)
# Version: 0.1
# Created: 2013.1.11
#
# http://rosalind.info/problems/gc/
#
# usage: gc.py <input> <output>

import sys

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as fin, open(sys.argv[2], 'w') as fw:

        seq = {}

        for line in fin:
            if (line[0] == '>'):
                header = line.rstrip()
                seq[header] = ''
            else:
                seq[header] = seq[header] + line.rstrip()

        has_max_gcc_header = ''
        gc_content = 0

        for header in seq:
            this_gc_content = (seq[header].count('C') + seq[header].count('G')) / len(seq[header])
            if this_gc_content > gc_content:
                has_max_gcc_header = header
                gc_content = this_gc_content

        fw.write(has_max_gcc_header[1:] + '\n' + str(gc_content * 100) + '%')
        fw.flush()
