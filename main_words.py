# -*- coding: utf-8 -*-
# !/usr/bin/env python

import filesManagment
from algorithms import *
from utilities import *


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
