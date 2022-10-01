function [clustersInitial,clusterAssignment,SSE]= KMean(trainingData,k,InitialPointsFromData)
[numRows,numCols] = size(trainingData);
%Randomly Initialize Centroids
if InitialPointsFromData==false
    clustersInitial = rand(k,numCols);
else
    ChosenStartPoints = randsample(numRows,k);
    for l=1:k
        ChosenStartPoints(l,:);
        clustersInitial(l,:)=trainingData(ChosenStartPoints(l,:),:);
end
clusterAssignment=zeros(numRows,1);
clustersFinal=zeros(k,numCols)+1000;
while abs(clustersInitial-clustersFinal)>.00001;
clustersFinal=clustersInitial;
%Assign points to clusters
TotalSumbyCluster=zeros(k,numCols);
CountbyCluster=zeros(k,1);
for i=1:numRows
    distancefromCenters=zeros(k,1);
    for j=1:k
        distancefromCenters(j,:)=sqrt(sum((clustersInitial(j,:)-trainingData(i,:)).^2));
    end
    [val,idx] = min(distancefromCenters(:));
    clusterAssignment(i,1)=idx;
    TotalSumbyCluster(idx,:)=TotalSumbyCluster(idx,:)+trainingData(i,:);
    CountbyCluster(idx,1)=CountbyCluster(idx,1)+1;
end
for l=1:k
    if CountbyCluster(l,:)>0
        clustersInitial(l,:)=TotalSumbyCluster(l,:)/(CountbyCluster(l,:));
    end
end
end
SSE=0;
for i=1:numRows
    SSE=SSE+sum((clustersInitial(clusterAssignment(i,1),:)-trainingData(i,:)))^2;
end
end