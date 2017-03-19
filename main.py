# -*- coding: utf-8 -*-
# !/usr/bin/env python

import filesManagment
from algorithms import *

"""
nPoints=2500
dimension=3
nClusters=3

data = filesManagment.generate_random_data(nPoints, dimension)
filesManagment.write_data(data, "in.csv")
p = filesManagment.read_data("in.csv", ignore_first_column=True)

A = BaseStopUnchanged(p, nClusters, dimension, 3)
A.run()
display(A.C)


print(A.iter)

filesManagment.write_solution('out.csv', A.C)
filesManagment.write_centers('centers.csv', A.c)
"""


data = filesManagment.FileManager(dataType='words')
data.read('words.txt')

A = BaseWords(data.data, 3, 1)
A.run()
for wList in A.C:
	for w in wList:
		print(w)
	print()
