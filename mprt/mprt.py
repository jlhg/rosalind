#!/usr/bin/env python
#
# mprt - Finding a Protein Motif
#
# http://rosalind.info/problems/mprt/
#
# Created: 2013.10.17

import sys
import urllib2


def main():
    with open(sys.argv[1], 'r') as fi:
        for line in fi:
            line = line.strip()
            response = urllib2.urlopen('http://www.uniprot.org/uniprot/%s.fasta' % (line))

            response.readline()  # discard fasta header
            seq = response.read().replace('\n', '')
            locations = nglyco_motif(seq)
            if locations:
                print(line)
                print(' '.join([str(i) for i in locations]))


def nglyco_motif(seq):
    locations = []
    for i in range(len(seq)):
        if i + 4 < len(seq) - 1:
            if seq[i] == 'N' and \
               seq[i + 1] != 'P' and \
               seq[i + 2] in {'S', 'T'} and \
               seq[i + 3] != 'P':
                locations.append(i + 1)

    return locations


if __name__ == '__main__':
    main()
