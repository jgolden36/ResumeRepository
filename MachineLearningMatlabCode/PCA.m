function [PrincipalComponents,percentageVarianceExplained] = PCA(TrainingData,Components)
meanVector=mean(TrainingData);
standardDeviationVector=std(TrainingData);
demeanedScaledData=(TrainingData-meanVector)./standardDeviationVector;
[U,S,V]=svd(demeanedScaledData);
percentageVarianceExplained=zeros(Components,1);
for i=1:Components
    percentageVarianceExplained(i,:)=sum(S(i,:))/sum(S,'all');
end
PrincipalComponents=(V(:,1:Components)).'*demeanedScaledData.';
end