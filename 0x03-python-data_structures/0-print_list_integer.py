#!/usr/bin/python3
def print_list_integer(my_list=[]):
    l = len(my_list)
    for i in range(my_list[0], my_list[l-1]):
        print("{:d}".format(i))
