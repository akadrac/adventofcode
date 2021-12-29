import sys
from collections import deque
import functools


def getData():
    with open(sys.argv[1]) as f:
        return f.read().splitlines()


def surrouding(rl, cl, r, c):
    return [
        (x, y)
        for (x, y) in [
            (r, c - 1),
            (r - 1, c),
            (r, c + 1),
            (r + 1, c),
            (r - 1, c - 1),
            (r - 1, c + 1),
            (r + 1, c - 1),
            (r + 1, c + 1),
        ]
        if 0 <= x < rl and 0 <= y < cl
    ]


def addOne(i):
    for r in range(len(i)):
        for c in range(len(i[0])):
            i[r][c] += 1


def reset(i):
    for r in range(len(i)):
        for c in range(len(i[0])):
            if i[r][c] > 9:
                i[r][c] = 0


def flashed(i):
    f = 0
    for r in range(len(i)):
        for c in range(len(i[0])):
            if i[r][c] > 9:
                f += 1

    return f


def cascade(i):

    f = []
    for r in range(len(i)):
        for c in range(len(i[0])):
            if i[r][c] > 9:
                f.append((r, c))

    if len(f) > 0:
        bob(i, f)


def bob(i, queue):

    flashed = set()
    while len(queue) > 0:
        (r, c) = queue.pop()
        if (r, c) in flashed:
            continue

        i[r][c] += 1

        if i[r][c] > 9:
            flashed.add((r, c))
            s = surrouding(len(i), len(i[0]), r, c)
            queue.extend(s)


def main():
    i = [list(map(int, list(x))) for x in getData()]

    f = 0
    s = 0
    l = True

    size = len(i) * len(i[0])

    while l:
        addOne(i)

        cascade(i)

        t = flashed(i)

        if t == size:
            print("sync:", s + 1)
            l = False

        if s < 100:
            f += t

        reset(i)

        s += 1

    print(f)


if __name__ == "__main__":
    main()
