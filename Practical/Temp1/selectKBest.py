from get_data import getData


data_dict = getData() 

counter=0

for fold in range(500):
    X_train, X_test, y_train, y_test = crossval.train_test_split(X, y, test_size=0.3)
    clf = LinearRegression()
    #clf = RidgeCV()
    #clf = LogisticRegression()
    #clf=ElasticNetCV()

    b = fs.SelectKBest(fs.f_regression, k=1) #k is number of features.
    b.fit(X_train, y_train)
    #print b.get_params

    X_train = X_train[:, b.get_support()]
    X_test = X_test[:, b.get_support()]


    clf.fit(X_train,y_train)
    sc = clf.score(X_train, y_train)
    training.append(sc)
    #print "The training R-Squared for fold " + str(1) + " is " + str(round(sc*100,1))+"%"
    sc = clf.score(X_test, y_test)
    actual.append(sc)
    #print "The actual R-Squared for fold " + str(1) + " is " + str(round(sc*100,1))+"%"

