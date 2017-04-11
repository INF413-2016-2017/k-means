# -*- coding: utf-8 -*-
# !/usr/bin/env python

import filesManagment
from algorithms import *
from utilities import *
import matplotlib.pyplot as plt

""" Parameters """
nPoints = 500

dimension = 2
nClusters = 4
D = Distance()


""" Points test """
data = filesManagment.generate_random_gaussian_data(nPoints, dimension, 1)
filesManagment.write_data(data, "in.csv")
data = filesManagment.read_data("in.csv", ignore_first_column=True)

A = G_means(None, None, None)
s, p = A.gaussian_test(data)

print(s, p)

points = zip(*data)
plt.scatter(points[0], points[1])
plt.show()


"""
filesManagment.write_data(data, "in.csv")
p = filesManagment.read_data("in.csv", ignore_first_column=True)

A = GeneralizedLlyod(p, nClusters, D.euclidean, iter_max=5)
A.run()

display_points(A.clusters, A.centers)


filesManagment.write_solution('out.csv', A.clusters)
filesManagment.write_centers('centers.csv', A.centers)
"""
