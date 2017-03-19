# -*- coding: utf-8 -*-

from utilities import *
import numpy as np
import distance


class Algorithm(object):
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
			distances = [ this.distance(this.C[i][j], B) for j in range(len(this.C[i])) ]
			this.c[i] = this.C[i][np.argmin(distances)]

	def updateDistances(this):
		pLeft = this.p-set(this.c)
		this.L = {}

		for p in pLeft:
			this.L[p] = [0 for i in range(this.k)]
			for i in range(this.k):
				this.L[p][i] = this.distance(this.c[i], p)

	def run(this):
		this.chooseCenters()
		this.updateDistances()
		this.pointsToClusters()

		while this.stopCondition():
			this.updateCenters()
			this.updateDistances()
			this.pointsToClusters()



class Base(Algorithm):
	def __init__(this, data, nClusters, dimension, max_iter=10):
		super(Base, this).__init__(data, nClusters, dimension)
		this.iter = 0
		this.max_iter = max_iter

	def distance(this, X, Y):
		"""
			Returns the euclidean distance between X and Y. No sqrt applied.
			X and Y are tuples of the same dimension.
		"""
		if len(X)!=this.d or len(Y) != this.d:
			raise Exception("Wrong dimension")
		else:
			distance = 0
			for i in range(this.d):
				distance += (X[i]-Y[i])**2
			return distance

	def pointsToClusters(this):
	    """
	        Assign points to the cluster of the closest center.
	    """
	    this.C = [ [this.c[i]] for i in range(this.k) ]							# C[i] is the list of points in cluster i. Add the center in the list.

	    for p in this.L.keys():
	        this.C[np.argmin(this.L[p])].append(p)

	def chooseCenters(this):
		"""
			Choose k centers among the points in p randomly.
		"""
		this.c = []
		pTmp = list(this.p)
		#print(pTmp)
		for i in range(this.k):
			this.c.append( pTmp.pop(randint(0,this.n-1)) )

	def stopCondition(this):
		this.iter += 1
		return this.iter < this.max_iter




class BaseStopUnchanged(Base):
	"""
		Base algorithm, but stops when no points moved from a cluster for more than max_iter.
	"""
	def __init__(this, data, nClusters, dimension, max_iter=10):
		super(BaseStopUnchanged, this).__init__(data, nClusters, dimension, max_iter)
		this.iter_stop = 0
		this.C_former = []

	def stopCondition(this):
		this.iter += 1
		if this.hasChanged():
			this.iter_stop = 0
			this.C_former = this.C
			return True
		else:
			this.iter_stop += 1
			return this.iter_stop < this.max_iter


	def hasChanged(this):
		return this.C_former != this.C



class BaseWords(Base):
	def __init__(this, data, nClusters, dimension, max_iter=10):
		super(BaseWords, this).__init__(data, nClusters, dimension)
		this.iter = 0
		this.max_iter = max_iter

	def distance(this, X, Y):
		"""
			Returns the euclidean distance between X and Y.
			X and Y are strings.
		"""
		return distance.levenshtein(X, Y, normalized=True)

	def chooseCenters(this):
		this.c = ['hydra', 'aqua', 'phobie']

	def run(this):
		this.chooseCenters()
		this.updateDistances()
		this.pointsToClusters()
