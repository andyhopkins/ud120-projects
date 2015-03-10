import matplotlib.pyplot
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.svm import SVC

#sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import test_classifier, dump_classifier_and_data

def classify(my_dataset, features_list):  
    
    ### remove outliers
    for key in ["TOTAL"]:
        my_dataset.pop(key,0)
    
    #feature = 'total_stock_value'
    #for key in data_dict:
    #    if data_dict[key][feature] != 'NaN' and data_dict[key][feature] > 20000000:
    #        print key,'',data_dict[key][feature]
    
    ### Extract features and labels from dataset for local testing
    data = featureFormat(my_dataset, features_list, sort_keys = True)
    labels, features = targetFeatureSplit(data)
    
    #print features
    
    ### Task 4: Try a varity of classifiers
    ### Please name your classifier clf for easy export below.
    ### Note that if you want to do PCA or other multi-stage operations,
    ### you'll need to use Pipelines. For more info:
    ### http://scikit-learn.org/stable/modules/pipeline.html
    
    #clf = GaussianNB()    # Provided to give you a starting point. Try a varity of classifiers.
    #clf = tree.DecisionTreeClassifier(min_samples_split = 50)
    clf = SVC(kernel="linear")
    ### Task 5: Tune your classifier to achieve better than .3 precision and recall 
    ### using our testing script.
    ### Because of the small size of the dataset, the script uses stratified
    ### shuffle split cross validation. For more info: 
    ### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html
    
    test_classifier(clf, my_dataset, features_list)
    
    ### Dump your classifier, dataset, and features_list so 
    ### anyone can run/check your results.
    
    #dump_classifier_and_data(clf, my_dataset, features_list)
    
    
    for point in data:
        salary = point[1]
        total_payments = point[2]
        matplotlib.pyplot.scatter( salary, total_payments, color = "g" )
    
    matplotlib.pyplot.xlabel("salary")
    matplotlib.pyplot.ylabel("total_payments")
    matplotlib.pyplot.show()

    return clf