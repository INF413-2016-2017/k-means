# -*- coding: utf-8 -*-

from random import randint
from collections import Counter
import numpy as np
import scipy.stats as stats

import itertools


class Algorithm(object):
    def __init__(this, data, n_clusters, distance, iterations=50):
        """
        :type data: object
        :type n_clusters: int
        :param data: Input data
        :param n_clusters: Number of clusters
        :param distance: function that takes two arguments.
        """
        # FIXME: Add comments.
        this.p = set(data)  # Set of data.
        this.n = len(data)  # Number of data.
        this.k = n_clusters  # Number of clusters.
        this.c = []  # List of centers.
        this.L = {}  # Dictionary of list representing the distances of each element to the centers.
        this.C = []  # List of list in which C[k] is the list of data in cluster k.
        this.distance = distance

        this.iterations = iterations

        this.distMin = 0
        this.cBest = []
        this.CBest = []

    def remember_best_result(this):
        """
        Stores the best result so far
        """

        totalDistance = 0

        for i in range(len(this.C)):
        #for each center
            for point in this.C[i]:
            #for each point related to this center
                totalDistance+=this.L[point][i]
                #add the distance between the point and the center

        #if this is the best result so far (or the 1st) we remember it
        if totalDistance < this.distMin or this.distMin == 0:
            this.cBest = this.c
            this.CBest = this.C
            this.distMin = totalDistance

    @staticmethod
    def _average(data, data_type):
        """
        Return the coordinates of the barycenter if data are points, the average word if data are words.
        :type data_type: str
        :param data_type: Indicates if the data are points or words.
        :return: Average data
        """
        if data_type == 'points':
            """
                Return the coordinates of the barycenter of the tuples in the list L
            """
            n = len(data)
            d = len(data[0])  # Number of coordinates
            B = [0 for k in range(d)]

            for point in data:
                for i in range(d):
                    B[i] += point[i]

            #FIXME: add comments or change method.
            B = map(lambda x: x / n, B)
            return tuple(B)

        elif data_type == 'words':
            """
                Return the average word from the list of words.
            """
            # FIXME: sometimes, data is empty.
            max_length = max(map(len, data))
            average_word = ['' for k in range(max_length)]

            # Make all the words the same length
            # FIXME: add comments
            for i in range(len(data)):
                n = len(data[i])
                data[i] = data[i] + (max_length - n) * ' '

            for k in range(max_length):
                listchar = [w[k] for w in data]  # List of k-th characters in each word.
                average_word[k] = Counter(listchar).most_common(1)[0][0]

            return ''.join(average_word)  # Convert to string

        else:
            raise Exception("Data type not implemented")

    def update_distances(this):
        """
        Updates the dictionary of distances.
        :return: None
        """
        pLeft = this.p - set(this.c)
        this.L = {}

        for p in pLeft:
            this.L[p] = [0 for i in range(this.k)]
            for i in range(this.k):
                this.L[p][i] = this.distance(this.c[i], p)

    def run(this):
        """
        Main loop of the algorithm
        :return: None
        """
        for i in range(this.iterations):

            this.choose_init_centers()
            this.update_distances()
            this.points_to_clusters()

            while this.stop_condition():
                this.update_centers()
                this.update_distances()
                this.points_to_clusters()

            this.remember_best_result()

            print("iteration: "+str(i+1))
            print("distance totale: "+str(this.distMin))

        this.c = this.cBest
        this.C=this.CBest


class GeneralizedLlyod(Algorithm):
    """
    Generalize Lloyd's algorithm.
    """
    def __init__(this, data, n_clusters, distance, iter_max=10, data_type='points'):
        super(GeneralizedLlyod, this).__init__(data, n_clusters, distance)
        this.iter = 0
        this.iter_max = iter_max
        this.data_type = data_type

    def choose_init_centers(this):
        """
        Choose k centers among p randomly.
        """
        this.c = []
        pTmp = list(this.p)
        for i in range(this.k):
            this.c.append(pTmp.pop(randint(0, len(pTmp) - 1)))

    def stop_condition(this):
        """
        Stop the algorithm when more than max_iter have been made.
        :return: boolean
        """
        this.iter += 1
        return this.iter < this.iter_max

    def update_centers(this):
        """
        Choose a new center for each cluster.
        :return: None.
        """
        for i in range(this.k):
            this.c[i] = this._average(this.C[i], this.data_type)  # Barycenter of average word

    def points_to_clusters(this):
        """
        Assign points to the cluster of the closest center.
        :return: None
        """
        this.C = [[] for i in range(this.k)]  # C[i] is the list of points in cluster i.

        for p in this.L.keys():
            this.C[np.argmin(this.L[p])].append(p)


class GeneralizedLlyod_clusterAsCenter(GeneralizedLlyod):
    """
    Regular k-means algorithm, but use a point belong to the cluster as a center.
    """
    def __init__(this, data, n_clusters, distance, iter_max=10, data_type='points'):
        super(GeneralizedLlyod_clusterAsCenter, this).__init__(data, n_clusters, distance, iter_max, data_type)

    def update_centers(this):
        """
        Choose new center for each cluster. Compute the average, then chose the closest to the average.
        :return: None
        """
        for i in range(this.k):
            # Return the closest point to the average in this.C[i].
            B = this._average(this.C[i], this.data_type)  # Barycenter for points, else average word
            distances = [this.distance(this.C[i][j], B) for j in range(len(this.C[i]))]
            this.c[i] = this.C[i][np.argmin(distances)]

    def points_to_clusters(this):
        """
        Assign points to the cluster of the closest center.
        :return: None
        """
        this.C = [[this.c[i]] for i in range(this.k)]  # C[i]: list of points in cluster i. Add the center in the list.

        for p in this.L.keys():
            this.C[np.argmin(this.L[p])].append(p)


class GeneralizedLlyod_stopUnchanged(GeneralizedLlyod):
    """
    Base algorithm, but stops when no points changed of cluster.
    """
    def __init__(this, data, n_clusters, distance, iter_max=10, data_type='points'):
        super(GeneralizedLlyod_stopUnchanged, this).__init__(data, n_clusters, distance, iter_max, data_type)
        this.c_former = []

    def stop_condition(this):
        """
        Stop the algorithm when no points changed of cluster.
        Compare the list of center instead of the clusters: faster.
        :return: boolean
        """
        if this.c_former != this.c:
            this.c_former = this.c
            return True
        else:
            return False

class G_means:
    def __init__(this, data, alpha, distance):
        this.data = data
        this.alpha = alpha
        this.distance = distance
        this.c = []

    @staticmethod
    def gaussian_test(data):
        return stats.normaltest(data)

    def run(this):
        k = 1
        k_former = -1
        centers = [point]

        if k_former != k:
            k_former = k
            k_means = GeneralizedLlyod(this.data, k, this.distance, centers)

            for cluster in k_means.C:
                p = this.gaussian_test(cluster)
                if p < 0.5:
                    centers.append(new_center)
                    k+=1
