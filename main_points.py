# -*- coding: utf-8 -*-
# !/usr/bin/env python

import filesManagment
from algorithms import *
from utilities import *


""" Parameters """
nPoints = 5000
dimension = 2
nClusters = 8


""" Points test """
data = filesManagment.generate_random_data(nPoints, dimension)
filesManagment.write_data(data, "in.csv")
p = filesManagment.read_data("in.csv", ignore_first_column=True)
D = Distance()

A = Base(p, nClusters, D.euclidean, 3)
A.run()

displayPoints(A.C, A.c)

filesManagment.write_solution('out.csv', A.C)
filesManagment.write_centers('centers.csv', A.c)