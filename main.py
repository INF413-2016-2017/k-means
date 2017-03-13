# -*- coding: utf-8 -*-
# !/usr/bin/env python

import filesManagment
from algorithms import *


nPoints=500
dimension=3
nClusters=2

data = filesManagment.generate_random_data(nPoints, dimension)
filesManagment.write_data(data, "in.csv")
p = filesManagment.read_data("in.csv", ignore_first_column=True)

A = alg0(p, nClusters, dimension)
A.run()
display3D(A.C)

filesManagment.write_solution('out.csv', A.C)
filesManagment.write_centers('centers.csv', A.c)
