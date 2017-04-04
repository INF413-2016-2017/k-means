# -*- coding: utf-8 -*-
# !/usr/bin/env python

import filesManagment
from algorithms import *
from utilities import *


""" Parameters """
filename = 'words.txt'
k = 3
D = Distance()


""" Words test """
data = filesManagment.FileManager(dataType='words')
data.read(filename)

A = Base(data.data, k, D.levenshtein, data_type='words')
A.run()

display_words(A.C)
