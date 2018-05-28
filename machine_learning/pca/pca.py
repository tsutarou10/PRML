from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np

class PCA :
	def __init__(self, n_components) :
		self.n_components = n_components

	def calMean(self, X):
		return X.mean(axis = 0)
		
	def main(self, X):
		X = X - self.calMean(X)
		cov = np.cov(X, rowvar = False)

		l, v = np.linalg.eig(cov)
		l_idx = np.argsort(l)[::-1]
		l = l[l_idx]
		v = v[:, l_idx] # extract column Eigenvectors 

		comp = v[:, :self.n_components]

		T = np.dot(X, comp)
		return T

if __name__ == '__main__':
	iris = load_iris()
	pca = PCA(n_components = 2)
	x = pca.main(iris.data)

	plt.figure()
	plt.scatter(x[:,0], x[:,1], c = iris.target)
	plt.show()
