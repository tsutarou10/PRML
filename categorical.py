#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def cat(x,p):
	dist = []
	for i in range(5):
		dist.append(np.prod(pow(p,x[i])))
	return dist

if __name__ == "__main__":
	p = np.array([0.1,0.5,0.2,0.05,0.15])
	x = np.array([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]])
	dist = cat(x,p)
	x = np.array([1,2,3,4,5])
	label = ["x = 1","x = 2","x = 3","x = 4","x = 5"]
	plt.ylim([0.0,1.0])
	plt.title("Categorical Distribution")
	plt.bar(x,dist,tick_label = label,align = "center")
	plt.savefig("categorical.png")
	plt.show()