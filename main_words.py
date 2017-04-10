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
data = filesManagment.read_data("words.txt", data_type='words')

A = GeneralizedLlyod(data, k, D.levenshtein, data_type='words', iter_max=5)
A.run()

display_words(A.C)
