#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        length = 0
        return (length, None)
    else:
        lsentence = len(sentence)
        fchr = sentence[0]
        rtr_tuple = (lsentence, fchr)
        return rtr_tuple
