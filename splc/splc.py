#!/usr/bin/env python
#
# splc - RNA Splicing
#
# http://rosalind.info/problems/splc/
#
# Created: 2013.10.15

import sys
from collections import OrderedDict


def main():
    with open(sys.argv[1], 'r') as fi:
        seqs = OrderedDict()
        for line in fi:
            line = line.strip()
            if line.startswith('>'):
                header = line
            else:
                if header not in seqs:
                    seqs.update({header: [line]})
                else:
                    seqs.get(header).append(line)

        count = 0
        dna = None
        for key, value in seqs.items():
            count += 1
            if count == 1:
                dna = ''.join(value)
            else:
                try:
                    index = dna.index(''.join(value))
                    dna = dna[0:index] + dna[index + len(''.join(value)):]
                except ValueError:
                    pass
        protein = translation(dna)
        print(protein)


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
        'TAA': '',
        'CAA': 'Q',
        'AAA': 'K',
        'GAA': 'E',
        'TAG': '',
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
        'TGA': '',
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


if __name__ == '__main__':
    main()
