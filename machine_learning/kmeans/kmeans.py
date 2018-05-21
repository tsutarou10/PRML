#coding:utf-8

import numpy as np
from sklearn.datasets import load_iris
import random
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

class Kmeans :
	def __init__(self, clusterNum) :
		self.clusterNum = clusterNum
		
	def loadFeatures(self) :
		iris = load_iris()
		features = iris.data
		return features

	def initAssign(self, X) :
		V = X.shape[0]
		Y = np.zeros(V)
		for v in range(V) :
			Y[v] = random.randrange(3)
		
		return Y

	def normalize(self, a, b) :
		sumA , sumB = a.sum(), b.sum()
		a, b = a / sumA, b / sumB
		return a, b

	def dis(self, a, b) :
		if a.shape[0] != b.shape[0]:
			print 'different dimension'
			return
		rslt = np.linalg.norm(a - b)
		return rslt

	def reassign(self, Vmean, X) :
		Y = np.zeros(X.shape[0])
		minTmp = 1e11
		minIndex = 3
		for v in range(X.shape[0]):
			for c in range(self.clusterNum) :
				if minTmp > self.dis(Vmean[c], X[v]) :
					minTmp = self.dis(Vmean[c], X[v])
					minIndex = c
			Y[v] = minIndex
			minTmp = 1e11
		return Y

	def delta(self, a, b) :
		for aa, bb in zip(a, b) :
			if aa != bb :
				return False
		return True

	def main(self, X) :
		Y = self.initAssign(X)
		Vmean = np.zeros((self.clusterNum, X.shape[1]), dtype = np.float)

		iterNum = 1
		while 1 :
			print 'the number of iteration :' + str(iterNum)
			for i in range(self.clusterNum):
				Vmean[i] = X[np.where(Y == i)].mean(axis = 0)
			Y_next = self.reassign(Vmean, X)
			if(self.delta(Y_next, Y)) :
					return Y_next
			Y = Y_next
			iterNum += 1
		return Y_next

	def show(self, X, Y) :
		pca = PCA(n_components = 2)
		pca.fit(X)
		X = pca.fit_transform(X)

		for number, y in enumerate(Y) :
			if y == 0 :
				c = 'red'
			elif y == 1 :
				c = 'blue'
			else :
				c = 'green'
			plt.scatter(X[number][0], X[number][1], color = c)
		plt.show()

if __name__ == '__main__' :
	cls = Kmeans(clusterNum = 3)
	X = cls.loadFeatures()
	Y = cls.main(X)
	cls.show(X, Y)
