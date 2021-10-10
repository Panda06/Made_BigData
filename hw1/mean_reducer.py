#!/usr/bin/python3

import sys

def read_input(file):
    for line in file:
        yield line.split(",")

def main():
    mean, count = 0, 0
    data = read_input(sys.stdin)
    for line in data:
        ck, mk= map(float, line)
        if count == 0 and ck == 0:
            continue
        mean = (mean * count + ck * mk) 
        count += ck
        mean /= count
    print("mean\t{}".format(mean))



if __name__ == "__main__":
    main()
