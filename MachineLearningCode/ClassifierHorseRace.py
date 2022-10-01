import os
os.chdir('C:/Users/bnhas/OneDrive/Documents/Classes spring 2022/OMS Analytics/Computational data Analysis/Problems/homework4/homework4')
def getDataPart1(file='data/marriage.csv'):
    from numpy import genfromtxt
    my_data = genfromtxt(file, delimiter=',')
    return my_data

DataforAnalysis1=getDataPart1()
def AnalyzeDataPart1(data=DataforAnalysis1):
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import GaussianNB
    from sklearn.linear_model import LogisticRegression
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.decomposition import PCA
    import matplotlib.pyplot as plt
    numberofColumns=data.shape[1]
    X=data[:,0:numberofColumns-1]
    y=data[:,numberofColumns-1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    logistic=LogisticRegression(random_state=0).fit(X_train, y_train)
    PredLog=logistic.predict(X_test)
    ProbLog=logistic.predict_proba(X_test)
    gnb = GaussianNB()
    BayesPred = gnb.fit(X_train, y_train).predict(X_test)
    neigh = KNeighborsClassifier(n_neighbors=20)
    NeighborsModel=neigh.fit(X_train, y_train)
    NeighborsPrediction=NeighborsModel.predict(X_test)
    NeighborError=np.sum(np.absolute(NeighborsPrediction-y_test))/y_test.shape[0]
    LogisticError=np.sum(np.absolute(PredLog-y_test))/y_test.shape[0]
    BayesError=np.sum(np.absolute(BayesPred-y_test))/y_test.shape[0]
    print("Logistic Regression Error is ")
    print(float(LogisticError))
    print("Naive Bayes Error is ")
    print(BayesError)
    print("Nearest Neighbors Error is ") 
    print(NeighborError)
    pcaReduction=PCA(n_components=2)
    pcaReduction.fit(np.transpose(data))
    PCA11=pcaReduction.components_[0:2]
    gnb = GaussianNB()
    BayesPred = gnb.fit(np.transpose(PCA11), y).predict(np.transpose(PCA11))
    LogModel=LogisticRegression(random_state=0).fit(np.transpose(PCA11), y)
    PredLog=LogModel.predict(np.transpose(PCA11))
    neigh = KNeighborsClassifier(n_neighbors=20)
    Neighborspred=neigh.fit(np.transpose(PCA11), y).predict(np.transpose(PCA11))
    plt.scatter(PCA11[0], PCA11[1], c=y, ec='k')
    plt.show()
    plt.scatter(PCA11[0], PCA11[1], c=BayesPred, ec='k')
    plt.show()
    plt.scatter(PCA11[0], PCA11[1], c=PredLog, ec='k')
    plt.show()
    plt.scatter(PCA11[0], PCA11[1], c=Neighborspred, ec='k')
    plt.show()


AnalyzeDataPart1()

def getDataPart2(file='data/mnist_10digits.mat'):
    import pandas as pd
    import numpy as np
    import scipy.io
    data = scipy.io.loadmat(file)
    xtraining=data['xtrain']
    ytraining=data['ytrain']
    xtesting=data['xtest']
    ytesting=data['ytest']
    return xtraining,ytraining,xtesting,ytesting

xtraining,ytrain,xtest,ytest=getDataPart2()

xtrain,ytrain,xtest,ytest=getDataPart2()
def AnalyzeDataPart2(Trainsetx=xtrain,Trainsety=ytrain,Testsetx=xtest,Testsety=ytest):
    import numpy as np
    from sklearn.linear_model import LogisticRegression
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn import svm
    from sklearn.neural_network import MLPClassifier
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import precision_recall_fscore_support
    from sklearn.svm import SVC
    from sklearn.svm import LinearSVC
    Trainsetx=Trainsetx/255
    Testsetx=Testsetx/255
    SVMModel = LinearSVC()
    SVMModel.fit(Trainsetx, Trainsety.reshape(60000))
    SVMPred=SVMModel.predict(Testsetx)
    logistic=LogisticRegression(multi_class="multinomial",max_iter=10000,solver='newton-cg').fit(Trainsetx, Trainsety.reshape(60000))
    print("done Logistic")
    PredLog=logistic.predict(Testsetx)
    ProbLog=logistic.predict_proba(Testsetx)
    neigh = KNeighborsClassifier(n_neighbors=10)
    NeighborsModel=neigh.fit(Trainsetx, Trainsety.reshape(60000))
    print("done Neighbors")
    RadialBasis=SVC(kernel='rbf')
    RadialBasisModel=RadialBasis.fit(Trainsetx, Trainsety.reshape(60000))
    NeighborsPrediction=neigh.predict(Testsetx)
    RadialBasisPred=RadialBasisModel.predict(Testsetx)
    print("done radial")
    NeuralNet = MLPClassifier(solver='sgd', alpha=1e-5,hidden_layer_sizes=(20, 10),max_iter=10000)
    Trainsetx32=Trainsetx.astype(np.float32)
    Trainsety32=Trainsety.astype(np.float32)
    Testsetx32=Testsetx.astype(np.float32)
    Testsety32=Testsety.astype(np.float32)
    NeuralNet.fit(Trainsetx32, Trainsety32.reshape(60000))
    NeuralNetPred=NeuralNet.predict(Testsetx32)
    logConfusion=confusion_matrix(Testsety, PredLog)
    NeighborsConfusion=confusion_matrix(Testsety.reshape(10000), NeighborsPrediction)
    NeuralConfusion=confusion_matrix(Testsety.reshape(10000), NeuralNetPred)
    RadialBasisconfusion=confusion_matrix(Testsety.reshape(10000),RadialBasisPred)
    SVMConfusion=confusion_matrix(Testsety.reshape(10000), SVMPred)
    print("The SVM Non-kernal confusion matrix was ")
    print(SVMConfusion)
    print("The neural network confusion matrix was")
    print(NeuralConfusion)
    print("The Logistic Confusion Matrix was")
    print(logConfusion)
    print("The Nearest neighbors Confusion Matrix was")
    print(NeighborsConfusion)
    print("The SVM kernal confusion matrix was ")
    print(RadialBasisconfusion)
    scoringSVM=precision_recall_fscore_support(Testsety.reshape(10000),SVMPred)
    scoringNeuralNet=precision_recall_fscore_support(Testsety.reshape(10000),NeuralNetPred)
    scoringLogistic=precision_recall_fscore_support(Testsety.reshape(10000),PredLog)
    scoringNeighbors=precision_recall_fscore_support(Testsety.reshape(10000),NeighborsPrediction)
    scoringKernalSVM=precision_recall_fscore_support(Testsety.reshape(10000),RadialBasisPred)
    print("The SVM non-kernal scoring list is ")
    print(scoringSVM)
    print("The SVM kernal scoring list is ")
    print(scoringKernalSVM)
    print("The Neural Net scoring list is ")
    print(scoringNeuralNet)
    print("The Nearest Neighbors scoring list is ")
    print(scoringNeighbors)
    print("The Logistic scoring list is ")
    print(scoringLogistic)

AnalyzeDataPart2()
