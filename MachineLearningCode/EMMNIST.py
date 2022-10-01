import os
import numpy as np
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import numpy as np
import random
import numpy.matlib
import pandas as pd
from scipy.stats import multivariate_normal as mvn
import matplotlib.pyplot as plt
import time
import math
import seaborn as sns 
from sklearn import preprocessing
from sklearn import cluster
#os.chdir("C:/Users/Dana Annie/Downloads/Textbooks Spring 2022/OMS Analytics/Computational Data Analysis/homework3")
def getDataandLabels():
    import pandas as pd
    import numpy as np
    import scipy.io
    data = scipy.io.loadmat('data/data.mat')
    labels=scipy.io.loadmat('data/label.mat')
    return data['data'],labels['trueLabel']

x,labels=getDataandLabels()
def PrincipalComponent(data=x):
    import numpy as np
    u, s, vh=np.linalg.svd(x)
    mean=np.mean(x)
    Eigenvectors=u[:,0:4]
    MeanTransform=(x-mean)
    PrincipalComponent1=np.dot(np.transpose(Eigenvectors[:,0]),MeanTransform/s[0])
    PrincipalComponent2=np.dot(np.transpose(Eigenvectors[:,1]),MeanTransform/s[1])
    PrincipalComponent3=np.dot(np.transpose(Eigenvectors[:,2]),MeanTransform/s[2])
    PrincipalComponent4=np.dot(np.transpose(Eigenvectors[:,3]),MeanTransform/s[3])
    ReducedForm=np.column_stack([PrincipalComponent1, PrincipalComponent2,PrincipalComponent3,PrincipalComponent4])
    return ReducedForm,Eigenvectors,np.diagflat(s[0:4]),mean
iterationNumber=0
dataForEM,eigenvect,eigenval,meanfinder=PrincipalComponent()
numberMixtures=2
pi = np.random.random(numberMixtures)
pi = pi/np.sum(pi)
initialMean= np.random.randn(numberMixtures,4)
Old_mean = initialMean.copy()
sigma = []
m,n=dataForEM.shape
for ii in range(numberMixtures):
    dummy = np.random.randn(4, 4)
    sigma.append(dummy@dummy.T)
tau = np.full((m, numberMixtures), fill_value=0.)
maxIter= 100
tol = 1e-3

plt.ion()
loglikelihoodTracker=[]
iterations=[]
for ii in range(100):

    # E-step    
    for kk in range(numberMixtures):
        tau[:, kk] = pi[kk] * mvn.pdf(dataForEM, initialMean[kk], sigma[kk])
    # normalize tau
    sum_tau = np.sum(tau, axis=1)
    sum_tau.shape = (m,1)    
    tau = np.divide(tau, np.tile(sum_tau, (1, numberMixtures)))
    
    
    # M-step
    for kk in range(numberMixtures):
        # update prior
        pi[kk] = np.sum(tau[:, kk])/m
        
        # update component mean
        initialMean[kk] = dataForEM.T @ tau[:,kk] / np.sum(tau[:,kk], axis = 0)
        
        # update cov matrix
        dummy = dataForEM - np.tile(initialMean[kk], (m,1)) # X-mu
        sigma[kk] = dummy.T @ np.diag(tau[:,kk]) @ dummy / np.sum(tau[:,kk], axis = 0)
    loglikelihoodfunction=0
    #for kk in range(numberMixtures):
    #for i in range(m):
    #loglikelihoodfunction=loglikelihoodfunction+tau[kk]*(math.log(pi[kk])-.5*np.transpose((dataForEM[i]-initialMean[kk]))*np.linalg.inv(sigma)*(dataForEM[i]-initialMean[kk])-.5*math.log(np.linalg.det(sigma))-n/2*(math.log(2*math.pi)))
    likelihood=(np.log(np.sum([k*mvn(initialMean[i],sigma[j]).pdf(dataForEM) for k,i,j in zip(pi,range(len(initialMean)),range(len(sigma)))])))
    loglikelihoodTracker.append(likelihood)
    iterationNumber=iterationNumber+1
    iterations.append(iterationNumber)
    print('-----iteration---',ii)   
    #plt.scatter(dataForEM[:,0], dataForEM[:,1], c= tau[:,0])
    #plt.scatter(dataForEM[:,2], dataForEM[:,3], c= tau[:,1])
    #plt.axis('scaled')
    #plt.draw()
    #plt.pause(.1)
    if np.linalg.norm(initialMean-Old_mean) < tol:
        plt.plot(iterations,loglikelihoodTracker)
        plt.xlabel("Iteration")
        plt.ylabel("Loglikelihood")
        break
    Old_mean = initialMean.copy()
    if ii==99:
        print('max iteration reached')
        break
MeanReconstructed=np.dot(np.dot(dataForEM,eigenval),np.transpose(initialMean))+meanfinder
#varReconstructed=np.dot(np.dot(np.dot(dataForEM,eigenval),sigma),np.dot(eigenval,np.transpose(dataForEM)))
plt.imshow((np.reshape(MeanReconstructed[:,0],(10,199))))
plt.imshow((np.reshape(MeanReconstructed[:,1],(10,199))))
ax = sns.heatmap(sigma[0])
plt.show()
ax = sns.heatmap(sigma[1])
plt.show()
labelnumber=0
correctMatch=0
Total=len(labels[0])
for i in tau:
    if i[0]>i[1]:
        labelchoice=2
        if labels[0][labelnumber]-labelchoice==0:
            correctMatch=correctMatch+1
    else:
        labelchoice=6
        if labels[0][labelnumber]-labelchoice==0:
            correctMatch=correctMatch+1
    labelnumber=labelnumber+1
Mismatchrate=1-(float(correctMatch))/float(Total)
print(Mismatchrate)
labelnumber=0
kmeans=cluster.KMeans(2).fit(x)
labelsKmeans=kmeans.labels_
correctMatchkmeans=0
for i in labelsKmeans:
    if i==1:
        labelchoice=6
        if labels[0][labelnumber]-labelchoice==0:
            correctMatchkmeans=correctMatchkmeans+1
    else:
        labelchoice=2
        if labels[0][labelnumber]-labelchoice==0:
            correctMatchkmeans=correctMatchkmeans+1
    labelnumber=labelnumber+1
Mismatchratekmeans=1-(float(correctMatchkmeans))/float(Total)
print(Mismatchratekmeans)
