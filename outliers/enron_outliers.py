#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus",]
data = featureFormat(data_dict, features)

### your code below
def getKey(item):
    return item[0]

def searchPersonByFeautures(data,features,data_dict):
    print "searched ",data
    for person in data_dict:
        cond=True
        for i in range(len(features)):
            val=data_dict[person][features[i]]
            cond=cond and val==data[i]

        if cond:
            return "matched person",person
    return "not found"

data=sorted(data, key=getKey,reverse=True)

print searchPersonByFeautures(data[0],features,data_dict)
data.pop(0)

print searchPersonByFeautures(data[0],features,data_dict)
data.pop(0)
print searchPersonByFeautures(data[0],features,data_dict)
data.pop(0)

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )


matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

