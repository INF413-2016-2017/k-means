# -*- coding: utf-8 -*-
# !/usr/bin/env python

import filesManagment
from algorithms import *
from utilities import *


""" Parameters """
nPoints = 2
dimension = 2
nClusters = 2


""" Points test """
data = filesManagment.generate_random_data(nPoints, dimension)
filesManagment.write_data(data, "in.csv")
p = filesManagment.read_data("in.csv", ignore_first_column=True)
D = Distance()

A = Base(p, nClusters, D.euclidean)
A.run()

displayPoints(A.C, A.c)