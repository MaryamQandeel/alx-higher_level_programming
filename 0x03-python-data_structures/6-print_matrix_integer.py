#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in matrix:
        if len(matrix) == 0:
            print("$")
        elif i is len(matrix) - 1:
                    print("{:d}$".format(matrix[i]), end="\n")
        else:
            for j in range(len(i)):
                if j is len(i) - 1:
                    print("{:d}$".format(i[j]), end="\n")
                else:
                    print("{:d}".format(i[j]), end=" ")
