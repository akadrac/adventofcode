import sys
from collections import defaultdict
import functools
import re


def getData():
    with open(sys.argv[1]) as f:
        return f.read().splitlines()


def vFold(page, s):
    print("folding v:", s)
    tmp = page[:s]
    rest = page[s + 1 :][::-1]

    for r, value in enumerate(rest):
        for c, e in enumerate(value):
            if e == "#":
                tmp[r][c] = "#"

    return tmp


def hFold(page, s):
    print("folding h:", s)
    tmp = [[x for x in y[:s]] for y in page]
    rest = [[x for x in y[s + 1 :][::-1]] for y in page]

    for r, value in enumerate(rest):
        for c, e in enumerate(value):
            if e == "#":
                tmp[r][c] = "#"

    return tmp


def main():
    input = getData()

    i = [list(map(int, i.split(","))) for i in input if len(i) < 13 and len(i) > 0]
    folds = [i.split("=") for i in input if len(i) > 13]

    for index, (t, s) in enumerate(folds):
        folds[index] = [t[-1], int(s)]

    # print(i)
    # print(folds)

    maxC = 0
    maxR = 0

    for t, s in folds:
        if t == "y":
            maxR = max(maxR, s * 2 + 1)
        else:
            maxC = max(maxC, s * 2 + 1)

    print(maxR)
    print(maxC)

    page = [[" " for x in range(maxC)] for y in range(maxR)]

    for c, r in i:
        page[r][c] = "#"

    for t, s in folds:
        if t[-1] == "y":
            page = vFold(page, int(s))
        else:
            page = hFold(page, int(s))

    # print(functools.reduce(lambda a, b: a + b, [p for p in page]).count(1))

    for p in page:
        print("".join(p))


if __name__ == "__main__":
    main()
