#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def bern(x,p):
	return pow(p,x) * pow(1-p,1-x)

if __name__ == "__main__":
	dist = np.zeros(2)
	for i in range(1,10):
		plt.figure()
		p = 0.1 * i
		dist[0] = bern(0,p)
		dist[1] = bern(1,p)

		x = np.array([0,1])

		label = ["x = 0","x = 1"]
		plt.ylim([0.0,1.0])
		plt.title("bernoulli distribution (p = " + str(p) + ")")
		plt.bar(x,dist,tick_label = label,align = "center")
		plt.savefig("bernoulli_" + str(p) + ".png")