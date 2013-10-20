#!/usr/bin/env python
#
# Solution by propheta13
#
# This is slower than sign.py

import sys
from itertools import permutations


def main():
    n = int(sys.argv[1])
    lst = [x for x in permutations([i for i in range(-n, n + 1) if (i != 0)], n) if set(range(1, n + 1)) == set(map(abs, x))]
    print len(lst)
    for i in lst:
        print ' '.join(map(str, i))


if __name__ == '__main__':
    main()
