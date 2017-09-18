#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt

def function(x):
	return np.sin(x)

def diff(x,n):
	r = n % 4
	if r == 1:
		return np.cos(x)
	elif r == 2:
		return -1 * np.sin(x)
	elif r == 3:
		return -1 * np.cos(x)
	elif r == 0:
		return np.sin(x)

def kaijou(n):
	k = 1
	if n == 0 or n == 1:
		return 1
	else:
		for i in range(1,n+1):
			k *= i
	return k

if __name__ == '__main__':
	x = np.arange(-6,6,0.1)
	plt.ylim(ymin=-1,ymax=1)
	y = np.sin(x)
	plt.plot(x,y,label='sin x')
	plt.legend()
	f = function([0 for i in range(120)])
	
	plt.plot(x,f)
	plt.grid(True)
	for i in range(1,12):
		print kaijou(i)
		if i % 2 != 0:
			f += ((diff(0,i) * pow(x,i)) / kaijou(i))
			plt.plot(x,f,label = 'dim = ' + str(i))
			plt.legend()
	plt.show()
