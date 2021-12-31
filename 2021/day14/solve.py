import sys
from collections import defaultdict
import functools
import re


def getData():
    with open(sys.argv[1]) as f:
        return f.read().splitlines()


def part1(seq, rules, steps):

    step = 0
    while step < min(steps, 10):
        new_seq = ""
        for x in range(len(seq) - 1):
            pair = seq[x : x + 2]
            insert = rules[pair]
            if x == 0:
                new_seq += pair[0]
            new_seq += insert + pair[1]
        seq = new_seq
        step += 1

        # print(seq)

    pairs = defaultdict(int)
    for p in set(seq[index : index + 2] for index in range(len(seq) - 1)):
        pairs[p] = seq.count(p)

    characters = set(seq)
    most = 0
    least = sys.maxsize

    for c in characters:
        x = seq.count(c)
        # print(c, x)
        most = max(most, x)
        least = min(least, x)

    # print(pairs)
    # print(characters)
    print("result", most - least, "most", most, "least", least)


def part2(seq, rules, steps):

    pairs = defaultdict(int)
    for p in set(seq[index : index + 2] for index in range(len(seq) - 1)):
        pairs[p] = seq.count(p)
    characters = defaultdict(int)

    for c in seq:
        characters[c] += 1

    # print(pairs)
    # print(characters)
    # print(sum(characters.values()))

    step = 0
    while step < steps:
        # print("step", step)

        new_pairs = defaultdict(int)
        for p, v in pairs.items():
            # print(p, v)
            insert = rules[p]
            characters[insert] += v
            new_pairs[p[0] + insert] += v
            new_pairs[insert + p[1]] += v

        pairs = new_pairs

        step += 1

        # print(pairs)
        # print(characters)

    most = 0
    least = sys.maxsize
    for v in characters.values():
        most = max(most, v)
        least = min(least, v)

    # print(pairs)
    # print(characters)
    # print(sum(characters.values()))
    print("result", most - least, "most", most, "least", least)


def main():
    input = getData()

    seq = input[0]
    rules = dict(value.split(" -> ") for value in input if len(value.split("->")) > 1)

    steps = 40
    part1(seq, rules, steps)
    part2(seq, rules, steps)


if __name__ == "__main__":
    main()
