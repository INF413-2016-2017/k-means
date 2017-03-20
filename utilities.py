# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def display(C, c):
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
