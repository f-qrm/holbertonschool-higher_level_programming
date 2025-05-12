#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    copy_my_list = my_list[:]
    result = []
    for i in copy_my_list:
        if i % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
