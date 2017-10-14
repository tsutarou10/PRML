#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt

def function(x): #x^3 - 2x^2 + x + 3
	return x ** 2 - 4 * x + 4

	#return pow(x,3) - 2 * pow(x,2) + x + 3

def diff1(x): #1階微分 3x^2 - 4x + 1
	dx = 1e-12
	return (function(x+dx) - function(x)) / dx

def diff2(x): #2階微分 6x - 4
	dx = 1e-2
	return (diff1(x+dx) - diff1(x)) / dx

'''
initX : 初期値
learningRate : 学習率
'''
def gradient(initX):
	x = initX
	dx = 1e-11
	dist = np.array([])
	iter = 0
	while True:
		dist = np.append(dist,x)
		tmp = x
		x = x - diff1(x) / diff2(x)
		iter += 1
		if -1 * dx < abs(x - tmp) < dx:
			break
	return dist,iter

if __name__ == '__main__':
	x = np.arange(-4,8,0.1)
	y = function(x)
	dist,iter = gradient(5)
	plt.plot(x,y,label = 'f(x) num of iter = ' + str(iter))
	
	y = function(dist)
	plt.plot(dist,y)
	print 'min = ' + str(dist[len(dist) - 1]) #最小値を出力
	plt.legend()
	plt.show()
	plt.savefig('gradient_method.png')
