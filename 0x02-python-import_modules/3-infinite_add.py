#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    argc = len(sys.argv)
    for x in range(1, argc):
        sum += int(sys.argv[x])
    print(sum)
