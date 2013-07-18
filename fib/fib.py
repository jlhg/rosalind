#!/usr/bin/env python
#
# fib.py
#
# Copyright (C) 2013, Jian-Long Huang
# Licensed under The MIT License
# http://opensource.org/licenses/MIT
#
# Author: Jian-Long Huang (jlhgln@gmail.com)
# Version: 0.1
# Created: 2013.7.18
#
# http://rosalind.info/problems/fib/
#
# Usage: fib.py <input>


def fib(m, k):
    """Rabbits and recurrence relations

    m: month
    k: number of rabbit pairs produced

    formula: Fn = Fn-1 + Fn-2 * k (with F1 = F2 = 1)
    """
    assert m > 2

    first = 1
    second = 1
    generation = 3
    while generation <= m:
        result = second + first * k
        second, first = result, second
        generation += 1

    return result


if __name__ == '__main__':
    import sys
    with open(sys.argv[1], 'r') as fi:
        month, k = fi.readline().strip().split(' ')
        print(fib(int(month), int(k)))
