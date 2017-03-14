# -*- coding: utf-8 -*-
# !/usr/bin/env python

import filesManagment
from algorithms import *


nPoints=5000
dimension=2
nClusters=10

data = filesManagment.generate_random_data(nPoints, dimension)
filesManagment.write_data(data, "in.csv")
p = filesManagment.read_data("in.csv", ignore_first_column=True)

A = Base(p, nClusters, dimension, 10)
A.run()
display(A.C)

filesManagment.write_solution('out.csv', A.C)
filesManagment.write_centers('centers.csv', A.c)
