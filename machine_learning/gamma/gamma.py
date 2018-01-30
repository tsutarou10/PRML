#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

N = 100
alpha = [0.1,1,4]
beta = [0.1,1,6]
l = np.linspace(0.0,2.0,N)
for a,b in zip(alpha,beta):
	y = (1 / gamma(a)) * pow(b,a) * pow(l,a-1) * np.exp(-1*b*l)
	plt.plot(l,y,label = 'a = ' + str(a) + ' b = ' + str(b))
	plt.legend(loc = 'upper right')
plt.title('gamma distribution')
plt.savefig('gamma.png')
plt.show()
