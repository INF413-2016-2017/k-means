# -*- coding: utf-8 -*-

from random import randint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


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

def display(C):
	if len(C[0][0]) == 2:
		for cluster in C:
			points = zip(*cluster)
			plt.scatter(points[0], points[1])
		plt.show()

	elif len(C[0][0]) == 3:
		fig = plt.figure()
		ax = Axes3D(fig)

		for cluster in C:
			points = zip(*cluster)
			ax.scatter(points[0], points[1], points[2])
		plt.show()

	else:
		raise Exception("Wrong dimension")
