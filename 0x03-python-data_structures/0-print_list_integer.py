#!/usr/bin/python3
def print_list_integer(my_list=[]):
    len = my_list.length
    for i in range(my_list[0], my_list[len+1]):
        print("{:d}\n".format(i))
