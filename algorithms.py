# -*- coding: utf-8 -*-

from utilities import *

# TODO: study complexity


class algorithm:
	def __init__(this, data, nClusters, dimension):
		this.p = set(data)
		this.n = len(data)
		this.k = nClusters
		this.d = dimension
		this.c = []
		this.L = []
		this.C = []

class alg0(algorithm):
	def run(this):
		this.c = chooseCenter_rand(list(this.p), this.k)
		this.L = updateDistances(this.c, this.p)
		this.C = pointsToClusters(this.L, this.c)

		i = 0
		while i<5:
			this.c = updateCenters(this.C)
			this.L = updateDistances(this.c, this.p)
			this.C = pointsToClusters(this.L, this.c)
			i += 1
