# -*- coding: utf-8 -*-
# !/usr/bin/env python

import filesManagment
from algorithms import *
from utilities import *


""" Points test """
nPoints = 5000
dimension = 2
nClusters = 8

data = filesManagment.generate_random_data(nPoints, dimension)
filesManagment.write_data(data, "in.csv")
p = filesManagment.read_data("in.csv", ignore_first_column=True)

D = Distance()
A = Base(p, nClusters, D.euclidean, 3)


A.run()
display(A.C, A.c)

filesManagment.write_solution('out.csv', A.C)
filesManagment.write_centers('centers.csv', A.c)



""" Words test """
data = filesManagment.FileManager(dataType='words')
data.read('words.txt')

D = Distance()
A = Base(data.data, 2, D.levenshtein,  dataType='words')
A.run()
for wList in A.C:
	for w in wList:
		print(w)
	print()
