import sys
from collections import deque
import functools


def getData():
    with open(sys.argv[1]) as f:
        return f.read().splitlines()


def main():
    i = [list(x) for x in getData()]

    t = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }

    c = []
    x = []
    for r in i:
        s = []
        for v in r:
            if v in t:
                s.append(v)
            else:
                if t[s[-1]] == v:
                    s.pop()
                else:
                    print("Expected", t[s[-1]], "but found", v, "instead.")
                    c.append(v)
                    s.clear()
                    break

        if len(s) != 0:
            x.append(s[::-1])

    p = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    q = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4,
    }

    print("corrupt:", functools.reduce(lambda a, b: a + p[b], c, 0))

    m = sorted([functools.reduce(lambda a, b: a * 5 + q[b], z, 0) for z in x])
    print("missing:", m[round((len(m) - 1) / 2)])
    return


if __name__ == "__main__":
    main()
