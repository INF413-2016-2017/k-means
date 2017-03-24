# -*- coding: utf-8 -*-

from random import randint
from collections import Counter
import numpy as np


class Algorithm(object):
    def __init__(this, data, nClusters, distance):
        """
        :param data: list
        :param nClusters: int
        :param distance: function that takes two arguments.
        """
        #FIXME: Add comments.
        this.p = set(data)
        this.n = len(data)
        this.k = nClusters
        this.c = []
        this.L = []
        this.C = []
        this.distance = distance

    def average(this, L, dataType):
        if dataType == 'points':
            """
                Return the coordinates of the barycenter of the tuples in the list L
            """
            n = len(L)
            d = len(L[0])  # Number of coordinates
            B = [0 for k in range(d)]

            for point in L:
                for i in range(d):
                    B[i] += point[i]

            #FIXME: add comments or change method.
            B = map(lambda x: x / n, B)
            return tuple(B)

        elif dataType == 'words':
            """
                Return the average word from the list of words.
            """
            maxLength = max(map(len, L))
            averageWord = ['' for k in range(maxLength)]

            # Make all the words the same length
            #FIXME: add comments
            for i in range(len(L)):
                n = len(L[i])
                L[i] = L[i] + (maxLength - n) * ' '

            for k in range(maxLength):
                listChar = [w[k] for w in L]  # List of k-th characters in each word.
                averageWord[k] = Counter(listChar).most_common(1)[0][0]

            return ''.join(w)  # Convert to string

        else:
            raise Exception("Data type not implemented")

    def updateDistances(this):
        """
        Updates the list of distances.
        :return: None
        """
        pLeft = this.p - set(this.c)
        this.L = {}

        for p in pLeft:
            this.L[p] = [0 for i in range(this.k)]
            for i in range(this.k):
                this.L[p][i] = this.distance(this.c[i], p)

    def pointsToClusters(this):
        """
        Assign points to the cluster of the closest center.
        :return: None
        """
        this.C = [[this.c[i]] for i in range(this.k)]  # C[i] is the list of points in cluster i. Add the center in the list.

        for p in this.L.keys():
            this.C[np.argmin(this.L[p])].append(p)

    def run(this):
        """
        Main loop of the algorithm
        :return: None
        """
        this.chooseInitCenters()
        this.updateDistances()
        this.pointsToClusters()

        while this.stopCondition():
            this.updateCenters()
            this.updateDistances()
            this.pointsToClusters()


class Base(Algorithm):
    """
    Regular k-means algorithm.
    """
    def __init__(this, data, nClusters, distance, iter_max=10, dataType='points'):
        super(Base, this).__init__(data, nClusters, distance)
        this.iter = 0
        this.iter_max = iter_max
        this.dataType = dataType

    def updateCenters(this):
        """
        Choose new center for each cluster.
        :return: None
        """
        for i in range(this.k):
            # Return the closest point to the average in this.C[i].
            B = this.average(this.C[i], this.dataType)  # Barycenter for points, else average word
            distances = [this.distance(this.C[i][j], B) for j in range(len(this.C[i]))]
            this.c[i] = this.C[i][np.argmin(distances)]


    def chooseInitCenters(this):
        """
        Choose k centers among p randomly.
        """
        this.c = []
        pTmp = list(this.p)
        for i in range(this.k):
            this.c.append(pTmp.pop(randint(0, len(pTmp) - 1)))


    def stopCondition(this):
        """
        Stop the algorithm when more than max_iter have been made.
        :return: boolean
        """
        this.iter += 1
        return this.iter < this.iter_max


class BaseStopUnchanged(Base):
    """
    Base algorithm, but stops when no points moved from a cluster for more than max_iter.
    """
    def __init__(this, data, nClusters, iter_max=10):
        super(BaseStopUnchanged, this).__init__(data, nClusters, iter_max)
        this.iter_stop = 0
        this.C_former = []

    def stopCondition(this):
        """
        Stop the algorithm when no points moved from a cluster for more than max_iter.
        :return: boolean
        """
        # FIXME: check if useful
        this.iter += 1
        if this.hasChanged():
            this.iter_stop = 0
            this.C_former = this.C
            return True
        else:
            this.iter_stop += 1
            return this.iter_stop < this.iter_max

    def hasChanged(this):
        """
        Indicated if a point changed of cluster.
        :return: boolean
        """
        # FIXME: use c instead of C ?
        return this.C_former != this.C

class Base2(Base):
    """
    Regular k-means algorithm, but the centers are not in the dataset only barycenter.
    """
    def __init__(this, data, nClusters, distance, iter_max=10, dataType='points'):
        super(Base2, this).__init__(data, nClusters, distance, iter_max, dataType)

    def updateCenters(this):
        """
        Choose a new center for each cluster.
        :return: None.
        """
        for i in range(this.k):
            this.c[i] = this.average(this.C[i], this.dataType) # Barycenter of average word

    def pointsToClusters(this):
        """
        Assign points to the cluster of the closest center.
        :return: None
        """
        this.C = [[] for i in range(this.k)]  # C[i] is the list of points in cluster i.

        for p in this.L.keys():
            this.C[np.argmin(this.L[p])].append(p)