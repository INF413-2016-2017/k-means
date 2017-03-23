# -*- coding: utf-8 -*-
# !/usr/bin/env python

import filesManagment
from algorithms import *
from utilities import *


""" Parameters """
filename = 'words.txt'
k = 2


""" Words test """
data = filesManagment.FileManager(dataType='words')
data.read(filename)
D = Distance()

A = Base(data.data, k, D.levenshtein,  dataType='words')
A.run()

displayWords(A.C)