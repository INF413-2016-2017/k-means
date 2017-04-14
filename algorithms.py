# -*- coding: utf-8 -*-

from random import randint, random
from collections import Counter
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


class Algorithm(object):
    def __init__(this, data, n_clusters, distance):
        """
        :type data: object
        :type n_clusters: int
        :param data: Input data
        :param n_clusters: Number of clusters
        :param distance: function that takes two arguments.
        """
        # FIXME: Add comments.
        this.data = set(data)  # Set of data.
        this.n = len(data)  # Number of data.
        this.k = n_clusters  # Number of clusters.
        this.centers = []  # List of centers.
        this.distances = {}  # Dictionary of list representing the distances of each element to the centers.
        this.clusters = []  # List of list in which clusters[k] is the list of data in cluster k.
        this.distance = distance

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
                Return the coordinates of the barycenter of the tuples in the list distances
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

        for p in this.data:
            this.distances[p] = [0 for i in range(this.k)]
            for i in range(this.k):
                this.distances[p][i] = this.distance(this.centers[i], p)

    def run(this):
        """
        Main loop of the algorithm
        :return: None
        """

        this.choose_init_centers()
        this.update_distances()
        this.points_to_clusters()

        while this.stop_condition():
            this.update_centers()
            this.update_distances()
            this.points_to_clusters()


class AverageResults(Algorithm):
    def __init__(this, data, n_clusters, distance, iterations=20):
        """
        Allows to launch an algorithm iterations times, and keep the best result among all solutions produced.
        :type data: object
        :type n_clusters: int
        :param data: Input data
        :param n_clusters: Number of clusters
        :param distance: function that takes two arguments.
        :param iterations: Number of times to launch the algorithm.
        """

        super(AverageResults, this).__init__(data, n_clusters, distance)

        this.iterations = iterations
        this.distMin = 0 # Best sum of distances between points and their center
        this.centers_best = [] # Best centers
        this.clusters_best = [] # Best clusters

    def remember_best_result(this):
        """
        Stores the best result so far
        """

        totalDistance = 0

        for cluster in range(len(this.clusters)):
            for point in this.clusters[i]:
                totalDistance += this.distances[point][i]

        # If this is the best result so far (or the 1st) we remember it
        if totalDistance < this.distMin or this.distMin == 0:
            this.centers_best = this.centers
            this.clusters_best = this.clusters
            this.distMin = totalDistance

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

        this.centers = this.cBest
        this.clusters=this.CBest


class GeneralizedLlyod(Algorithm):
    """
    Generalize Lloyd's algorithm.
    """
    def __init__(this, data, n_clusters, distance, iter_max=10, data_type='points', centers=None):
        super(GeneralizedLlyod, this).__init__(data, n_clusters, distance)
        this.iter = 0
        this.iter_max = iter_max
        this.data_type = data_type
        this.centers = centers

    @staticmethod
    def random_point(dimension):
        point = []
        for j in range(dimension):
            point.append(random())
        return tuple(point)

    def choose_init_centers(this):
        """
        Choose k centers randomly.
        """

        if this.centers is not None:
            if len(this.centers) != this.k:
                raise Exception("Number of centers provided incorrect.")
        else:
            this.centers = []
            if this.data_type == "points":

                # Get the dimension
                for e in this.data:
                    break
                d = len(e)

                for i in range(this.k):
                    this.centers.append(this.random_point(d))
            else:
                # TODO: add words data type
                raise Exception("Data type not implemented.")

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
        # FIXME: sometimes, a cluster does not contain any point. Hence, the call to _average will result in an error.
        for i in range(this.k):
            if this.clusters[i] == []:
                for e in this.data:
                    break
                this.centers[i] = this.random_point(len(e))
            else:
                this.centers[i] = this._average(this.clusters[i], this.data_type)  # Barycenter or average word

    def points_to_clusters(this):
        """
        Assign points to the cluster of the closest center.
        :return: None
        """
        this.clusters = [[] for i in range(this.k)]  # clusters[i] is the list of points in cluster i.

        for p in this.distances.keys():
            this.clusters[np.argmin(this.distances[p])].append(p)


class GeneralizedLlyod_clusterAsCenter(GeneralizedLlyod):
    """
    Regular k-means algorithm, but use a point belong to the cluster as a center.
    """
    def __init__(this, data, n_clusters, distance, iter_max=10, data_type='points'):
        super(GeneralizedLlyod_clusterAsCenter, this).__init__(data, n_clusters, distance, iter_max, data_type)

    def choose_init_centers(this):
        """
        Choose k centers among data randomly.
        """

        if this.centers is not None:
            if len(this.centers) != this.k:
                raise Exception("Number of centers provided incorrect.")
        else:
            this.centers = []
            pTmp = list(this.data)
            for i in range(this.k):
                this.centers.append(pTmp.pop(randint(0, len(pTmp) - 1)))

    def update_centers(this):
        """
        Choose new center for each cluster. Compute the average, then chose the closest to the average.
        :return: None
        """
        for i in range(this.k):
            # Return the closest point to the average in this.clusters[i].
            B = this._average(this.clusters[i], this.data_type)  # Barycenter for points, else average word
            distances = [this.distance(this.clusters[i][j], B) for j in range(len(this.clusters[i]))]
            this.centers[i] = this.clusters[i][np.argmin(distances)]

    def points_to_clusters(this):
        """
        Assign points to the cluster of the closest center.
        :return: None
        """
        this.clusters = [[this.centers[i]] for i in range(this.k)]  # clusters[i]: list of points in cluster i. Add the center in the list.

        for p in this.distances.keys():
            this.clusters[np.argmin(this.distances[p])].append(p)


class GeneralizedLlyod_stopUnchanged(GeneralizedLlyod):
    """
    Base algorithm, but stops when no points changed of cluster.
    FIXME: doesn't work. Strange behavior.
    """
    def __init__(this, data, n_clusters, distance, iter_max=10, data_type='points'):
        super(GeneralizedLlyod_stopUnchanged, this).__init__(data, n_clusters, distance, iter_max, data_type)
        this.centers_former = []

    def stop_condition(this):
        """
        Stop the algorithm when no points changed of cluster.
        Compare the list of center instead of the clusters: faster.
        :return: boolean
        """
        if this.centers_former != this.centers:
            this.centers_former = this.centers
            return True
        else:
            return False


class G_means:
    """
    Choose the first center randomly: first element of the data provided.
    """
    def __init__(this, data, alpha, distance):
        this.data = data
        this.alpha = alpha
        this.distance = distance
        this.k = 1
        this.centers = []
        this.clusters = []

    def is_gaussian(this, data):
        s, p = stats.normaltest(data, axis=None)
        if this.alpha < p:
            points = zip(*data)
            plt.scatter(points[0], points[1], s=10)
            plt.show()
        return this.alpha < p

    def run(this):
        k_former = -1

        while k_former != this.k:
            k_former = this.k
            k_means = GeneralizedLlyod(this.data, this.k, this.distance)
            k_means.run()

            this.centers = k_means.centers
            this.clusters = k_means.clusters

            for cluster in k_means.clusters:
                if len(cluster) >= 20 and not this.is_gaussian(cluster):
                    this.k += 1
            print("Current cluster size: "+str(this.k))