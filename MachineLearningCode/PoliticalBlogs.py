def L2Norm(Z,centers):
    import numpy as np
    m=len(Z)
    n=len(centers)
    distancer=np.empty((m,n))
    for i in range(m):
        distancer[i,:]=np.linalg.norm(Z[i,:]-centers, ord=2, axis=1)**2
    return distancer

import os
#os.chdir("C:/Users/Dana Annie/Downloads/Homework1/data")
def spectralClustering(nodesFile="Data/nodes.txt",edgesFile="Data/edges.txt",k=2):
    # I used some of the implementation I wrote for K-means from CSE 6040 for this. I used my implementation from the homework, not the professor's code
    import pandas as pd
    import numpy as np
    import random
    import math
    nodes=pd.read_csv(nodesFile,delimiter="\t",header=None,names=["index","website","political","blogfrom"])
    edges=pd.read_csv(edgesFile,delimiter="\t",header=None,names=["edge","connected"])
    TotalNodes=max(edges.iloc[:, 0].max(),edges.iloc[:, 1].max())
    zeroesMatrix=np.zeros((TotalNodes+1,TotalNodes+1))
    zeroesMatrix1=np.zeros((TotalNodes+1,TotalNodes+1))
    AdjacencyMatrix=zeroesMatrix
    DiagonalMatrix=zeroesMatrix1
    rownumber=len(edges)
    for i in range(0,rownumber):
        node=int(edges["edge"][i])
        connected=int(edges["connected"][i])
        AdjacencyMatrix[node,connected]=1
        AdjacencyMatrix[connected,node]=1
        DiagonalMatrix[node,node]+=1
        DiagonalMatrix[connected,connected]+=1
    Laplacian=DiagonalMatrix-AdjacencyMatrix
    w, v=np.linalg.eig(Laplacian)
    clusterEigenvectors=v[w==0]
    kSmallest=clusterEigenvectors[-k:]
    Z=np.column_stack((kSmallest[0],kSmallest[1]))
    sample=np.random.randint(0,len(Z), size=k)
    initialCenters=Z[sample,:]
    clue=0
    convergence=0
    Newcenters=initialCenters
    while convergence!=1:
        initialCenters=Newcenters
        #computeDistance
        distanceMatrix=L2Norm(Z,Newcenters)
        #assignClusterLabels
        labelAssignment=np.argmin(distanceMatrix,axis=1)
        #UpdateCenters
        Newcenters = np.empty((k, 2))
        for j in range(k):
            Newcenters[j,:]=np.mean(Z[labelAssignment==j,:],axis=0)
        #convergenceCheck
        if set([tuple(x) for x in initialCenters]) == set([tuple(x) for x in Newcenters]):
            convergence=1
        print("iteration number")
        print(clue)
        clue=clue+1
    estimateMatrix=np.zeros(k)
    TotalinCat=np.zeros(k)
    DecidedValue=np.zeros(k)
    MatchMatrix=np.zeros(k)
    MismatchRate=np.zeros(k)
    for l in range(1489):
        centerChosen=labelAssignment[l]
        truevalue=nodes["political"][l]
        estimateMatrix[centerChosen]+=truevalue
        TotalinCat[centerChosen]+=1
    for w in range(k):
        if estimateMatrix[w]/TotalinCat[w]<.5:
            DecidedValue[w]=0
        else:
            DecidedValue[w]=1
    for x in range(1489):
        center=labelAssignment[x]
        if DecidedValue[center]==nodes["political"][x]:
            MatchMatrix[labelAssignment[x]]+=1
    for c in range(k):
        MismatchRate[c]+=1-(float(MatchMatrix[c])/float(TotalinCat[c]))
    print(TotalinCat)
    print(MismatchRate)
    return MismatchRate

spectralClustering(k=2)
