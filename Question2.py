import os
import numpy as np
#os.chdir('C:/Users/bnhas/OneDrive/Desktop/Classes spring 2022/OMS Analytics/Computational data Analysis/Problems/homework5')
def getData(file='data/RealEstate.csv'):
    from numpy import genfromtxt
    import pandas as pd
    my_data = pd.read_csv(file)
    return my_data

data=getData()

def PreprocessData(data=data):
    import numpy as np
    from sklearn.preprocessing import OneHotEncoder
    from sklearn import preprocessing
    DatanoVars=data[['Price','Bedrooms','Bathrooms','Size','Price/SQ.Ft']]
    x1=data['Status'].to_frame()
    le = preprocessing.LabelEncoder()
    X_2 = x1.apply(le.fit_transform)
    enc = OneHotEncoder()
    enc.fit(X_2)
    OneHot=enc.transform(X_2).toarray()
    PreprocessedData=np.hstack((DatanoVars,OneHot))
    return PreprocessedData

PreprocessedData=PreprocessData()
print(PreprocessedData.shape)

def RidgeRegression(data=PreprocessedData):
    import numpy as np
    np.random.seed(2)
    from sklearn.model_selection import KFold
    from sklearn.linear_model import Ridge
    import matplotlib.pyplot as plt
    from sklearn.linear_model import RidgeCV
    from sklearn.model_selection import learning_curve
    from sklearn.model_selection import validation_curve
    from sklearn.metrics import mean_squared_error
    RidgeCV=RidgeCV(cv=5,alphas=(1, 80, 5.0)).fit(data[:,1:9], data[:,0])
    clf = Ridge(alpha=1.0)
    predictions=clf.fit(data[:,1:9],data[:,0]).predict(data[:,1:9])
    Paramrange=np.arange(0,80,5)
    train_scores, test_scores=validation_curve(clf,data[:,1:9],data[:,0],param_name="alpha",param_range=Paramrange)
    plt.plot(Paramrange,test_scores)
    plt.title("Validation Curve with Ridge")
    plt.xlabel("alpha")
    plt.ylabel("Score")
    plt.show()
    print(RidgeCV.coef_)
    print(RidgeCV.intercept_)
    print(RidgeCV.alpha_)
    print(mean_squared_error(data[:,0], predictions))

RidgeRegression()


def LASSORegression(data=PreprocessedData):
    import numpy as np
    from sklearn.model_selection import KFold
    from sklearn.linear_model import Lasso
    import matplotlib.pyplot as plt
    from sklearn.model_selection import learning_curve
    from sklearn.model_selection import KFold
    from sklearn.linear_model import LassoCV
    import matplotlib.pyplot as plt
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    from sklearn.model_selection import validation_curve
    from sklearn.linear_model import lasso_path
    np.random.seed(3)
    LassoCV=LassoCV(cv=5, random_state=0).fit(data[:,1:9], data[:,0])    
    Paramrange=np.arange(1,3000,10)
    clf=Lasso()
    train_scores, test_scores=validation_curve(clf,data[:,1:9],data[:,0],param_name="alpha",param_range=Paramrange)
    plt.plot(Paramrange,test_scores)
    plt.title("Validation Curve with Lasso")
    plt.xlabel("alpha")
    plt.ylabel("Score")
    plt.show()
    _, coef_path, _=lasso_path(data[:,1:9], data[:,0], alphas=Paramrange)
    plt.plot(Paramrange,coef_path.reshape(300,7))
    plt.show()
    print(LassoCV.coef_)
    print(LassoCV.intercept_)
    print(LassoCV.alpha_)

LASSORegression()