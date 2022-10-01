import os
import numpy as np
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
#os.chdir("C:/Users/Dana Annie/Downloads/Textbooks Spring 2022/OMS Analytics/Computational Data Analysis/homework2-7")
def getData():
	import pandas as pd
	import numpy as np
	import scipy.io
	data = scipy.io.loadmat('data/isomap.mat')
	return data['images']

DistanceMatrix=getData()

def NearestNeighborGraph(data=DistanceMatrix,epsilon=5,DistanceMeasure='euclidean'):
	import numpy as np
	NearestNeighbors=np.zeros((698, 698))
	for i in range(698):
		for j in range(698):
			difference=data[i]-data[j]
			if DistanceMeasure=="euclidean":
				distance=np.linalg.norm(difference,ord=2)
			else:
				distance=np.linalg.norm(difference,ord=1)
			if distance<epsilon:
				NearestNeighbors[i][j]+=distance
	return NearestNeighbors

NearestNeighbor=NearestNeighborGraph()
Manhattan=NearestNeighborGraph(epsilon=50,DistanceMeasure='Manhattan')
from matplotlib import pyplot as plt 
plt.imshow(NearestNeighbor, cmap='hot', interpolation='nearest')
plt.show()
def visualizeGraph(matrix=DistanceMatrix):
	import numpy as np
	import networkx as nx
	G = nx.DiGraph(matrix)
	nx.draw(G)

def PrincipalComponentProjection(matrix=DistanceMatrix):
	import numpy as np
	mean=np.mean(matrix)
	u, s, vh=np.linalg.svd(matrix)
	Eigenvectors=u[:,0:2]
	MeanTransform=(matrix-mean)
	PrincipalComponent1=np.dot(np.transpose(Eigenvectors[:,0]),MeanTransform/s[0])
	PrincipalComponent2=np.dot(np.transpose(Eigenvectors[:,1]),MeanTransform/s[1])
	ReducedForm=np.column_stack([PrincipalComponent1, PrincipalComponent2])
	return ReducedForm

def Isomap(DistanceMatrix=NearestNeighbor):
	import numpy as np
	from scipy.sparse.csgraph import shortest_path
	shortestPathMatrix=shortest_path(DistanceMatrix)
	shortestPathMatrixSquared=np.dot(shortestPathMatrix,shortestPathMatrix)
	IdentityMatrix=np.identity(shortestPathMatrixSquared.shape[0])
	onesMatrixProduct=np.dot(np.ones(shortestPathMatrixSquared.shape[0]),np.transpose(np.ones(shortestPathMatrixSquared.shape[0])))
	Hmatrix=IdentityMatrix-float(1)/float(shortestPathMatrixSquared.shape[0])*onesMatrixProduct
	ZtransposeZ=-.5*np.dot(np.dot(Hmatrix,shortestPathMatrixSquared),Hmatrix)
	u, s, vh=np.linalg.svd(ZtransposeZ)
	FirstReduced=u[0]
	SecondReduced=u[1]
	reducedFormBefore=np.column_stack([FirstReduced, SecondReduced])
	Diagonal=np.diag([s[0],s[1]])
	reducedFormAfter=np.dot(reducedFormBefore,Diagonal)
	return reducedFormAfter

IsomapData=Isomap()
IsomapDataMan=Isomap(DistanceMatrix=Manhattan)
fig, ax =plt.subplots()
ax.scatter(IsomapData[:,0],IsomapData[:,1])
Image11=np.reshape(DistanceMatrix[:,0],(64,64))
Image1 = OffsetImage(Image11, zoom=.1)
xy1 = [IsomapData[0][0], IsomapData[0][1]]
Image22=np.reshape(DistanceMatrix[:,50],(64,64))
Image2 = OffsetImage(Image22, zoom=.1)
xy2=[IsomapData[50][0], IsomapData[50][1]]
Image33=np.reshape(DistanceMatrix[:,250],(64,64))
Image3 = OffsetImage(Image33, zoom=.1)
xy3=[IsomapData[250][0], IsomapData[250][1]]
Image44=np.reshape(DistanceMatrix[:,300],(64,64))
Image4 = OffsetImage(Image44, zoom=.1)
xy4=[IsomapData[300][0], IsomapData[300][1]]
Image55=np.reshape(DistanceMatrix[:,450],(64,64))
Image5 = OffsetImage(Image55, zoom=.1)
xy5=[IsomapData[450][0], IsomapData[450][1]]
ab = AnnotationBbox(Image1, xy1,
    xybox=(30., -30.),
    xycoords='data',
    boxcoords="offset points")                                  
ax.add_artist(ab)
ab = AnnotationBbox(Image2, xy2,
    xybox=(30., -30.),
    xycoords='data',
    boxcoords="offset points")                                  
ax.add_artist(ab)
ab = AnnotationBbox(Image3, xy3,
    xybox=(30., -30.),
    xycoords='data',
    boxcoords="offset points")                                  
ax.add_artist(ab)
ab = AnnotationBbox(Image4, xy4,
    xybox=(30., -30.),
    xycoords='data',
    boxcoords="offset points")                                  
ax.add_artist(ab)
ab = AnnotationBbox(Image5, xy5,
    xybox=(30., -30.),
    xycoords='data',
    boxcoords="offset points")                                  
ax.add_artist(ab)
ax.grid(True)
plt.draw()
plt.show()
plt.close()
fig, ax =plt.subplots()
ax.scatter(IsomapDataMan[:,0],IsomapDataMan[:,1])
Image11=np.reshape(DistanceMatrix[:,0],(64,64))
Image1 = OffsetImage(Image11, zoom=.1)
xy1 = [IsomapDataMan[0][0], IsomapDataMan[0][1]]
Image22=np.reshape(DistanceMatrix[:,50],(64,64))
Image2 = OffsetImage(Image22, zoom=.1)
xy2=[IsomapDataMan[50][0], IsomapDataMan[50][1]]
Image33=np.reshape(DistanceMatrix[:,250],(64,64))
Image3 = OffsetImage(Image33, zoom=.1)
xy3=[IsomapDataMan[250][0], IsomapDataMan[250][1]]
Image44=np.reshape(DistanceMatrix[:,300],(64,64))
Image4 = OffsetImage(Image44, zoom=.1)
xy4=[IsomapDataMan[300][0], IsomapDataMan[300][1]]
Image55=np.reshape(DistanceMatrix[:,450],(64,64))
Image5 = OffsetImage(Image55, zoom=.1)
xy5=[IsomapDataMan[450][0], IsomapDataMan[450][1]]
ab = AnnotationBbox(Image1, xy1,
    xybox=(30., -30.),
    xycoords='data',
    boxcoords="offset points")                                  
ax.add_artist(ab)
ab = AnnotationBbox(Image2, xy2,
    xybox=(30., -30.),
    xycoords='data',
    boxcoords="offset points")                                  
ax.add_artist(ab)
ab = AnnotationBbox(Image3, xy3,
    xybox=(30., -30.),
    xycoords='data',
    boxcoords="offset points")                                  
ax.add_artist(ab)
ab = AnnotationBbox(Image4, xy4,
    xybox=(30., -30.),
    xycoords='data',
    boxcoords="offset points")                                  
ax.add_artist(ab)
ab = AnnotationBbox(Image5, xy5,
    xybox=(30., -30.),
    xycoords='data',
    boxcoords="offset points")                                  
ax.add_artist(ab)
plt.show()
plt.close()
k=PrincipalComponentProjection()
fig1, ax1 =plt.subplots()
ax1.scatter(k[:,0],k[:,1])
plt.show()
