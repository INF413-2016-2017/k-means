# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This file test a set of points for a gaussian distribution.
"""

import filesManagment
import matplotlib.pyplot as plt
import scipy.stats as stats

""" Parameters """
nPoints = 5000
dimension = 2

""" Gaussian test """
while True:
    data = filesManagment.generate_random_gaussian_data(nPoints, dimension, 2)
    filesManagment.write_data(data, "in.csv")
    data = filesManagment.read_data("in.csv", ignore_first_column=True)

    dim = zip(*data)
    print(stats.anderson_ksamp(data))

    points = zip(*data)
    plt.scatter(points[0], points[1])
    plt.show()
