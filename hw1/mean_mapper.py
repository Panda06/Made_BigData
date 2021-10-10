#!/usr/bin/python3

import sys


def read_input(file):
    for line in file:
        yield line.split(",")


def main():
    data = read_input(sys.stdin)
    price_sum, count = 0, 0
    for line in data:
        try:
            if line[-7] is None:
                continue
            price = float(line[-7])
            price_sum += price
            count += 1
        except (IndexError, ValueError):
            pass
    if count == 0:
        mean = 0
    else:
        mean = price_sum / count
    print("{},{}".format(count, mean))


if __name__ == "__main__":
    main()
