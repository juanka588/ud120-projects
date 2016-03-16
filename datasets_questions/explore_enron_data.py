#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print ("total persons ",len(enron_data))
print enron_data
count=0
hasSalary=0
hasEmail=0
for person in enron_data:
    print(person,enron_data[person]["email_address"])
    if(enron_data[person]["poi"]==1):
        count=count+1

    if(enron_data[person]["salary"]!="NaN"):
        hasSalary=hasSalary+1

    if(enron_data[person]["email_address"]!="NaN"):
        hasEmail=hasEmail+1


print ("poi ",count)
print ("stock value of PRENTICE JAMES",enron_data["PRENTICE JAMES"]["total_stock_value"])
print ("from_message to poi's of COLWELL WESLEY",enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print ("stock options of SKILLING JEFFREY K",enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
print ("payments of SKILLING JEFFREY K",enron_data["SKILLING JEFFREY K"]["total_payments"])
print ("payments of LAY KENNETH L",enron_data["LAY KENNETH L"]["total_payments"])
print ("payments of FASTOW ANDREW S",enron_data["FASTOW ANDREW S"]["total_payments"])
print ("Person with emails: ",hasEmail," Persons with Salary: ",hasSalary)