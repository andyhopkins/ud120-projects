#!/usr/bin/python

import sys
import pickle
import matplotlib.pyplot
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import test_classifier, dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi','salary','total_payments','bonus','restricted_stock','exercised_stock_options','total_stock_value'] # You will need to use more features

### Load the dictionary containing the dataset
data_dict = pickle.load(open("final_project_dataset.pkl", "r") )

### Task 2: Remove outliers
### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.
my_dataset = data_dict

### remove outliers
for key in ["TOTAL","SKILLING JEFFREY K","LAY KENNETH L","FREVERT MARK A",'HIRKO JOSEPH','RICE KENNETH D','PAI LOU L']:
    data_dict.pop(key,0)


feature = 'total_stock_value'
for key in data_dict:
    if data_dict[key][feature] != 'NaN' and data_dict[key][feature] > 20000000:
        print key,'',data_dict[key][feature]

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

#print features

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()    # Provided to give you a starting point. Try a varity of classifiers.

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script.
### Because of the small size of the dataset, the script uses stratified
### shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

test_classifier(clf, my_dataset, features_list)

### Dump your classifier, dataset, and features_list so 
### anyone can run/check your results.

dump_classifier_and_data(clf, my_dataset, features_list)


for point in data:
    salary = point[1]
    total_payments = point[2]
    matplotlib.pyplot.scatter( salary, total_payments )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("total_payments")
matplotlib.pyplot.show()

for point in data:
    salary = point[1]
    bonus = point[3]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

for point in data:
    salary = point[1]
    restricted_stock = point[4]
    matplotlib.pyplot.scatter( salary, restricted_stock )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("restricted_stock")
matplotlib.pyplot.show()

for point in data:
    salary = point[1]
    exercised_stock_options = point[5]
    matplotlib.pyplot.scatter( salary, exercised_stock_options )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("exercised_stock_options")
matplotlib.pyplot.show()

for point in data:
    salary = point[1]
    total_stock_value = point[6]
    matplotlib.pyplot.scatter( salary, total_stock_value )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("total_stock_value")
matplotlib.pyplot.show()

