#!/usr/bin/python

import matplotlib.pyplot as plt
from nltk.chunk.util import accuracy

from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

import sys
from time import time
features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary


from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

names = ["Random Forest", "AdaBoost", "Naive Bayes", "Decision Tree","Linear SVM","Nearest Neighbors"]

classifiers=[
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    AdaBoostClassifier(),
    GaussianNB(),
    tree.DecisionTreeClassifier(min_samples_split=40),
    svm.SVC(kernel='linear'),
    KNeighborsClassifier(n_neighbors=3)
]

for name, clf in zip(names, classifiers):
    print name
    t0 = time()
    clf.fit(features_train,labels_train)
    print "training time: ", round(time()-t0, 3), "s"
    t0 = time()
    pred = clf.predict(features_test)
    print "prediction time:", round(time()-t0, 3), "s"
    acc = accuracy_score(labels_test,pred)
    print "accuracy ", acc
    print " "
    try:
        prettyPicture(clf, features_test, labels_test)
    except NameError:
        print(NameError)
        pass
