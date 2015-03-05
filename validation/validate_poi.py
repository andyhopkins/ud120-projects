#!/usr/bin/python


"""
    starter code for the validation mini-project
    the first step toward building your POI identifier!

    start by loading/formatting the data

    after that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from time import time

### import sklearn objects
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn import cross_validation

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

### it's all yours from here forward!  

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
print "Accuracy is ",acc


