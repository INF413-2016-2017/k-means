# -*- coding: utf-8 -*-
# !/usr/bin/env python

import filesManagment
from algorithms import *
from utilities import *

""" Parameters """
nPoints = 5000
dimension = 2
nClusters = 5
D = Distance()


""" Points test """
data = filesManagment.generate_random_gaussian_data(nPoints, dimension, 5)
# data = filesManagment.generate_random_data(nPoints, dimension)

filesManagment.write_data(data, "in.csv")
p = filesManagment.read_data("in.csv", ignore_first_column=True)

A = GeneralizedLlyod(p, nClusters, D.euclidean, iter_max=5)
A.run()

B = GeneralizedLlyod_clusterAsCenter(p, nClusters, D.euclidean, iter_max=5)
B.run()

C = GeneralizedLlyod_stopUnchanged(p, nClusters, D.euclidean, iter_max=5)
C.run()

# Display the clusters and the centers. Support dimensions 2 and 3.
display_points(A.clusters, A.centers, dimension)
display_points(B.clusters, B.centers, dimension)
display_points(C.clusters, C.centers, dimension)


# Write the solution
filesManagment.write_solution('out.csv', A.clusters)
filesManagment.write_centers('centers.csv', A.centers)
