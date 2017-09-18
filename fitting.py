#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import random
from matplotlib import pyplot as plt

def makeData(trainNum):
	noise = np.random.randn(trainNum) * 0.1 #make a noise
	xTrain = np.random.rand(trainNum) #training data
	yTrain = np.sin(2 * np.pi * xTrain) + noise #supervised data
	np.save('xTrain.npy',xTrain)
	np.save('yTrain.npy',yTrain)

def setTrain():
	xTrain = np.load('xTrain.npy')
	yTrain = np.load('yTrain.npy')
	return xTrain,yTrain

def fitting(M,trainNum):
	w = np.random.rand(M+1) #init a weight
	xTrain,yTrain = setTrain()
	X = np.array([pow(xTrain,i) for i in range(M+1)])
	Y = np.dot(w,X)
	A = np.array([[pow(xTrain,i+j).sum() for j in range(M+1)] for i in range(M+1)])
	T = np.array([(pow(xTrain,i)*yTrain).sum() for i in range(M+1)])
	return np.linalg.solve(A,T)

def RMS(y,t,N): # Root Mean Square error
	return np.sqrt(pow(y-t,2).sum()/N)

if __name__ == '__main__':
	trainNum = 10
	makeData(trainNum)
	x = np.arange(0,1,0.01)
	w = fitting(M,trainNum)
	xTrain,yTrain = setTrain()	
	for M in range(10):
		w = fitting(M,trainNum)
		tmpY = np.array([w[i] * pow(x,i) for i in range(M+1)])
		y = tmpY.sum(axis = 0)
		plt.plot(x,y,label = 'M = ' + str(M))
		plt.legend()
		plt.plot(x,np.sin(2*np.pi*x),label = 'sin')
		plt.legend()
		plt.plot(xTrain,yTrain,'o')
		plt.ylim(ymin = -1.3,ymax = 1.3)
		#plt.savefig('fittingM'+str(M)+'.png')
		plt.show()
	
	
	#plt.show()
	'''
	trainNum = 10
	testNum = 100
	makeData(trainNum)
	xTrain,yTrain = setTrain()
	xTest = np.random.rand(testNum)
	MTrArray = np.array([])
	rmsTrArray = np.array([])
	MTeArray = np.array([])
	rmsTeArray = np.array([])
	noise = np.random.rand(testNum) * 0.1
	yTest = np.sin(2 * np.pi * xTest) + noise
	x = np.arange(0,1,0.01)
	for M in range(10):
		w = fitting(M,trainNum)
		tmpTrY = np.array([w[i] * pow(xTrain,i) for i in range(M+1)])
		tmpTeY = np.array([w[i] * pow(xTest,i) for i in range(M+1)])
		trY = tmpTrY.sum(axis = 0)
		teY = tmpTeY.sum(axis = 0)
		MTrArray = np.append(M,MTrArray)
		rmsTrArray = np.append(RMS(trY,yTrain,trainNum),rmsTrArray)
		MTeArray = np.append(M,MTeArray)
		rmsTeArray = np.append(RMS(teY,yTest,testNum),rmsTeArray)
	plt.plot(MTrArray,rmsTrArray,label = 'train',marker = 'o')
	plt.legend()
	plt.plot(MTeArray,rmsTeArray,label = 'test',marker = 'o')
	plt.legend()
	plt.ylim(ymin=0,ymax = 1)
	plt.show()
	'''













