#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy import integrate

def norm(x,mu,sigma):
	return 1 / pow(2*np.pi*sigma,0.5) * np.exp(-0.5*pow(x-mu,2)/sigma)

if __name__ == "__main__":
	N = 1000
	x = np.linspace(-6,6, N)
	mu = [0.0,-3.4,1.5]
	sigma = [1.0,0.25,4.41]
	for m,s in zip(mu,sigma):
		y = norm(x,m,s)
		plt.plot(x,y,label = "meam = " + str(m) + " variance = " + str(s))
		plt.legend(loc = "upper right")
	plt.show()
