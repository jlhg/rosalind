#!/usr/bin/env python
#
# orf - Open Reading Frames
#
# http://rosalind.info/problems/orf/
#
# Created: 2013.10.16

import sys


def main():
    with open(sys.argv[1], 'r') as fi:
        fi.readline()
        seq = []
        for line in fi:
            seq.append(line.strip())

        orfaa = set()
        for i in generate_sixorfs(''.join(seq)):
            for j in generate_orfaa(i):
                orfaa.add(j)

        for i in orfaa:
            print(i)


def translation(text):
    codon_table = {
        'TTT': 'F',
        'CTT': 'L',
        'ATT': 'I',
        'GTT': 'V',
        'TTC': 'F',
        'CTC': 'L',
        'ATC': 'I',
        'GTC': 'V',
        'TTA': 'L',
        'CTA': 'L',
        'ATA': 'I',
        'GTA': 'V',
        'TTG': 'L',
        'CTG': 'L',
        'ATG': 'M',
        'GTG': 'V',
        'TCT': 'S',
        'CCT': 'P',
        'ACT': 'T',
        'GCT': 'A',
        'TCC': 'S',
        'CCC': 'P',
        'ACC': 'T',
        'GCC': 'A',
        'TCA': 'S',
        'CCA': 'P',
        'ACA': 'T',
        'GCA': 'A',
        'TCG': 'S',
        'CCG': 'P',
        'ACG': 'T',
        'GCG': 'A',
        'TAT': 'Y',
        'CAT': 'H',
        'AAT': 'N',
        'GAT': 'D',
        'TAC': 'Y',
        'CAC': 'H',
        'AAC': 'N',
        'GAC': 'D',
        'TAA': '*',
        'CAA': 'Q',
        'AAA': 'K',
        'GAA': 'E',
        'TAG': '*',
        'CAG': 'Q',
        'AAG': 'K',
        'GAG': 'E',
        'TGT': 'C',
        'CGT': 'R',
        'AGT': 'S',
        'GGT': 'G',
        'TGC': 'C',
        'CGC': 'R',
        'AGC': 'S',
        'GGC': 'G',
        'TGA': '*',
        'CGA': 'R',
        'AGA': 'R',
        'GGA': 'G',
        'TGG': 'W',
        'CGG': 'R',
        'AGG': 'R',
        'GGG': 'G',
    }

    aa = []
    for i in range(0, len(text), 3):
        if codon_table.get(text[i:i + 3]):
            aa.append(codon_table.get(text[i:i + 3]))

    return ''.join(aa)


def generate_sixorfs(seq):
    orfs = []
    orfs.append(seq)
    orfs.append(seq[1:])
    orfs.append(seq[2:])

    seqrc = revcomp(seq)
    orfs.append(seqrc)
    orfs.append(seqrc[1:])
    orfs.append(seqrc[2:])

    return orfs


def generate_orfaa(seq):
    prots = translation(seq).split('*')
    for p in prots[:-1]:
        try:
            pos = 0
            while True:
                start = p.index('M', pos)
                yield p[start:]
                pos = start + 1
        except ValueError:
            continue


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
