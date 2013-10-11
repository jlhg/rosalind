#!/usr/bin/env python

import sys
from itertools import permutations


def main():
    number = int(sys.argv[1])
    for p in permutations([str(i) for i in range(1, number + 1)]):
        print(' '.join(p))


if __name__ == '__main__':
    main()
