#!/usr/bin/python3
if (__name__ == "__main__"):
    import sys

    find = len(sys.argv) - 1
    if (find == 0):
        print("0 arguments.")
    elif (find == 1):
        print("1 arguments:")
    else:
        print("{} arguments:".format(find))
    for i in range(find):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
