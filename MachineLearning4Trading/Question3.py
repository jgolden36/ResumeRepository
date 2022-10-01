import os
#os.chdir('C:/Users/bnhas/OneDrive/Desktop/Classes spring 2022/OMS Analytics/Computational data Analysis/Problems/homework5')
def getData(file='data/cs.mat'):
    import pandas as pd
    import numpy as np
    import scipy.io
    data = scipy.io.loadmat(file)
    return data['img']

data=getData()

#print(data.shape)

def LASSORegression(data=data):
    import numpy as np
    from sklearn.model_selection import KFold
    from sklearn.linear_model import Lasso
    from sklearn.linear_model import LassoCV
    import matplotlib.pyplot as plt
    from sklearn.model_selection import learning_curve
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    from sklearn.model_selection import validation_curve
    A=np.random.normal(0,1,(2500,1300))
    Noise=np.random.normal(0,25,(1300,1))
    newData=data.reshape((2500,1))
    kf = KFold(n_splits=10)
    #kf.get_n_splits(X)
    LassoCV=LassoCV(cv=10, random_state=0).fit(A, newData.reshape(2500))
    LassoPred=LassoCV.predict(A)
    plt.imshow(LassoPred.reshape((50,50)))
    plt.show()
    clf = Lasso()
    Paramrange=np.arange(0,1,.01)
    train_scores, test_scores=validation_curve(clf,A,newData,param_name="alpha",param_range=Paramrange)
    plt.plot(Paramrange,test_scores)
    plt.title("Validation Curve with Lasso")
    plt.xlabel("alpha")
    plt.ylabel("Score")
    plt.show()


LASSORegression()

def RidgeRegression(data=data):
    import numpy as np
    from sklearn.model_selection import KFold
    from sklearn.linear_model import Ridge
    from sklearn.linear_model import RidgeCV
    import matplotlib.pyplot as plt
    from sklearn.model_selection import validation_curve
    A=np.random.normal(0,1,(2500,1300))
    newData=data.reshape((2500,1))
    RidgeCV=RidgeCV(cv=10).fit(A, newData.reshape(2500))
    RidgePred=RidgeCV.predict(A)
    clf = Ridge()
    train_scores, test_scores=validation_curve(clf,A,newData,param_name="alpha",param_range=[1e-3, 1e-2, 1e-1, 1])
    plt.plot([1e-3, 1e-2, 1e-1, 1],test_scores)
    plt.title("Validation Curve with Ridge")
    plt.xlabel("alpha")
    plt.ylabel("Score")
    plt.show()
    plt.imshow(RidgePred.reshape((50,50)))
    plt.show()

RidgeRegression()
