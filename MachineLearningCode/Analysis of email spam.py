import os
os.chdir('C:/Users/bnhas/OneDrive/Desktop/Classes spring 2022/OMS Analytics/Computational data Analysis/Solutions/Golden_Dana_HW6/Golden_Dana_HW6')
def readData(file='data/spambase.data'):
    import numpy as np
    x=np.genfromtxt(file, delimiter=",")
    data=np.nan_to_num(x)
    return data

dataForAnalysis=readData()
def PrepareData(data=dataForAnalysis):
    import numpy as np
    from sklearn.model_selection import train_test_split
    np.random.shuffle(data)
    XData=data[:,0:data.shape[1]-1]
    yColumn=data[:,data.shape[1]-1]
    X_train, X_test, y_train, y_test = train_test_split(XData, yColumn, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test 

X_train, X_test, y_train, y_test=PrepareData()
def CARTModel(trainX=X_train,trainy=y_train,testx=X_test,testy=y_test):
    from sklearn import tree
    from sklearn.metrics import mean_squared_error
    import matplotlib.pyplot as plt
    from sklearn.metrics import accuracy_score
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)
    tree.plot_tree(clf, max_depth=2)
    plt.show()
    tree.plot_tree(clf)
    #plt.show()
    predictedValues=clf.predict(X_test)
    Error=mean_squared_error(predictedValues,y_test)
    Score=1-accuracy_score(predictedValues,y_test)
    return Error,Score

ErrorCart,scoreCART=CARTModel()
print(ErrorCart)

def RandomForestModel(CartError=scoreCART,trainX=X_train,trainy=y_train,testx=X_test,testy=y_test):
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import mean_squared_error
    import matplotlib.pyplot as plt
    from sklearn.metrics import accuracy_score
    plt.clf()
    clf = RandomForestClassifier(max_depth=4, random_state=0)
    RFClass=clf.fit(X_train, y_train)
    predictedValues=RFClass.predict(X_test)
    ErrorRF=mean_squared_error(predictedValues,y_test)
    print(ErrorRF)
    testResults=[]
    list_nb_trees = [5, 10, 15, 30, 45, 60, 80, 100]
    for nb_trees in list_nb_trees:
        rf = RandomForestClassifier(n_estimators=nb_trees)
        rf.fit(X_train, y_train)
        testResults.append(1-accuracy_score(y_test, rf.predict(X_test)))
    plt.plot(list_nb_trees, testResults, label="Testing Score")
    cartScoreList=[scoreCART]*8
    plt.plot(list_nb_trees,cartScoreList)
    plt.show()

RandomForestModel()

def SVMMOdel(trainX=X_train,trainy=y_train,testx=X_test,testy=y_test):
    from sklearn.svm import SVC
    from sklearn import svm
    import numpy as np
    from sklearn.metrics import accuracy_score
    nonSpam=np.where(y_train == 0)[0]
    newXtrain=X_train[nonSpam]
    newYtrain=y_train[nonSpam]
    clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
    clf=clf.fit(newXtrain)
    Predictions=clf.predict(X_test)
    #print(Predictions)
    #print((len(y_test)-sum(y_test))/len(y_test))
    MisclassificationRate=1-accuracy_score(y_test, Predictions)
    print(MisclassificationRate)

SVMMOdel()
