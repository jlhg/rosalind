#!/usr/bin/env python
#
# perm - enumerating gene orders
#
# http://rosalind.info/problems/perm/
#
# Created: 2013.10.11
# Usage: perm.py <integer>

import sys


def main():
    number = int(sys.argv[1])
    lst = [str(i) for i in range(1, number + 1)]
    perm = list(permutation(lst))
    print(len(perm))
    for p in perm:
        print(p)


def permutation(lst):
    """Print permutation of a list of elements"""
    if len(lst) == 1:
        yield lst[0]
    else:
        for i in lst:
            lst_new = list(lst)
            lst_new.remove(i)
            for j in permutation(lst_new):
                yield '%s %s' % (i, ''.join(j))


if __name__ == '__main__':
    main()
