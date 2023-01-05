#!/usr/bin/python3
if (__name__ == "__main__"):
    import hidden_4

    names_all = dir(hidden_4)
    for x in names_all:
        if x[:2] != "__":
            print(x)
