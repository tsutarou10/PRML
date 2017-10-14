#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import random
from matplotlib import pyplot as plt


if __name__ == '__main__':
	X = np.array([i for i in range(10)]) # random variable 0,...,9
	Y = np.array([0.5 for i in range(10)])
	plt.plot(X,Y,color = 'red')
	distY = np.zeros(2)
	distX = np.zeros(10)
	distXY1 = np.zeros(10)
	for i in range(10):
		plt.plot([i for j in range(10)],X,color = 'red')
	plt.ylim(ymin=0,ymax=1)

	for i in range(60):
		ranX = random.uniform(0,9)
		if 7 < ranX < 9:
			ranX -= 1
		else:
			ranX += 1
		ranY = random.uniform(0,1)
		if 0.6 < ranY <= 1.0:
			ranY -= 0.2
		else:
			ranY += 0.3
		if 0.0 <= ranY < 0.5:
			distY[0] += 1
			distXY1[int(ranX)] += 1
		else:
			distY[1] += 1
		plt.plot(ranX,ranY,'o',color = 'blue')
		distX[int(ranX)] += 1

	plt.show()
	plt.figure()
	plt.barh([0,1],distY)
	plt.show()
	plt.figure()
	plt.bar(X,distX)
	plt.show()
	plt.figure()
	plt.bar(X,distXY1)
	plt.show()

