import os
#os.chdir("C:/Users/Dana Annie/Downloads/Textbooks Spring 2022/OMS Analytics/Computational Data Analysis/homework2-7/data")
def importDataFromFile(file="data/food-consumption.csv"):
	import numpy as np
	import pandas as pd
	from numpy import genfromtxt
	FoodConsumption=pd.read_csv('food-consumption.csv')
	FoodConsumption=FoodConsumption.to_numpy()
	return FoodConsumption[:,1:]

def PrincipalComponent(file="data/food-consumption.csv",foodAsFeature=True):
	import numpy as np
	x=importDataFromFile(file)
	if foodAsFeature==False:
		x=np.transpose(x)
	u, s, vh=np.linalg.svd(x.astype('float64'))
	mean=np.mean(x)
	Eigenvectors=u[:,0:2]
	MeanTransform=(x-mean)
	PrincipalComponent1=np.dot(np.transpose(Eigenvectors[:,0]),MeanTransform/s[0])
	PrincipalComponent2=np.dot(np.transpose(Eigenvectors[:,1]),MeanTransform/s[1])
	ReducedForm=np.column_stack([PrincipalComponent1, PrincipalComponent2])
	return ReducedForm

x=PrincipalComponent()
y=PrincipalComponent(foodAsFeature=False)

countriesList=['Germany', 'Italy', 'France', 'Holland', 'Belgium', 'Luxembourg', 'England', 'Portugal', 'Austria', 'Switzerland', 'Sweden', 'Denmark', 'Norway', 'Finland', 'Spain', 'Ireland']
FoodList=['Real coffee', 'Instant coffee', 'Tea', 'Sweetener', 'Biscuits', 'Powder soup', 'Tin soup', 'Potatoes', 'Frozen fish', 'Frozen veggies', 'Apples', 'Oranges', 'Tinned fruit', 'Jam', 'Garlic', 'Butter', 'Margarine', 'Olive oil', 'Yoghurt', 'Crisp bread']

from matplotlib import pyplot as plt 
fig, ax =plt.subplots()
ax.scatter(x[:,0],x[:,1])
for i, txt in enumerate(FoodList):
    ax.annotate(txt, (x[:,0][i], x[:,1][i]))
plt.show()
fig, ax =plt.subplots()
ax.scatter(y[:,0],y[:,1])
for i, txt in enumerate(countriesList):
    ax.annotate(txt, (y[:,0][i], y[:,1][i]))
plt.show()
