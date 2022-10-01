function StandardizedData= Standardize(TrainingData)
meanVector=mean(TrainingData);
standardDeviationVector=std(TrainingData);
StandardizedData=(TrainingData-meanVector)./standardDeviationVector;
end