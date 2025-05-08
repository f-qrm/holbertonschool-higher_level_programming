#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            result += "{}".format(chr(ord(c) - 32))
        else:
            result += "{}".format(c)
    print(result)
