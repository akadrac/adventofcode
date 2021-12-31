import sys
from collections import defaultdict
from functools import reduce
import re
from heapq import heappop, heappush


def getData():
    with open(sys.argv[1]) as f:
        return f.read().splitlines()


# def surrouding(size, p):
#     f = p // size

#     [x for x in [p - 1, p + 1] if f * size < x < (f + 1) * size]
#     [x for x in [p - size, p + size] if 0 < x < size * size]

#     return [
#         *[x for x in [p - 1, p + 1] if f * size < x < (f + 1) * size],
#         *[x for x in [p - size, p + size] if 0 < x < size * size],
#     ]


# def pathFindOld(grid, size, randomCost):
#     minCost = randomCost
#     queue = [[0]]
#     minPath = []

#     loop = 0
#     while len(queue) > 0:
#         loop += 1
#         # print(loop, len(queue))

#         path = queue.pop()
#         if cost(grid, path) > minCost:
#             continue
#         elif path[-1] == size * size - 1:
#             c = cost(grid, path)
#             print(c)
#             minCost = min(minCost, c)
#             if c == minCost:
#                 minPath = path
#         else:
#             queue.extend(
#                 [[*path, x] for x in surrouding(size, path[-1]) if x not in path]
#             )

#     print(minPath)
#     print(minCost)

#     return minPath


# def pathFindOld2(grid, size, randomCost):
#     minCost = randomCost
#     queue = [[0, 0]]
#     minPath = []

#     loop = 0
#     while len(queue) > 0:
#         loop += 1
#         # print(loop, len(queue))
#         # print(queue)

#         path = queue.pop()
#         # print(path)
#         if path[0] > minCost:
#             continue
#         elif path[-1] == size * size - 1:
#             if path[0] < minCost:
#                 minCost = path[0]
#                 minPath = path
#                 print(minCost, minPath)
#         else:
#             queue.extend(
#                 [
#                     [path[0] + int(grid[x]), *path[1:], x]
#                     for x in surrouding(size, path[-1])
#                     if x not in path
#                 ]
#             )

#     print(minPath)
#     print(minCost)

#     return minPath


# def diagPath(grid, size):
#     path = []
#     for x in range(size):
#         path.append(size * x + x)

#     return path


# def stepPath(grid, size):
#     path = []
#     for x in range(size):
#         path.append(size * x + x)
#         if size * x + x + 1 < size * size:
#             path.append(size * x + x + 1)

#     return path


# def cost(grid, path):
#     return reduce(lambda a, c: a + int(grid[c]), path, 0) - int(grid[0])


# def pathFind(grid, size):
#     return


# def dijkstra(input, label):
#     size = len(input[0])
#     grid = "".join(input)

#     visited_and_distance = defaultdict(int)
#     for i in range(size * size):
#         visited_and_distance[i] = sys.maxsize

#     visited_and_distance[0] = 0

#     for i in range(1, size * size):
#         if i == 12:
#             print(previous(i, size))
#         visited_and_distance[i] = min(
#             [visited_and_distance[x] for x in previous(i, size)]
#         ) + int(grid[i])

#     print(visited_and_distance)
#     print(label, visited_and_distance[size * size - 1])


def previous(i, size):
    f = i // size
    return [
        *[x for x in [i - 1, i + 1] if f * size <= x < (f + 1) * size],
        *[x for x in [i - size, i + size] if 0 <= x < size * size],
    ]


def dijkstra(input, label):
    size = len(input[0])
    grid = "".join(input)

    visited_and_distance = [[0, sys.maxsize] for s in range(size * size)]
    visited_and_distance[0] = [0, 0]

    queue = []
    heappush(queue, (0, 0))  # set the starting point
    while queue:
        risk, item = heappop(queue)
        if item == size * size - 1:  # found exit
            print(label, risk)
            break
        for i in previous(item, size):
            if visited_and_distance[i][0] == 0:
                r = risk + int(grid[i])
                visited_and_distance[i] = [1, r]
                heappush(queue, (r, i))


def p2(input, label):
    i = [list(map(int, list(x))) for x in input]

    old_size = len(input[0])
    new_size = old_size * 5

    tmp_input = [[0 for c in range(new_size)] for r in range(new_size)]

    for r in range(old_size):
        for c in range(old_size):
            tmp_input[r][c] = i[r][c]

    # down
    for r in range(old_size, new_size):
        for c in range(old_size):
            tmp_input[r][c] = tmp_input[r - old_size][c] % 9 + 1

    # across
    for r in range(new_size):
        for c in range(old_size, new_size):
            tmp_input[r][c] = tmp_input[r][c - old_size] % 9 + 1

    new_input = ["".join(map(str, x)) for x in tmp_input]

    dijkstra(new_input, label)


def main():
    input = getData()

    dijkstra(input, "p1")
    p2(input, "p2")


if __name__ == "__main__":
    main()
