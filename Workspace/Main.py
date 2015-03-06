#!/usr/bin/python

""" Complete the code in ClassifyNB.py with the sklearn
    Naive Bayes classifier to classify the terrain data.
    
    The objective of this exercise is to recreate the decision 
    boundary found in the lesson video, and make a plot that
    visually shows the decision boundary """


from prep_data import makeTerrainData
from visualization import prettyPicture, output_image
from NBClassifier import classify
from feature_format import featureFormat

import pickle
import numpy as np
import pylab as pl

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop("TOTAL",0)


features = ["salary", "bonus"]
data = featureFormat(data_dict, features)





print data

features_train, labels_train, features_test, labels_test = makeTerrainData()



clf = classify(features_train, labels_train)



    ### draw the decision boundary with the text points overlaid
prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())





