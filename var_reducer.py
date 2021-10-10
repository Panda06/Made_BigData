#!/usr/bin/python3

import sys

def read_input(file):
    for line in file:
        yield line.split(",")

def main():
    mean, count, var = 0, 0, 0
    data = read_input(sys.stdin)
    for line in data:
        ck, mk, vk = map(float, line)
        if count == 0 and ck == 0:
            continue
        var = (var * count + vk * ck) / (count + ck) 
        var += count * ck * ((mean - mk) / (count + ck)) ** 2
        mean = (mean * count + mk * ck) 
        count += ck
        mean /= count

    print("var,{}".format(var))



if __name__ == "__main__":
    main()
