#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

from sklearn.cross_validation import train_test_split

### your code goes here
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)


### it's all yours from here forward!

from sklearn import tree
from sklearn.metrics import accuracy_score,precision_score,recall_score

print "features in data ",len(features[0])
clf=tree.DecisionTreeClassifier()

clf.fit(features_train,labels_train)

pred = clf.predict(features_test)

acc = accuracy_score(labels_test,pred)
pred_score = precision_score(labels_test,pred)
recall_scor = recall_score(labels_test,pred)


print "accuracy ", acc

print "precision score ", pred_score
print "recall score ", recall_scor

print "poi in test set ",sum(labels_test)
print "persons in test set ",len(labels_test)

print "real ",labels_test
print "predicted ",pred
print "true positives",sum(labels_test*pred)


