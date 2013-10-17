#!/usr/bin/env python
#
# prot.py
#
# Copyright (C) 2013, Jian-Long Huang
# Licensed under The MIT License
# http://opensource.org/licenses/MIT
#
# Author: Jian-Long Huang (jlhgln@gmail.com)
# Version: 0.1
# Created: 2013.7.22
#
# http://rosalind.info/problems/prot/
#
# Usage: prot.py <input> <output>


def rna_to_protein(finput):
    codon_table = {
        'UUU': 'F',
        'CUU': 'L',
        'AUU': 'I',
        'GUU': 'V',
        'UUC': 'F',
        'CUC': 'L',
        'AUC': 'I',
        'GUC': 'V',
        'UUA': 'L',
        'CUA': 'L',
        'AUA': 'I',
        'GUA': 'V',
        'UUG': 'L',
        'CUG': 'L',
        'AUG': 'M',
        'GUG': 'V',
        'UCU': 'S',
        'CCU': 'P',
        'ACU': 'T',
        'GCU': 'A',
        'UCC': 'S',
        'CCC': 'P',
        'ACC': 'T',
        'GCC': 'A',
        'UCA': 'S',
        'CCA': 'P',
        'ACA': 'T',
        'GCA': 'A',
        'UCG': 'S',
        'CCG': 'P',
        'ACG': 'T',
        'GCG': 'A',
        'UAU': 'Y',
        'CAU': 'H',
        'AAU': 'N',
        'GAU': 'D',
        'UAC': 'Y',
        'CAC': 'H',
        'AAC': 'N',
        'GAC': 'D',
        'UAA': '',
        'CAA': 'Q',
        'AAA': 'K',
        'GAA': 'E',
        'UAG': '',
        'CAG': 'Q',
        'AAG': 'K',
        'GAG': 'E',
        'UGU': 'C',
        'CGU': 'R',
        'AGU': 'S',
        'GGU': 'G',
        'UGC': 'C',
        'CGC': 'R',
        'AGC': 'S',
        'GGC': 'G',
        'UGA': '',
        'CGA': 'R',
        'AGA': 'R',
        'GGA': 'G',
        'UGG': 'W',
        'CGG': 'R',
        'AGG': 'R',
        'GGG': 'G',
    }

    with open(finput, 'r') as fi:
        while True:
            codon = fi.read(3)
            if codon == '':
                break
            yield codon_table.get(codon)


if __name__ == '__main__':
    import sys
    protein_generator = rna_to_protein(sys.argv[1])
    with open(sys.argv[2], 'w') as fo:
        for aa in protein_generator:
            if aa:
                fo.write(aa)
                fo.flush()
