# -*- coding: utf-8 -*-
# !/usr/bin/env python

import filesManagment
from algorithms import *
from utilities import *
import matplotlib.pyplot as plt

""" Parameters """
nPoints = 5000
dimension = 2
D = Distance()


""" G-means points test """
data = filesManagment.generate_random_gaussian_data(nPoints, dimension, 6)

filesManagment.write_data(data, "in.csv")
p = filesManagment.read_data("in.csv", ignore_first_column=True)

g_means = G_means(p, 0.055, D.euclidean)
g_means.run()

print("Number of clusters: "+str(g_means.k))
print("Clusters: "+str(g_means.clusters))
print("Centers: "+str(g_means.centers))
display_points(g_means.clusters, g_means.centers, dimension)


# filesManagment.write_solution('out.csv', A.clusters)
# filesManagment.write_centers('centers.csv', A.centers)