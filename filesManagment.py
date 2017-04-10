# -*- coding: utf-8 -*-

import random
import numpy as np


def read_data(filename, skip_first_line=False, ignore_first_column=False, data_type='points'):
    """
    Loads data from a csv file and returns the corresponding list. See provided input files for format convention.

    :param filename: csv file name.

    :param skip_first_line: if True, the first line is not read. Default value: False.

    :param ignore_first_column: if True, the first column is ignored. Default value: False.

    :param data_type: either 'points' or 'words'.

    :return: a list of data.
    """

    f = open(filename, 'r')
    if skip_first_line:
        f.readline()

    data = []

    if data_type == 'points':
        for line in f:
            line = line.split(",")
            line[1:] = [float(x) for x in line[1:]]
            if ignore_first_column:
                line = line[1:]
            data.append(tuple(line))
    else:
        for line in f:
            line = line.split(' ')
            data.append(line[0].strip())
    f.close()
    return data


def write_data(data, filename):
    """
    Writes data in a csv file.

    :param data: a list of lists
    :param filename: the path of the file in which data is written.
    The file is created if necessary; if it exists, it is overwritten.
    """
    # If you're curious, look at python's module csv instead, which offers
    # more powerful means to write (and read!) csv files.
    f = open(filename, 'w')
    for item in data:
        f.write(','.join([repr(x) for x in item]))
        f.write('\n')
    f.close()


def generate_random_data(nb_objs, nb_attrs):
    """
    Generates a matrix of random data.
    :return: a matrix with nb_objs rows and nb_attrs+1 columns. 
    The 1st column is filled with line numbers (integers, from 1 to nb_objs).
    """
    data = []
    for i in range(nb_objs):
        line = [i + 1] + map(lambda x: random.random(), range(nb_attrs))
        data.append(tuple(line))
    return data


def generate_random_gaussian_data(nb_objs, nb_attrs, k):
    """
    Generate k cluster of points following a gaussian repartition.
    :param nb_objs: 
    :param nb_attrs: 
    :param k: The number of groups to create.
    :return: 
    """
    data = []

    centers = generate_random_data(k, nb_attrs)

    centers = np.array(centers)
    centers = centers[:, 1:]
    
    for i in range(nb_objs):
        center = centers[random.randint(0, len(centers)-1)]
        line = [i + 1] + map(lambda x: random.gauss(x, 0.05), center)
        # line = [i+1, random.gauss(center[j],1) for j in range(len(center))]
        data.append(line)
    return data


def write_solution(filename, solution):
    f = open(filename, 'w')
    k = 1  # Cluster index
    i = 1  # Points index

    for cluster in solution:
        for point in cluster:
            s = str(i) + ',' + str(point)[1:-1] + ',' + str(k)
            s = s.replace(' ', '')  # Remove whitespaces
            f.write(s + '\n')
            i += 1
        k += 1
    # f.close()


def write_centers(filename, centers):
    f = open(filename, 'w')
    k = 1  # Center index

    for center in centers:
        s = str(k) + ',' + str(center)[1:-1]
        s = s.replace(' ', '')  # Remove whitespaces
        f.write(s + '\n')
        k += 1
    # f.close()
