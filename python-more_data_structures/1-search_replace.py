#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new1_list = []
    for i in my_list:
        if i == search:
            new1_list.append(replace)
        else:
            new1_list.append(i)
    return new1_list
