
import random


def makeTerrainData(n_points=20):
###############################################################################
### create the dataset
    random.seed(42)
    grade = [random.random() for ii in range(0,n_points)]
    bumpy = [random.random() for ii in range(0,n_points)]
    error = [random.random() for ii in range(0,n_points)]
    
### determine label 0.0 is fast 1.0 is slow 
    y = [round(grade[ii]*bumpy[ii]+0.3+0.1*error[ii]) for ii in range(0,n_points)]

    for ii in range(0, len(y)):
        if grade[ii]>0.8 or bumpy[ii]>0.8:
            y[ii] = 1.0
    
### merge grade and bumpy datasets into tuples
    X = [[gg, ss] for gg, ss in zip(grade, bumpy)]
    
### split into train/test sets  
    split = int(0.75*n_points)
    X_train = X[0:split]
    X_test  = X[split:]
    y_train = y[0:split]
    y_test  = y[split:]


    return X_train, y_train, X_test, y_test
#    return training_data, test_data

features_train, labels_train, features_test, labels_test = makeTerrainData()