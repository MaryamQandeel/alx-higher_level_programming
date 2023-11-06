#!/usr/bin/python3
def print_list_integer(my_list=[]):
    len = len(my_list)
    for i in range(my_list[0], my_list[len-1]+1):
        print("{:d}".format(i))
