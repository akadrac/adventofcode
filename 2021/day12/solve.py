import sys
from collections import defaultdict


def getData():
    with open(sys.argv[1]) as f:
        return f.read().splitlines()


def paths4P1(nodes):
    paths = []
    queue = []
    for e in nodes["start"]:
        queue.append(["start", e])

    while len(queue) > 0:
        q = queue.pop()
        for e in nodes[q[-1]]:
            if e == "start":
                continue
            elif e == "end":
                paths.append(q + [e])
            elif e.isupper():
                queue.append(q + [e])
            elif q.count(e) == 0:
                queue.append(q + [e])

    return paths


def paths4P2(nodes):
    paths = []
    queue = []
    for e in nodes["start"]:
        queue.append(["start", e])

    while len(queue) > 0:
        q = queue.pop()

        for e in nodes[q[-1]]:
            if e == "start":
                continue
            elif e == "end":
                paths.append(q + [e])
            elif e.isupper():
                queue.append(q + [e])
            else:
                l = [i for i in q if i not in ["start", "end"] and i.islower()]
                if any(True for i in l if l.count(i) > 1) and q.count(e) > 0:
                    continue
                else:
                    queue.append(q + [e])

    return paths


def main():
    i = [x.split("-") for x in getData()]

    nodes = defaultdict(list)

    for (n, e) in i:
        nodes[n].append(e)
        nodes[e].append(n)

    # print(nodes)

    p1 = paths4P1(nodes)
    p2 = paths4P2(nodes)

    # print(paths)
    print(len(p1))
    print(len(p2))
    # for p in p2:
    #     print(",".join(map(str, p)))


if __name__ == "__main__":
    main()
