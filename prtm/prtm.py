#!/usr/bin/env python
#
# Calculating Protein Mass
#
# http://rosalind.info/problems/prtm/
#
# Created: 2013.10.19

import sys


def main():
    with open(sys.argv[1], 'r') as fi:
        weight = 0
        for line in fi:
            weight += weight_aa(line.strip())
        print(weight)


def weight_aa(s):
    mass_table = {
        'A': 71.03711,
        'C': 103.00919,
        'D': 115.02694,
        'E': 129.04259,
        'F': 147.06841,
        'G': 57.02146,
        'H': 137.05891,
        'I': 113.08406,
        'K': 128.09496,
        'L': 113.08406,
        'M': 131.04049,
        'N': 114.04293,
        'P': 97.05276,
        'Q': 128.05858,
        'R': 156.10111,
        'S': 87.03203,
        'T': 101.04768,
        'V': 99.06841,
        'W': 186.07931,
        'Y': 163.06333,
    }

    weight = 0
    for i in s:
        weight += mass_table.get(i)

    return weight


if __name__ == '__main__':
    main()
