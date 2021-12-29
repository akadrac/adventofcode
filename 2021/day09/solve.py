import sys
import functools


def getData():
    with open(sys.argv[1]) as f:
        return f.read().splitlines()


def surrouding(rl, cl, r, c):
    return [
        (x, y)
        for (x, y) in [(r, c - 1), (r - 1, c), (r, c + 1), (r + 1, c)]
        if 0 <= x < rl and 0 <= y < cl
    ]


def basin(i, ir, ic):
    basin = []
    vistied = set()
    queue = [(ir, ic)]

    while len(queue) > 0:
        (r, c) = queue.pop()

        if (r, c) in vistied:
            continue
        else:
            vistied.add((r, c))
            if i[r][c] != 9:
                basin.append((r, c))
                queue.extend(
                    [
                        (ar, ac)
                        for (ar, ac) in surrouding(len(i), len(i[0]), r, c)
                        if (ar, ac) not in vistied
                    ]
                )

    return len(basin)


def main():
    i = [list(map(int, list(x))) for x in getData()]

    lr = len(i)
    lc = len(i[0])

    t = []
    minPos = []

    for r in range(lr):
        for c in range(lc):
            v = i[r][c]

            a = i[r][c - 1] if c - 1 >= 0 else 9
            s = i[r - 1][c] if r - 1 >= 0 else 9
            d = i[r][c + 1] if c + 1 < lc else 9
            w = i[r + 1][c] if r + 1 < lr else 9

            # print(r, c, v, a, s, w, d)
            if v < min([a, s, w, d]):
                t.append(v + 1)
                minPos.append([r, c])

    b = [basin(i, r, c) for [r, c] in minPos]

    print("sum of min", sum(t))
    print(
        "basin size", functools.reduce(lambda a, b: a * b, sorted(b, reverse=True)[0:3])
    )
    return


if __name__ == "__main__":
    main()
