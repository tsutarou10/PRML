#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy import integrate

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
	# タイトル
	plt.title('multivariate normal distribution')

	# ラベル
	plt.xlabel('$x_{1}$')
	plt.ylabel('$x_{2}$')
	plt.show()


	"""
	Z = mlab.bivariate_normal(X, Y, 2.0, 1.0, 0.0, 0.0, 0.0)

    # ヒートマップ
    plt.pcolor(X, Y, Z, cmap=plt.cm.hot)

    plt.colorbar()

    # タイトル
    plt.title('bivariate normal density')

    # ラベル
    plt.xlabel('$x$', size=12)
    plt.ylabel('$y$', size=12)

    plt.show()
    Ym = np.sum(Z,axis = 0)
    Xm = np.sum(Z,axis = 1)
    plt.figure(2)
    plt.plot(x,Ym)
    plt.show()
    plt.figure(3)
    plt.plot(Xm,y)
    plt.show()
    """
	"""
	mu = [0.0,-3.4,1.5]
	sigma = [1.0,0.25,4.41]
	for m,s in zip(mu,sigma):
		y = norm(x,m,s)
		plt.plot(x,y,label = "meam = " + str(m) + " variance = " + str(s))
		plt.legend(loc = "upper right")
	plt.show()
	"""
