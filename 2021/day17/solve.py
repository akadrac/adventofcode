import sys
import re
import math


def getData():
    with open(sys.argv[1]) as f:
        return f.read().splitlines()


def main():
    input = getData()[0]
    # print(input)

    target = [
        int(x)
        for x in re.findall(
            "x=(-?\d{1,3})\.\.(-?\d{1,3}).*y=(-?\d{1,3})\.\.(-?\d{1,3})", input
        )[0]
    ]
    print(target)

    range_x = range(math.ceil(math.sqrt(abs(target[0]))) - 1, abs(target[1] + 1))
    range_y = range(-abs(target[2]) - 1, abs(target[2] - 1) - 1)

    solution = []
    space = []
    max_y = 0

    for x in range_x:
        for y in range_y:
            space.append((x, y))

    for (shot_x, shot_y) in space:
        tmp_x = shot_x
        tmp_y = shot_y
        tmp_max_y = 0

        pos_x = 0
        pos_y = 0

        while True:
            pos_x += tmp_x
            pos_y += tmp_y
            tmp_max_y = max(tmp_max_y, pos_y)

            if target[0] <= pos_x <= target[1] and target[2] <= pos_y <= target[3]:
                max_y = max(max_y, tmp_max_y)
                solution.append((shot_x, shot_y))
                break
            elif tmp_x == 0 and not target[0] <= pos_x <= target[1]:
                break
            elif pos_x > target[1] or pos_y < target[2]:
                break

            if tmp_x > 0:
                tmp_x -= 1
            elif tmp_x < 0:
                tmp_x += 1

            tmp_y -= 1

    print(len(solution))
    print(max_y)


if __name__ == "__main__":
    main()
