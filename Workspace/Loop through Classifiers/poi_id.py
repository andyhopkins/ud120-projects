#!/usr/bin/python


import pickle

from classifyNB import classify

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
labels_list = ['poi']
features_list = ['poi','salary','total_payments'] # You will need to use more features

### Load the dictionary containing the dataset
data_dict = pickle.load(open("final_project_dataset.pkl", "r") )

### Task 2: Remove outliers
### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.
my_dataset = data_dict



clf = classify(my_dataset, features_list)





