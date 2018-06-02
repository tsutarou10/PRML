Source codes for K-nearet neighbor method. 
 --- 
I upload source codes of K-nearet neighbor method and figure that shows result of K-nearet neighbor method.

I implemented source code of K-nearet neighbor method without scikit-learn. (but I use the dataset of Iris that is in scikit-learn for verifing my code.) 

Libraries Used
---
- python
  1. [numpy](http://www.numpy.org/)
  2. [scikit-learn](http://scikit-learn.org/stable/)
  3. [matplotlib](https://matplotlib.org)
Usage for K-nearet neighbor method
---
Saving the file "knn.py".

Next, you should import this file.
~~~
from knn import KNN
~~~

and
~~~
knn = KNN(k = 30, trRate = 0.8)
trX, teX, trY, teY = knn.prepareData()
y_pred = knn.main(trX, teX, trY)
knn.metrics(y_pred, teY)
~~~

You can show the result of KNN after typing this code in main function.

Result
---
```vim
Recall : 0.975
Precision : 0.975
F-1 : 0.975
Accuracy : 0.978
```
Developers
---

Implementor
 - [Tatsuro Miyazaki]
	 
