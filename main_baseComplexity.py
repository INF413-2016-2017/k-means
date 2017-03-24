# -*- coding: utf-8 -*-
# !/usr/bin/env python

import filesManagment
from algorithms import *
from utilities import *
import time
import matplotlib.pyplot as plt


""" Parameters """
nPointsMin, nPointsMax = 500, 5000
step = 20
iterNumber = 25
dimension = 2
nClusters = 5
D = Distance()
times = []

""" Complexity test for nPoints """
for nPoints in range(nPointsMin, nPointsMax, iterNumber):
    avgTime = 0

    for iter in range(iterNumber):
        data = filesManagment.generate_random_data(nPoints, dimension)
        filesManagment.write_data(data, "in.csv")
        p = filesManagment.read_data("in.csv", ignore_first_column=True)

        t0 = time.time()
        A = Base(p, nClusters, D.euclidean)
        A.run()
        avgTime += time.time()-t0

    times.append(avgTime/iterNumber)

plt.plot(range(nPointsMin, nPointsMax, iterNumber), times)
plt.xlabel('Nombre de points')
plt.ylabel('Temps en secondes')
plt.show()




""" Parameters """
nPoints = 2000
iterNumber = 2
dimension = 2
nClustersMin, nClusterMax = 2, 100
D = Distance()
times = []

""" Complexity test for nCluster """
for nCluster in range(nClustersMin, nClusterMax):
    avgTime = 0

    for iter in range(iterNumber):
        data = filesManagment.generate_random_data(nPoints, dimension)
        filesManagment.write_data(data, "in.csv")
        p = filesManagment.read_data("in.csv", ignore_first_column=True)

        t0 = time.time()
        A = Base(p, nClusters, D.euclidean)
        A.run()
        avgTime += time.time()-t0

    times.append(avgTime/iterNumber)

plt.plot(range(nClustersMin, nClusterMax), times)
plt.xlabel('Nombre de cluster')
plt.ylabel('Temps en secondes')
plt.show()