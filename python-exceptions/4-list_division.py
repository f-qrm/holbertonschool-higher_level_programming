#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    total = []
    for i in range(list_length):
        try:
            total_div = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            total_div = 0
        except (TypeError, ValueError):
            print("wrong type")
            total_div = 0
        except IndexError:
            print("out of range")
            total_div = 0
        finally:
            total.append(total_div)
    return total
