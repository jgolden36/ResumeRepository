def getData(file="C:/Users/bnhas/OneDrive/Desktop/Classes/Classes Summer 2022/Practicum/college football Data1.csv"):
	import numpy as np
	import pandas as pd
	with open(file) as f:
		print(f)
	return pd.read_csv(file, delimiter=",", encoding="cp1252")

data=getData()
def AnalyzeData(data=data):
	import pandas as pd
	import numpy as np
	import sys
	np.set_printoptions(threshold=sys.maxsize)
	from sklearn.neighbors import KNeighborsClassifier
	from sklearn.metrics import accuracy_score
	from sklearn.model_selection import train_test_split
	from sklearn.linear_model import LogisticRegression
	from sklearn.neural_network import MLPClassifier
	from sklearn.ensemble import RandomForestClassifier
	from sklearn.tree import DecisionTreeClassifier
	from sklearn.naive_bayes import GaussianNB
	pd.set_option('display.max_columns', None)
	y=data['Score Index']
	#data=pd.get_dummies(data)
	print(data.columns.tolist())
	X=data[['home_post_win_prob','home_pregame_elo','away_pregame_elo']]
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
	Logistic = LogisticRegression(max_iter=100).fit(X_train, y_train)
	neigh = KNeighborsClassifier(n_neighbors=50)
	Neural = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(10, 3), random_state=1)
	RF=RandomForestClassifier(max_depth=6, random_state=0)
	DT=DecisionTreeClassifier(max_depth=5)
	DT.fit(X_train,y_train)
	DTpred=DT.predict(X_test)
	RF.fit(X_train,y_train)
	RFprediction=RF.predict(X_test)
	Neural.fit(X_train,y_train)
	PredictionNeural=Neural.predict(X_test)
	model=neigh.fit(X_train, y_train)
	PredictionNeighbors=model.predict(X_test)
	PredictionLogistic=Logistic.predict(X_test)
	print("Score Final")
	print(accuracy_score(y_test,PredictionLogistic))
	print(accuracy_score(y_test,PredictionNeighbors))
	print(accuracy_score(y_test,PredictionNeural))
	print(accuracy_score(y_test,RFprediction))
	print(accuracy_score(y_test,DTpred))
AnalyzeData()