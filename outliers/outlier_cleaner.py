#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here

    for i in range(len(predictions)):
        cleaned_data.append((ages[i],net_worths[i],abs(predictions[i]-net_worths[i])))

    cleaned_data=sorted(cleaned_data, key=getKey,reverse=True)

    for i in range(len(cleaned_data)):
        print "i",i," ",cleaned_data[i]

    percentage=0.1
    size=int(len(cleaned_data)*percentage)

    for i in range(size):
        print "removed i",i," ",cleaned_data[0]
        cleaned_data.remove(cleaned_data[0])

    for i in range(len(cleaned_data)):
        print "i",i," ", cleaned_data[i]
    return cleaned_data

def getKey(item):
    return item[2]