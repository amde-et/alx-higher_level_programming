#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    Newsquare = []
    i = 0
    for x in matrix:
        Newsquare.append([])
        for y in matrix[i]:
            Newsquare[i].append(y**2)
        i += 1
    return (Newsquare)
