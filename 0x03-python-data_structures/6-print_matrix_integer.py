#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for d1 in matrix:
        for d2 in range(len(d1)):
            print(
                "{:d}".format(d1[d2]),
                end="" if d2 == len(d1) - 1 else " ")
        print("")
