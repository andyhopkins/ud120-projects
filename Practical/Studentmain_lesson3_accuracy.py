#!/usr/bin/python

""" lecture and example code for decision tree unit """

import sys
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl


features_train, labels_train, features_test, labels_test = makeTerrainData()

from sklearn import tree

clf2 = tree.DecisionTreeClassifier(min_samples_split = 2)
clf2 = clf2.fit(features_train, labels_train)
pred2 = clf2.predict(features_test)
from sklearn.metrics import accuracy_score
acc_min_samples_split_2 = accuracy_score(pred2, labels_test)
print "Accuracy for min_sample_split = 2 is ",acc_min_samples_split_2 * 100,"%"


clf50 = tree.DecisionTreeClassifier(min_samples_split = 50)
clf50 = clf50.fit(features_train, labels_train)
pred50 = clf50.predict(features_test)
from sklearn.metrics import accuracy_score
acc_min_samples_split_50 = accuracy_score(pred50, labels_test)
print "Accuracy for min_sample_split = 50 is ",acc_min_samples_split_50 * 100,"%"

