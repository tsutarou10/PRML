#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

def phi(x,mu,s):
	return np.exp(-(pow(x-mu,2))/(2*pow(s,2)))

if __name__ == "__main__":
	N = 1000
	x = np.linspace(-1,1, N)
	mu = [0.2*(i-5) if i > 5 else 0.2 * (-i) for i in range(11)]
	sigma = [0.1 for i in range(11)]
	for m,s in zip(mu,sigma):
		y = phi(x,m,s)
		plt.plot(x,y)
	plt.title("Gaussian Basis function")
	plt.savefig("gaussianBasis.png")
	plt.show()
