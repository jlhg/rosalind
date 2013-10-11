#!/usr/bin/env python
#
# Solved by Petar Ivanov

import sys


def substr_in_all(arr, part):
    for dna in arr:
        if part not in dna:
            return False
    return True


def common_substr(arr, l):
    first = arr[0]
    for i in range(len(first) - l + 1):
        part = first[i:i + l]
        if substr_in_all(arr, part):
            return part
    return ''


def longest_common_substr(arr):
    l = 0
    r = len(arr[0])

    while l + 1 < r:
        mid = (l + r) // 2
        if common_substr(arr, mid) != '':
            l = mid
        else:
            r = mid

    return common_substr(arr, l)


if __name__ == '__main__':
    arr = []
    with open(sys.argv[1], 'r') as fi:
        fi.readline()
        seq = []
        for line in fi:
            if line.startswith('>'):
                arr.append(''.join(seq))
                seq = []
            else:
                seq.append(line.strip())
        arr.append(''.join(seq))

    print(longest_common_substr(arr))
