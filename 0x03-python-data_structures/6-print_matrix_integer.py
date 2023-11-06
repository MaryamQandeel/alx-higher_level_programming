#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print None
    for i in matrix:
        if len(matrix) == 0:
            print("$")
        else:
            for j in range(len(i)):
                if j == i[len(i)-1]:
                    print("{:d}".format(i[j]), end="\n")
                else:
                    print("{:d}".format(i[j]), end=" ")
