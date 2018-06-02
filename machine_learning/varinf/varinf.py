#coding:utf-8
import numpy as np
def multiNorm(x, mu, sigma):
	return (1 / pow((2 * np.pi),1) * (1 / pow(np.linalg.det(cov), 0.5)) * np.exp(-0.5 * np.dot(x - mu, np.linalg.inv(cov)).dot(x - mu)))

def normal(x, mu, sigma):
	return (1 / pow(2 * np.pi * pow(sigma, 2), 0.5)) * np.exp(-0.5 * pow(x - mu, 2) / pow(sigma, 2))

def KLdiv(p, q):
	return stats.entropy(p, q, 2)


def main():
	maxiter = 100
	mu = [2, 2]
	sigma = [[0, 1], [1, 0]]
	x1 = np.linspace(-5.0, 5.0, 200)
	x2 = np.linspace(-5.0, 5.0, 200)
	S = np.linalg.inv(sigma)
	m2 = 0
	for i in xrange(maxiter):
		m1 = mu[0] - sigma[0][0] * S[0][1] * (m2 - mu[1])
		q1 = normal(x1, m1, sigma[0][0])
		m2 = mu[1] - sigma[1][1] * S[1][0] * (m1 - mu[0])
		q2 = normal(x2, m2, sigma[1][1])

	return m1, m2

if __name__ == '__main__' :
	m1, m2 = main()
	mu = np.array([m1, m2])
	sigma = np.array([[0, 0],[0, 0]])
	x = np.linspace(-5.0, 5.0, 200)
	y = np.linspace(-5.0, 5.0, 200)
	X, Y = np.meshgrid(x, y)
	N = np.array([])
	for yy in y:
		for xx in x:
			z = np.array([xx, yy])
			N = np.append(N, multiNorm(z, mu, sigma))
	N = N.reshape(200, 200)
	plt.show()
