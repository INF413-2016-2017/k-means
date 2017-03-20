# -*- coding: utf-8 -*-
# !/usr/bin/env python

import filesManagment
from algorithms import *
from utilities import *

""" Points test """

nPoints = 500
dimension = 2
nClusters = 5

data = filesManagment.generate_random_data(nPoints, dimension)
filesManagment.write_data(data, "in.csv")
p = filesManagment.read_data("in.csv", ignore_first_column=True)

A = Base(p, nClusters, dimension, 3)
A.run()
display(A.C, A.c)

print(A.iter)

filesManagment.write_solution('out.csv', A.C)
filesManagment.write_centers('centers.csv', A.c)

""" Words test """
"""
data = filesManagment.FileManager(dataType='words')
data.read('words.txt')

A = Base(data.data, 2, 1, dataType='words')
A.run()
for wList in A.C:
	for w in wList:
		print(w)
	print()
"""
