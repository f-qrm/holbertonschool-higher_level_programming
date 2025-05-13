#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set(my_list)
    total = 0
    for i in unique_integers:
        total += i
    return(total)
