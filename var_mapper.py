#!/usr/bin/python3

import sys

def read_input(file):
    for line in file:
        yield line.split(",")

def main():
    data = read_input(sys.stdin)
    price_sum, count, squared_price_sum = 0, 0, 0
    for line in data:
        try:
            if line[-7] is None:
                continue
            price = float(line[-7])
            price_sum += price
            squared_price_sum += price ** 2
            count += 1
        except (IndexError,ValueError):
            pass
    if count == 0:
        mean, var = 0, 0
    else:
        mean = price_sum / count
        var = squared_price_sum / count - mean ** 2
    print("{},{},{}".format(count, mean, var))


if __name__ == "__main__":
    main()
