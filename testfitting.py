#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import random
from matplotlib import pyplot as plt

def supervise(x):
	noise = np.random.rand(x.shape[0]) * 0.1
	return np.sin(2*np.pi*x) + noise

def makeData(trainingNum):
	x = np.arange(0,1,0.01)
	#xTrain = np.load("xTrain.npy")
	xTrain = np.random.rand(trainingNum)
	noise = np.random.rand(trainingNum) * 0.1
	fun = np.sin(2*np.pi*x)
	t = np.sin(2*np.pi*xTrain) + noise
	#t = np.load("t.npy")
	#plt.plot(x,fun)
	#plt.plot(xTrain,t,'o')
	np.save("xTrain.npy",xTrain)
	np.save("t.npy",t)
	#return xTrain,t

def fitting(M,trainingNum):
	w = np.random.rand(M+1)
	#makeData(trainingNum)
	#xTrain,t = makeData(trainingNum)
	xTrain = np.load("xTrain.npy")
	t = np.load("t.npy")
	xArray = np.array([pow(xTrain,i) for i in range(M+1)])
	y = np.dot(w,xArray)
	A = np.array([[pow(xTrain,i+j).sum() for j in range(M+1)] for i in range(M+1)])
	T = np.array([(pow(xTrain,i)*t).sum() for i in range(M+1)])
	return np.linalg.solve(A,T)	

def RMS(y,t,N):
	return np.sqrt(pow(y - t,2).sum()/N)


if __name__ == '__main__':
	'''
	M = 3
	trainingNum = 10
	w = fitting(M,trainingNum)
	x = np.arange(0,1,0.01)
	y = np.array([(w[i] * pow(x,i)) for i in range(M+1)])
	y = y.sum(axis=0)
	plt.ylim(ymin=-1.3,ymax=1.3)
	plt.plot(x,y,label = 'M=' + str(M))
	plt.legend()
	plt.show()'''
	plt.ylim(ymax=1.0)
	trainingNum = 10
	testNum = 100
	makeData(trainingNum)
	xtrain = np.load('xTrain.npy')
	xtest = np.random.rand(testNum)
	Marray = np.array([])
	RMSarray = np.array([])
	Mtarray = np.array([])
	RMStarray = np.array([])
	for M in range(10):
		w = fitting(M,trainingNum)
		ytrain = np.array([(w[i] * pow(xtrain,i)) for i in range(M+1)])
		ytest = np.array([(w[i] * pow(xtest,i)) for i in range(M+1)])
		ytrain = ytrain.sum(axis=0)
		ytest = ytest.sum(axis=0)
		ttrain = np.load('t.npy')
		ttest = supervise(xtest)
		rmstrain = RMS(ytrain,ttrain,trainingNum)
		Marray = np.append(M,Marray)
		RMSarray = np.append(rmstrain,RMSarray)
		rmstest = RMS(ytest,ttest,testNum)
		Mtarray = np.append(M,Mtarray)
		RMStarray = np.append(rmstest,RMStarray)
	plt.plot(Marray,RMSarray,label='train')
	plt.plot(Mtarray,RMStarray,label = 'test')
	plt.legend()
	plt.show()
	

