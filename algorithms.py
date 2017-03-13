# -*- coding: utf-8 -*-

from utilities import *


class algorithm:
	def __init__(this, data, nClusters, dimension):
		this.p = set(data)
		this.n = len(data)
		this.k = nClusters
		this.d = dimension
		this.c = []
		this.L = []
		this.C = []

	def updateCenters(this):
		# For each cluster, compute the new center
		for i in range(this.k):
			# Return the closest point to the barycenter in this.C[i].
			B = barycenter(this.C[i], this.d)
			#FIXME: Optimize the min func.
			distances = [ this.distance(this.C[i][j], B) for j in range(len(this.C[i])) ]
			this.c[i] = this.C[i][distances.index(min(distances))]

	def updateDistances(this):
		pLeft = this.p-set(this.c)
		this.L = {}

		for p in pLeft:
			this.L[p] = [0 for i in range(this.k)]
			for i in range(this.k):
				this.L[p][i] = this.distance(this.c[i], p)

	def distance(this, X, Y):
		"""
			Returns the euclidean distance between X and Y. No sqrt applied.
			X and Y are tuples of the same dimension.
		"""
		if len(X)!=this.d or len(Y) != this.d:
			raise Exception("X and Y don't have the same dimension")
		else:
			distance = 0
			for i in range(this.d):
				distance += (X[i]-Y[i])**2
			return distance

class alg0(algorithm):
	def chooseCenters(this):
		"""
			Choose k centers among the points in p randomly.
		"""
		this.c = []
		pTmp = list(this.p)
		for i in range(this.k):
			this.c.append( pTmp.pop(randint(0,this.n-1)) )

	def run(this):
		this.chooseCenters()
		this.updateDistances()
		this.C = pointsToClusters(this.L, this.c)

		i = 0
		while i<5:
			this.updateCenters()
			this.updateDistances()
			this.C = pointsToClusters(this.L, this.c)
			i += 1
