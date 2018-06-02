import numpy as np
from sklearn.datasets import load_iris
import random
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

class KNN :
    def __init__(self, k = 30, trRate = 0.8) :
        self.k = k
        self.trRate = trRate 

    def loadFeatures(self) :
        iris = load_iris()
        features = iris.data
        return features

    def loadLabels(self) :
        iris = load_iris()
        labels = iris.target
        return labels
    
    def distance(self, a, b):
        return np.dot(a-b, a-b)
    
    def main(self, trX, teX, trY) :
        y_pred = np.zeros(teX.shape[0])
        for teN, te in enumerate(teX) :
            minDis = 1e11
            for trN, tr in enumerate(trX) :
                tmp = self.distance(tr, te)
                if minDis > tmp :
                    minDis = tmp
                    y_pred[teN] = trY[trN]

        return y_pred

    def metrics(self, y_pred, teY):
        y_pred = self.convertLabel(y_pred)
        teY = self.convertLabel(teY)
        count = 0.
        a, b, c, d = 0., 0., 0., 0.
        for yp, te in zip(y_pred, teY):
            for i in range(3):
                if yp[i] == 1 and te[i] == 1 :
                    a += 1
                elif yp[i] == 0 and te[i] == 1:
                    b += 1
                elif yp[i] == 1 and te[i] == 0:
                    c += 1
                else :
                    d += 1
        
        print 'Recall : ' + str(a / (a + b))
        print 'Precision : ' + str(a / (a + c))
        print 'F-1 : ' + str(2 * a / (2 * a + b + c))
        print 'Accuracy : ' + str((a + d) / (a + b + c + d))

    def convertLabel(self, Y):
        newY = np.zeros([Y.shape[0], 3])
        for number, y in enumerate(Y):
            if y == 0 :
                newY[number] = [1, 0, 1]
            elif y == 1 :
                newY[number] = [0, 1, 0]
            else :
                newY[number] = [0, 0, 1]

        return newY

    def shuffleData(self, X, Y):
        idx = np.array([i for i in range(X.shape[0])])
        np.random.shuffle(idx)
        return X[idx], Y[idx]
    
    def prepareData(self) :
        X = self.loadFeatures()
        Y = self.loadLabels()
        X, Y = self.shuffleData(X, Y)
        trXNum = int(X.shape[0] * self.trRate)
        teXNum = X.shape[0] - trXNum
        trX = X[: trXNum]
        teX = X[trXNum: ]
        trY = Y[: trXNum]
        teY = Y[trXNum: ]
        return trX, teX, trY, teY

if __name__ == '__main__' :
    knn = KNN(k = 30, trRate = 0.8)
    trX, teX, trY, teY = knn.prepareData()
    y_pred = knn.main(trX, teX, trY)
    knn.metrics(y_pred, teY) 
