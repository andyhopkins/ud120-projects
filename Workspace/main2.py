#!/usr/bin/python

""" Complete the code in ClassifyNB.py with the sklearn
    Naive Bayes classifier to classify the terrain data.
    
    The objective of this exercise is to recreate the decision 
    boundary found in the lesson video, and make a plot that
    visually shows the decision boundary """





from feature_format import featureFormat, targetFeatureSplit

from sklearn import cross_validation
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score

from time import time

import pickle
import numpy as np
import pylab as pl
import matplotlib.pyplot
import matplotlib.pyplot as plt

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

### remove outliers
data_dict.pop("TOTAL",0)
data_dict.pop("KAMINSKI WINCENTY J",0)
data_dict.pop("KEAN STEVEN J",0)
data_dict.pop("BECK SALLY W",0)

for key in data_dict:
    if data_dict[key]['exercised_stock_options'] != 'NaN':
        print key,'',data_dict[key]['exercised_stock_options']


### select features to be used
#features_list = ["poi", "salary" ,  "to_messages",  "deferral_payments" ,  "total_payments",  "exercised_stock_options",  "bonus",  "restricted_stock",  "shared_receipt_with_poi",  "restricted_stock_deferred",  "total_stock_value",  "expenses",  "loan_advances",  "from_messages",  "other",  "from_this_person_to_poi", "director_fees",  "deferred_income",  "long_term_incentive", "from_poi_to_this_person"]
features_list = ["poi", "salary" ,  "exercised_stock_options"]
data = featureFormat(data_dict, features_list)

### split data between label and features
labels, features = targetFeatureSplit( data )

### split data to train and test
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)



### create classifier
#clf = svm.SVC()
clf = ExtraTreesClassifier(n_estimators=250,random_state=0)

### Fit classifier with training data
t0 = time()
clf.fit(features_train, labels_train)
print "Training Time:", round(time()-t0, 3), "s"
print


importances = clf.feature_importances_
std = np.std([tree.feature_importances_ for tree in clf.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

# Print the feature ranking
#print("Feature ranking:")
#
#for f in range(19):
#    #print f,'\t',features_list[f],'\t\t', importances[indices[f]]
#    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))
#
## Plot the feature importances of the forest
#plt.figure()
#plt.title("Feature importances")
#plt.bar(range(19), importances[indices],
#       color="r", yerr=std[indices], align="center")
#plt.xticks(range(19), indices)
#plt.xlim([-1, 19])
#plt.show()

### Predict with classifier against test data
pred = clf.predict(features_test)

### calculate score
print "score is ",clf.score(features_test,labels_test)


### Calculate accuracy
acc = accuracy_score(pred, labels_test)
print "Accuracy is ",acc

#### check prediction against test for poi
#tpcnt = 0
#fncnt = 0
#fpcnt = 0
#tncnt = 0
#
#for i in range(len(labels_test)):
#    if labels_test[i] == 1 and pred[i] ==1:
#        tpcnt += 1
#    elif labels_test[i] == 1:
#        fncnt += 1
#    elif pred[i] == 1:
#        fpcnt += 1
#    else:
#        tncnt += 1
#print
#print 'There are ',tpcnt,' true positives (actual label and predicted label is 1)'
#print 'There are ',tncnt,' true negitives (actual label and predicted label is 0)'
#print 'There are ',fncnt,' false negitives (actual label is 1 predicted label is 0)'           
#print 'There are ',fpcnt,' false positives (actual label is 0 and predicted label is 1)'  
#
#print
#print 'Current precision score is ',precision_score(labels_test,pred,average='macro')
#print 'Current recall score is ',recall_score(labels_test,pred)
#print 'Current F1 score is ',f1_score(labels_test,pred)
#
#
#
### plot datapoints for salary and bonus

for point in data:
    salary = point[1]
    bonus = point[2]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("from_messages")
matplotlib.pyplot.show()




