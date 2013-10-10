#!/usr/bin/env python
#
# revp - Locating Restriction Sites
#
# http://rosalind.info/problems/revp/
#
# Created: 2013.10.10

import sys


def main():
    with open(sys.argv[1], 'r') as fi:
        fi.readline()
        seqlist = []
        for line in fi:
            seqlist.append(line.strip())

        seq = ''.join(seqlist)
        for i in range(len(seq) - 3):
            for j in range(4, 13):
                if i + j <= len(seq) and revcomp(seq[i:i + j]) == seq[i:i + j]:
                    print('%s %s' % (i + 1, j))


def revcomp(text):
    comptable = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C',
    }
    rc = []
    for i in reversed(text):
        if i in comptable:
            rc.append(comptable.get(i))

    return ''.join(rc)


if __name__ == '__main__':
    main()
