#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    symbol = "__"
    for x in range(len(names)):
        if symbol not in names[x]:
            print(names[x])
