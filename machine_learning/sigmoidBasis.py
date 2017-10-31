#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x,mu,s):
	a = (x - mu) / s
	return 1 / (1 + np.exp(-a))

if __name__ == "__main__":
	N = 1000
	x = np.linspace(-1,1, N)
	mu = [0.2*(i-5) if i > 5 else 0.2 * (-i) for i in range(11)]
	sigma = [0.1 for i in range(11)]
	for m,s in zip(mu,sigma):
		y = sigmoid(x,m,s)
		plt.plot(x,y)
	plt.title("Sigmoid Basis function")
	plt.savefig("sigmoidBasis.png")
	plt.show()
