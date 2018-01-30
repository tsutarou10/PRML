#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

def norm(x,mu,sigma):
	return (1 / pow(2 * np.pi,x.shape[0]/2)) * (1 / pow(np.linalg.det(sigma),0.5)) * np.exp(-0.5 * np.dot(x - mu,np.linalg.inv(sigma)).dot(x - mu))
if __name__ == "__main__":
	x = np.linspace(-5.0, 5.0, 200)
	y = np.linspace(-5.0, 5.0, 200)
	X, Y = np.meshgrid(x, y)
	Mu = np.array([1.0,0.0])
	Sigma = np.array([[0.8,0.7],[0.7,1.3]])
	N = np.array([])
	for yy in y:
		for xx in x:
			z = np.array([xx,yy])
			N = np.append(N,norm(z,Mu,Sigma))
	N = N.reshape(200,200)
	plt.pcolor(X, Y, N, cmap=plt.cm.hot)
	plt.title('multivariate normal distribution')

	plt.xlabel('$x_{1}$')
	plt.ylabel('$x_{2}$')
	plt.savefig("multivariate_normal.png")
	plt.show()
