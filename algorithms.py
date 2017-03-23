# -*- coding: utf-8 -*-

from random import randint
import numpy as np


class Algorithm(object):
    def __init__(this, data, nClusters, dimension, distance):
        """
        Init function
        :param data:
        :param nClusters:
        :param dimension:
        :param distance: function that takes two arguments.
        """
        this.p = set(data)
        this.n = len(data)
        this.k = nClusters
        this.d = dimension
        this.c = []
        this.L = []
        this.C = []
        this.distance = distance

    def barycenter(this, L, d):
        """
            Return the coordinates of the barycenter of the tuples in the list L
        """
        n = len(L)
        B = [0 for k in range(d)]

        for point in L:
            for i in range(d):
                B[i] += point[i]

        B = map(lambda x: x / n, B)
        return tuple(B)

    def updateDistances(this):
        pLeft = this.p - set(this.c)
        this.L = {}

        for p in pLeft:
            this.L[p] = [0 for i in range(this.k)]
            for i in range(this.k):
                this.L[p][i] = this.distance(this.c[i], p)

    def pointsToClusters(this):
        """
            Assign points to the cluster of the closest center.
        """
        this.C = [[this.c[i]] for i in
                  range(this.k)]  # C[i] is the list of points in cluster i. Add the center in the list.

        for p in this.L.keys():
            this.C[np.argmin(this.L[p])].append(p)

    def run(this):
        this.chooseInitCenters()
        this.updateDistances()
        this.pointsToClusters()

        while this.stopCondition():
            this.updateCenters()
            this.updateDistances()
            this.pointsToClusters()


class Base(Algorithm):
    def __init__(this, data, nClusters, dimension, distance, max_iter=10, dataType='points'):
        super(Base, this).__init__(data, nClusters, dimension, distance)
        this.iter = 0
        this.max_iter = max_iter
        this.dataType = dataType

    def updateCenters(this):
        # For each cluster, compute the new center
        if this.dataType == 'points':
            for i in range(this.k):
                # Return the closest point to the barycenter in this.C[i].
                B = this.barycenter(this.C[i], this.d)
                distances = [this.distance(this.C[i][j], B) for j in range(len(this.C[i]))]
                this.c[i] = this.C[i][np.argmin(distances)]
        elif this.dataType == 'words':
            pass
        else:
            raise Exception("Data type not implemented")

    def chooseInitCenters(this):
        if this.dataType == 'points':
            """
                Choose k centers among the points in p randomly.
            """
            this.c = []
            pTmp = list(this.p)
            for i in range(this.k):
                this.c.append(pTmp.pop(randint(0, this.n - 1)))
        else:
            # FIXME: choose random words
            this.c = ['aquarium', 'aquatique']

    def stopCondition(this):
        this.iter += 1
        return this.iter < this.max_iter


class BaseStopUnchanged(Base):
    """
        Base algorithm, but stops when no points moved from a cluster for more than max_iter.
    """

    def __init__(this, data, nClusters, dimension, max_iter=10):
        super(BaseStopUnchanged, this).__init__(data, nClusters, dimension, max_iter)
        this.iter_stop = 0
        this.C_former = []

    def stopCondition(this):
        this.iter += 1
        if this.hasChanged():
            this.iter_stop = 0
            this.C_former = this.C
            return True
        else:
            this.iter_stop += 1
            return this.iter_stop < this.max_iter

    def hasChanged(this):
        return this.C_former != this.C
