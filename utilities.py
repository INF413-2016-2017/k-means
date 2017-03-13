# -*- coding: utf-8 -*-

from random import randint
import matplotlib.pyplot as plt


def distance_euclidean(X, Y):
    """
        Returns the euclidean distance between X and Y. No sqrt applied.
        X and Y are tuples of the same dimension.
    """
    d = len(X)
    if len(Y)!=d:
        raise Exception("X and Y don't have the same dimension")
    else:
        distance = 0
        for i in range(d):
            distance += (X[i]-Y[i])**2
        return distance


def getCenter(p, d):
    """
        Return the closest point to the barycenter in p.
    """

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

    B = barycenter(p,d)

    distances = [ distance_euclidean(p[i], B) for i in range(len(p)) ]
    #FIXME: Optimize the min func.
    return p[distances.index(min(distances))]


def chooseCenter_rand(x, k):
    """
        Choose k centers in x randomly.

		k: integer
		x: list of tuples
    """
    c = []

    for i in range(k):
        c.append(x.pop(randint(0,len(x)-1)))

    return c

def updateDistances(c, p):
    pLeft = p-set(c)
    k = len(c)
    L = {}

    for p in pLeft:
        L[p] = [0 for i in range(k)]
        for i in range(k):
            L[p][i] = distance_euclidean(c[i], p)
    return L


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

def updateCenters(C):
    d = len(C[0][0])
    k = len(C)
    c = [ None for i in range(k) ]

    # For each cluster, compute the new center
    for i in range(k):
        c[i] = getCenter(C[i], d)

    return c

def display(C):
    for cluster in C:
        points = zip(*cluster)
        plt.scatter(points[0], points[1])
    plt.show()
