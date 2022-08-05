def getData(file="C:/Users/bnhas/OneDrive/Desktop/Classes/Classes Summer 2022/Practicum/FootballData1.csv"):
	import numpy as np
	import pandas as pd
	return pd.read_csv(file, delimiter=",")
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
	y=data['Final Score Index']
	yQ1=data['Quarter 1 Score Index']
	yQ2=data['Quarter 2 Score Index']
	yQ3=data['Quarter 3 Score Index']
	data=pd.get_dummies(data)
	#print(data.columns.tolist())
	X=data[[' vegas_line',' over_under',' roof_dome',' roof_outdoors',' surface_astroturf',' surface_grass',' stadium_Empower Field at Mile High',' start_time_19:15:00','Average Yards Per Game Home Team','Average Points Home','Average Points Home Allowed','Average Yards Per Game away Team','Average Points away','Average Points away','Average Points Away Allowed',' Average home_time_of_possession',' Average away_time_of_possession','Average Penalties Per Game Home Team','Average Penalties Per Game away Team',' home_first_downs average',' away_first_downs average']]
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
	X_trainQ1, X_testQ1, y_trainQ1, y_testQ1 = train_test_split(X, yQ1, test_size=0.2)
	X_trainQ2, X_testQ2, y_trainQ2, y_testQ2 = train_test_split(X, yQ2, test_size=0.2)
	X_trainQ3, X_testQ3, y_trainQ3, y_testQ3 = train_test_split(X, yQ3, test_size=0.2)
	Logistic = LogisticRegression(max_iter=100).fit(X_train, y_train)
	neigh = KNeighborsClassifier(n_neighbors=50)
	Neural = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(10, 3), random_state=1)
	RF=RandomForestClassifier(max_depth=6, random_state=0)
	DT=DecisionTreeClassifier(max_depth=5)
	LogisticQ1 = LogisticRegression(max_iter=100).fit(X_train, y_trainQ1)
	neighQ1 = KNeighborsClassifier(n_neighbors=50)
	NeuralQ1 = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(10, 3), random_state=1)
	RFQ1=RandomForestClassifier(max_depth=6, random_state=0)
	DTQ1=DecisionTreeClassifier(max_depth=5)
	gnbQ1 = GaussianNB()
	LogisticQ2 = LogisticRegression(max_iter=100).fit(X_train, y_trainQ2)
	neighQ2 = KNeighborsClassifier(n_neighbors=50)
	NeuralQ2 = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(10, 3), random_state=1)
	RFQ2=RandomForestClassifier(max_depth=6, random_state=0)
	DTQ2=DecisionTreeClassifier(max_depth=5)
	gnbQ2 = GaussianNB()
	LogisticQ3 = LogisticRegression(max_iter=100).fit(X_train, y_trainQ3)
	neighQ3 = KNeighborsClassifier(n_neighbors=50)
	NeuralQ3 = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(10, 3), random_state=1)
	RFQ3=RandomForestClassifier(max_depth=6, random_state=0)
	DTQ3=DecisionTreeClassifier(max_depth=5)
	gnbQ3 = GaussianNB()
	LogisticQ1Pred=LogisticQ1.predict(X_test)
	RFQ1.fit(X_train,y_trainQ1)
	DTQ1.fit(X_train,y_trainQ1)
	gnbQ1.fit(X_train,y_trainQ1)
	NeuralQ1.fit(X_train,y_trainQ1)
	neighQ1.fit(X_train,y_trainQ1)
	RFQ1pred=RFQ1.predict(X_test)
	DTQ1pred=DTQ1.predict(X_test)
	gnbQ1Pred=gnbQ1.predict(X_test)
	NeuralPredQ1=NeuralQ1.predict(X_test)
	NeighPredQ1=neighQ1.predict(X_test)
	LogisticQ2Pred=LogisticQ2.predict(X_test)
	RFQ2.fit(X_train,y_trainQ2)
	DTQ2.fit(X_train,y_trainQ2)
	gnbQ2.fit(X_train,y_trainQ2)
	NeuralQ2.fit(X_train,y_trainQ2)
	neighQ2.fit(X_train,y_trainQ2)
	RFQ2pred=RFQ2.predict(X_test)
	DTQ2pred=DTQ2.predict(X_test)
	gnbQ2Pred=gnbQ2.predict(X_test)
	NeuralPredQ2=NeuralQ2.predict(X_test)
	LogisticQ3Pred=LogisticQ3.predict(X_test)
	NeighPredQ2=neighQ2.predict(X_test)
	RFQ3.fit(X_train,y_trainQ3)
	DTQ3.fit(X_train,y_trainQ3)
	gnbQ3.fit(X_train,y_trainQ3)
	NeuralQ3.fit(X_train,y_trainQ3)
	neighQ3.fit(X_train,y_trainQ3)
	RFQ3pred=RFQ2.predict(X_test)
	DTQ3pred=DTQ2.predict(X_test)
	gnbQ3Pred=gnbQ3.predict(X_test)
	NeuralPredQ3=NeuralQ3.predict(X_test)
	NeighPredQ3=neighQ3.predict(X_test)
	BayesPred = gnbQ1.fit(X_train, y_train).predict(X_test)
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
	print(accuracy_score(y_test,BayesPred))
	print("Score Q1")
	print(accuracy_score(y_testQ1,LogisticQ1Pred))
	print(accuracy_score(y_testQ1,RFQ1pred))
	print(accuracy_score(y_testQ1,gnbQ1Pred))
	print(accuracy_score(y_testQ1,DTQ1pred))
	print(accuracy_score(y_testQ1,NeuralPredQ1))
	print(accuracy_score(y_testQ1,NeighPredQ1))
	print("Score Q2")
	print(accuracy_score(y_testQ2,LogisticQ2Pred))
	print(accuracy_score(y_testQ2,RFQ2pred))
	print(accuracy_score(y_testQ2,gnbQ2Pred))
	print(accuracy_score(y_testQ2,DTQ2pred))
	print(accuracy_score(y_testQ2,NeuralPredQ2))
	print(accuracy_score(y_testQ2,NeighPredQ2))
	print("Score Q3")
	print(accuracy_score(y_testQ3,LogisticQ3Pred))
	print(accuracy_score(y_testQ3,RFQ3pred))
	print(accuracy_score(y_testQ3,gnbQ3Pred))
	print(accuracy_score(y_testQ3,DTQ3pred))
	print(accuracy_score(y_testQ3,NeuralPredQ3))
	print(accuracy_score(y_testQ3,NeighPredQ3))
AnalyzeData()