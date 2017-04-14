# -*- coding: utf-8 -*-
# !/usr/bin/env python

import filesManagment
from algorithms import *
from utilities import *

""" Parameters """
nPoints = 5000
dimension = 2
nClusters = 4
D = Distance()


""" Points test """
data = filesManagment.generate_random_gaussian_data(nPoints, dimension, 3)
filesManagment.write_data(data, "in.csv")
p = filesManagment.read_data("in.csv", ignore_first_column=True)

A = GeneralizedLlyod(p, nClusters, D.euclidean, iter_max=5)
A.run()

display_points(A.clusters, A.centers, dimension)  # Display the clusters and the centers. Support dimensions 2 and 3.


filesManagment.write_solution('out.csv', A.clusters)
filesManagment.write_centers('centers.csv', A.centers)






# FIXME: create a new file for this test.
""" n_cluster test """
"""
import matplotlib.pyplot as plt

totalDistance = []
cluster = [i for i in range(1,20)]

for nClusters in range(1,20):
    A = GeneralizedLlyod(data, nClusters, D.euclidean, iter_max=5)
    A.run()
    totalDistance.append(A.distMin)

    if nClusters == 1:
        display_points(A.clusters, A.centers)

plt.plot(cluster, totalDistance)
plt.show()
"""


