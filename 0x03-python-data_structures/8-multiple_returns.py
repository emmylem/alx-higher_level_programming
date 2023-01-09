#!/usr/bin/python3
def multiple_returns(sentence):
    # Return length of a string first char
    if (sentence == ""):
        return (0, None)
    return (len(sentence), sentence[0])
