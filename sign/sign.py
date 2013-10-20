#!/usr/bin/env python
#
# Enumerating Oriented Gene Orderings
#
# http://rosalind.info/problems/sign/
#
# Created: 2013.10.20

import sys


def main():
    number = int(sys.argv[1])
    lst = [str(i) for i in range(1, number + 1)]

    results = []
    for i in generate_signed_lists(lst):
        perm = list(permutation(i))
        for p in perm:
            results.append(p)
    print(len(results))
    for i in results:
        print(i)


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


def generate_signed_lists(lst):
    # No signed element
    yield lst

    # At least one signed element
    for i in range(1, len(lst) + 1):
        for c in combination(lst, i):
            unsigned = rm_subset(lst, c)
            signed = ['-%s' % (j) for j in c]
            yield unsigned + signed


def combination(lst, r):
    """A generator that yields tuples of combinations"""
    if r == 1:
        for i in lst:
            yield (i,)
    else:
        for i in range(len(lst)):
            for n in combination(lst[i + 1:], r - 1):
                yield (lst[i],) + n


def rm_subset(lst, subset):
    new_lst = list(lst)
    for i in subset:
        new_lst.remove(i)

    return new_lst


if __name__ == '__main__':
    main()
