#coding:utf-8

import numpy as np
import math
from scipy.special import gamma

def poi(x, lam):
	return pow(lam, x) * math.exp(-lam) / math.factorial(x)

def cat(s, pi):
	K = s.shape[0]
	for k in xrange(K):
		rslt *= pow(pi[k], s[k])
	return rslt

def latentSampling(s, eta):
	return cat(s, eta)

def lamSampling(lam, a, b):
	tmp = 0

def gam(lam, a, b):
	return (1 / gamma(a)) * pow(b, a) * pow(l, a - 1) * np.exp(-1 * b * l)

def softmax(x):
	return x / x.sum()

def diri(alpha):
	pi = softmax(np.random.rand(2))
	r = gamma(np.sum(alpha)) / (gamma(alpha[0]) + gamma(alpha[1]))
	rslt = r * np.power(pi[0], alpha[0] - 1) * np.power(pi[1], alpha[1] - 1)
	pi = np.array([rslt, 1. - rslt])
	return pi

def main():
	maxIter = 100
	x = np.linspace(-5.0, 5.0, 10)
	K = 2
	alpha = np.array([2.0, 1.0])

	pi = diri(alpha)
	print pi
	'''
	for i in xrange(maxIter):

		for n in xrange(N):
			s = latentSampling(s, eta)
		for k in xrange(K):
			lam = lamSampling(lam, a, b)

		pi = piSampling(pi, alpha)
	'''
if __name__ == '__main__':
	main()
