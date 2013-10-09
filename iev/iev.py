#!/usr/bin/env python
#
# iev - Calculating Expected Offspring
#
# http://rosalind.info/problems/iev/
#
# Created: 2013.10.9

import sys


def main():
    couples = open(sys.argv[1], 'r').readline().strip()
    gt1, gt2, gt3, gt4, gt5, gt6 = [int(i) for i in couples.split(' ')]
    expect = 2 * (gt1 + gt2 + gt3 + gt4 * 0.75 + gt5 * 0.5)
    print(expect)


if __name__ == '__main__':
    main()
