# -*- coding: utf-8 -*-

from random import randint
import matplotlib.pyplot as plt

def barycenter(L, d):
    """
        Return the coordinates of the barycenter of the tuples in the list L
    """
    n = len(L)
    B = [0 for k in range(d)]

    for point in L:
        for i in range(d):
            B[i] += point[i]

    B = map(lambda x: x/n, B)
    return tuple(B)


def display2D(C):
	if len(C[0][0]) != 2:
		raise Exception("Wrong dimension")

	for cluster in C:
		points = zip(*cluster)
		plt.scatter(points[0], points[1])
	plt.show()
