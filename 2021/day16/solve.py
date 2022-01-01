import sys
from functools import reduce


def getData():
    with open(sys.argv[1]) as f:
        return f.read().splitlines()


def product(v):
    return reduce(lambda a, b: a * b, v)


def gt(v):
    return int(v[0] > v[1])


def lt(v):
    return int(v[0] < v[1])


def eq(v):
    return int(v[0] == v[1])


exp = {
    0: sum,
    1: product,
    2: min,
    3: max,
    5: gt,
    6: lt,
    7: eq,
}


class PacketStream:
    index = 0
    sum_of_versions = 0
    total = 0

    def __init__(self, data):
        self.data = []

        for x in data:
            self.data.extend(str(format((int(x, 16)), "b")).zfill(4))

    def takeX(self, x, raw=False):
        result = self.data[self.index : self.index + x]
        self.index += x
        return "".join(result) if raw else int("".join(result), 2)

    def parser(self):
        pv = self.takeX(3)
        self.sum_of_versions += pv

        pt = self.takeX(3)

        if pt == 4:
            payload = ""
            while self.takeX(1):
                payload += self.takeX(4, True)
            payload += self.takeX(4, True)

            return int(payload, 2)

        else:
            lt = self.takeX(1)

            values = []
            if lt == 0:
                ll = self.takeX(15)

                l = self.index + ll
                while self.index < l:
                    values.append(self.parser())

            else:
                lc = self.takeX(11)

                for x in range(lc):
                    values.append(self.parser())

            return exp[pt](values)


def main():
    input = getData()

    row = 0
    if len(sys.argv) > 2:
        row = int(sys.argv[2])

    stream = PacketStream(input[row])
    result = stream.parser()

    print(input[row])
    print("sum_of_versions", stream.sum_of_versions)
    print("total", result)


if __name__ == "__main__":
    main()
