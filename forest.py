from sklearn import ensemble
from sklearn.utils import shuffle
import numpy as np
from sklearn import cross_validation

#load data from file
data = np.loadtxt('acceldata.txt',delimiter=',')
DT = data.transpose()

#split data into arrays
X = np.array(DT[0:-1]).transpose()
Y = np.array(DT[-1]).transpose()

#create training and test sets, 70% in training 30% in testing set
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size=0.30, random_state=0)

#construct random forest with 10 trees, creating bootstrap samples
rf = ensemble.RandomForestClassifier(n_estimators=10,random_state=0,bootstrap=True)

### fit and score the model
rf.fit(X_train,y_train)
