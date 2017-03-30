# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt
import distance


def display_points(C, c):
    """
    Display the cluster using a different color for each cluster.
    :param C: List of clusters.
    :param c: List of centers.
    :return: None
    """
    if len(C[0][0]) == 2:
        for cluster in C:
            points = zip(*cluster)
            plt.scatter(points[0], points[1], s=10)

        for center in c:
            plt.scatter(*center, marker='*', s=200, color='black')
        plt.show()

    elif len(C[0][0]) == 3:
        fig = plt.figure()
        ax = Axes3D(fig)

        for cluster in C:
            points = zip(*cluster)
            ax.scatter(points[0], points[1], points[2], s=10)
        plt.show()

    else:
        raise Exception("Wrong dimension")


def display_words(C):
    """
    Display the cluster of words.
    :param C: List of clusters.
    :return: None
    """
    for cluster in C:
        print(cluster)


class Distance:
    """
    Implements the different distances available.
    """
    def __init__(this):
        def euclidean(X, Y):
            """
                Returns the euclidean distance between X and Y. No sqrt applied.
                X and Y are tuples of the same dimension.
            """
            if len(X) != len(Y):
                raise Exception("Arguments do not have the same dimension")
            else:
                d = len(X)
                s = 0
                for i in range(d):
                    s += (X[i] - Y[i]) ** 2
                return sqrt(s)

        def levenshtein(X, Y):
            """
                Returns the Levenshtein distance between X and Y.
                X and Y are strings.
            """
            return distance.levenshtein(X, Y, normalized=True)

        this.euclidean = euclidean
        this.levenshtein = levenshtein
