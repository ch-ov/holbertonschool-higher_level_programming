#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print(f"{len(sys.argv) - 1} arguments.")
    elif len(sys.argv) == 2:
        print(f"{len(sys.argv) - 1} argument:")
    else:
        print(f"{len(sys.argv) - 1} arguments:")
    for x in range(len(sys.argv)):
        if x == 0:
            continue
        print(f"{x}: {sys.argv[x]}")
