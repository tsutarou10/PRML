#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt

def function(x):
	return x ** 2 - 4 * x + 4

def diff(x): #数値微分
	dx = 1e-11
	return (function(x+dx) - function(x)) / dx


'''
initX : 初期値
learningRate : 学習率
'''
def gradient(initX,learningRate):
	x = initX
	dx = 1e-11
	dist = np.array([])

	while True:
		dist = np.append(dist,x)
		if -1 * dx < diff(x) < dx:
			break
		x = x - learningRate * diff(x)

	return dist

if __name__ == '__main__':
	'''
	x^2 - 4x + 4のグラフの描写
	'''
	x = np.arange(-4,8,0.1)
	y = function(x)
	plt.plot(x,y,label = 'f(x)')

	dist = gradient(0,0.1)
	y = function(dist)
	plt.plot(dist,y)
	print 'min = ' + str(dist[len(dist) - 1]) #最小値を出力
	plt.legend()
	plt.show()
	plt.savefig('gradient_method.png')

