#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.special import gamma

N = 100
alpha = [0.1,1.0,2.0,8.0,10.0]
beta = [0.1,1.0,3.0,4.0,10.0]
p = np.linspace(0.0,1.0, N)
print p
for a,b in zip(alpha,beta):
	y = (gamma(a+b)/(gamma(a)*gamma(b))) * pow(p,a - 1) * pow(1-p,b - 1)
	plt.plot(p,y,label = "a = " + str(a) + " b = " + str(b))
	plt.legend(loc = "upper right")
plt.savefig("beta.png")
plt.show()