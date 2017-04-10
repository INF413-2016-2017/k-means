# -*- coding: utf-8 -*-
# !/usr/bin/env python

import filesManagment
from algorithms import *
from utilities import *

import matplotlib.pyplot as plt

""" Parameters """
nPoints = 5000

dimension = 2
#nClusters = 4
D = Distance()


""" Points test """
data = filesManagment.generate_random_gaussian_data(nPoints, dimension, 10)
filesManagment.write_data(data, "in.csv")
p = filesManagment.read_data("in.csv", ignore_first_column=True)

totalDistance = []
cluster = [i for i in range(1,20)]

for nClusters in range(1,20):
    A = GeneralizedLlyod(p, nClusters, D.euclidean, iter_max=5)
    A.run()
    totalDistance.append(A.distMin)

    if nClusters == 1:
        display_points(A.C, A.c)

plt.plot(cluster, totalDistance)
plt.show()



"""
filesManagment.write_solution('out.csv', A.C)
filesManagment.write_centers('centers.csv', A.c)
"""
