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



def pointsToClusters(L, c):
    """
        Assign points to the cluster of the closest center.
    """
    n = len(L)
    k = len(c)
    C = [ [c[i]] for i in range(k) ]                                            # C[i] is the list of points in cluster i. Add the center in the list.

    for p in L.keys():
        #FIXME: optimize the min research: write a function
        center = min(L[p])
        i = L[p].index(center)
        C[i].append(p)
    return C


def display2D(C):
	if len(C[0][0]) != 2:
		raise Exception("Wrong dimension")

	for cluster in C:
		points = zip(*cluster)
		plt.scatter(points[0], points[1])
	plt.show()
