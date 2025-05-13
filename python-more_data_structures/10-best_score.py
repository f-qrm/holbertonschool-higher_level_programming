#!/usr/bin/python3
def best_score(a_dictionary):
    max_ = 0
    cle = None
    if not a_dictionary:
        return None
    for key, score in a_dictionary.items():
        if score > max_:
            max_ = score
            cle = key
    return cle
