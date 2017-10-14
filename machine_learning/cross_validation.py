#coding: utf-8

from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC,SVC
import numpy as np
from sklearn.metrics import recall_score,precision_score,f1_score
from sklearn import datasets

class SVM:
		
	def svm(self):
		iris = datasets.load_iris()
		features = iris.data
		target = iris.target
		mask = np.arange(features.shape[0])
		mask = np.random.permutation(mask)

		scores1 = []
		scores2 = []
		scores3 = []

		S = 5
		
		mask = mask.reshape(S,mask.shape[0]/S) #make a mask
		
		for s in range(S):
			teX = features[mask[s]]
			teY = target[mask[s]]
			trX = features[np.setdiff1d(mask,mask[s])]
			trY = target[np.setdiff1d(mask,mask[s])]

			clf = OneVsRestClassifier(LinearSVC())
			clf = clf.fit(trX,trY)
			pred = clf.predict(teX)
			score1 = precision_score(teY,pred,average = "micro")
			score2 = recall_score(teY,pred,average = "micro")
			score3 = f1_score(teY,pred,average = "micro")
			scores1.append(score1)
			scores2.append(score2)
			scores3.append(score3)
		
		print "micro precision    : %.2f" % np.array(scores1).mean()
		print "micro recall    : %.2f" % np.array(scores2).mean()
		print "micro F1        : %.2f" % np.array(scores3).mean()

if __name__ == "__main__":
	s = SVM()
	s.svm()
