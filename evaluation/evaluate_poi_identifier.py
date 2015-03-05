#!/usr/bin/python


"""
    starter code for the evaluation mini-project
    start by copying your trained/tested POI identifier from
    that you built in the validation mini-project

    the second step toward building your POI identifier!

    start by loading/formatting the data

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



### your code goes here 

### Import objects
from time import time
### import sklearn objects
from sklearn.metrics import precision_score, recall_score, accuracy_score,f1_score
from sklearn import tree
from sklearn import cross_validation

### Split data into training and test
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)

### create classifier
clf = tree.DecisionTreeClassifier()

### fit classifier
t0 = time()
clf = clf.fit(features_train, labels_train)
print "Training time:", round(time()-t0, 3), "s"

### predict
pred = clf.predict(features_test)
print "Prediction time:", round(time()-t0, 3), "s"

### display accuracy
acc = accuracy_score(pred, labels_test)
print 
print "Accuracy is ",acc

### Display Predicted POI count in test data
cnt =0
for poi in pred:
    if poi == 1:
        cnt += 1        
print
print 'Of ',len(pred),' people, there are ',cnt,' pepole predicted as POIs in test data'

### Display true count of POI in test data 
cnt = 0
for poi in labels_test:
    if poi == 1:
        cnt += 1
print
print 'There are ',cnt,' POIs in the test data giving an accuracy of ',float(len(labels_test)-cnt)/len(labels_test)

### check prediction against test for poi
tpcnt = 0
fncnt = 0
fpcnt = 0
tncnt = 0

for i in range(len(labels_test)):
    if labels_test[i] == 1 and pred[i] ==1:
        tpcnt += 1
    elif labels_test[i] == 1:
        fncnt += 1
    elif pred[i] == 1:
        fpcnt += 1
    else:
        tncnt += 1
print
print 'There are ',tpcnt,' true positives (actual label and predicted label is 1)'
print 'There are ',tncnt,' true negitives (actual label and predicted label is 0)'
print 'There are ',fncnt,' false negitives (actual label is 1 predicted label is 0)'           
print 'There are ',fpcnt,' false positives (actual label is 0 and predicted label is 1)'       

### Show precision and recall scores

print
print 'Current precision score is ',precision_score(labels_test,pred,average='macro')
print 'Current recall score is ',recall_score(labels_test,pred)
print 'Current F1 score is ',f1_score(labels_test,pred)


