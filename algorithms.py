# -*- coding: utf-8 -*-

from utilities import *

# TODO: use a class for algorithms
# TODO: study complexity

def algo0(data, k):
    p = set(data)
    c = chooseCenter_rand(data, k)
    pointsLeft = data                                                           # data has been stripped of the centers
    n = len(data)
    
    L = updateDistances(c, p)
    C = pointsToClusters(L, c)
    
    i = 0
    while i<5:
        c = updateCenters(C)
        L = updateDistances(c, p)
        C = pointsToClusters(L, c)
        i += 1
        
    return C, c