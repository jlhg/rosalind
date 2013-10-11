#!/usr/bin/env python
#
# lcsm - Finding a Shared Motif
#
# http://rosalind.info/problems/lcsm/
#
# Created: 2013.10.11

import sys


def main():
    with open(sys.argv[1], 'r') as fi:
        seq = {}
        for line in fi:
            line = line.strip()
            if line.startswith('>'):
                header = line
                seq.update({header: []})
            else:
                seq.get(header).append(line)

        refseq, refseq_s = seq.items()[0]
        refseq_s = ''.join(refseq_s)
        seq.pop(refseq)
        window_size = range(2, len(refseq_s) + 1)
        common_subs = []
        has_common = False
        for i in window_size:
            for j in range(len(refseq_s)):
                for h, s in seq.items():
                    if j + i < len(refseq_s) and refseq_s[j:j + i] in ''.join(s):
                        has_common = True
                    else:
                        has_common = False
                        break
                if has_common:
                    common_subs.append(refseq_s[j:j + i])

        if common_subs:
            longest = None
            for i in common_subs:
                if longest:
                    if len(i) > len(longest):
                        longest = i
                else:
                    longest = i
            print(longest)
        else:
            print('No common substring.')


if __name__ == '__main__':
    main()
