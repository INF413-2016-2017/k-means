# -*- coding: utf-8 -*-
# !/usr/bin/env python

import filesManagment
from algorithms import *
from utilities import *
import random


""" Parameters """
nPoints = 5000

dimension = 2
nClusters = 4
D = Distance()


""" Points test """
data = filesManagment.generate_random_gaussian_data2(nPoints, dimension, 4)
filesManagment.write_data(data, "in.csv")
p = filesManagment.read_data("in.csv", ignore_first_column=True)

A = GeneralizedLlyod(p, nClusters, D.euclidean, iter_max=10)
A.run()

display_points(A.C, A.c)

filesManagment.write_solution('out.csv', A.C)
filesManagment.write_centers('centers.csv', A.c)
