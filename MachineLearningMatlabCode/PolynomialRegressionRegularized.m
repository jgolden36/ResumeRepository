function [CostFunctionTrain,CostFunctionCrossValid,CostFunctionTest,beta,lambda] = PolynomialRegressionRegularized(data)
[training_data,testing_data,crossValidation_data] = split_data(data);
[rowtrain columntrain] = size(training_data);
[rowcrossValid columntrain] = size(crossValidation_data);
[rowTest columntrain] = size(testing_data);
FullDataSetTrain=[training_data(:,1)];
FullDataSetCrossValidation=[ones(rowcrossValid,1) crossValidation_data(:,1)];
FullDataSetTest=[ones(rowTest,1) testing_data(:,1)];
CostFunctionTrain=zeros(30,1);
CostFunctionCrossValid=zeros(30,1);
FullDataSetTrainNormal=(FullDataSetTrain-mean(training_data(:,1)))./std(training_data(:,1));
for i=2:10
    FullDataSetTrain=[(training_data(:,1)).^i FullDataSetTrain];
    standardDev=std(training_data(:,1).^i);
    mean(training_data(:,1).^i);
    (FullDataSetTrain(:,i)-mean(training_data(:,1).^i));
    FullDataSetTrainNormal=[FullDataSetTrainNormal (training_data(:,1).^i-mean(training_data(:,1).^i))./std(training_data(:,1).^i)];
    FullDataSetCrossValidation=[FullDataSetCrossValidation crossValidation_data(:,1).^i];
    FullDataSetTest=[FullDataSetTest FullDataSetTest(:,1).^i];
end
for lambda=0:30
    beta=inv(FullDataSetTrainNormal.'*FullDataSetTrainNormal+lambda)*FullDataSetTrainNormal.'*((training_data(:,2)-mean(training_data(:,2)))/std(training_data(:,2)));
    beta0=mean(training_data(:,2));
    for i=1:10
        beta(i,1)=beta(i,1)*(std(training_data(:,1).^i)/std(training_data(:,2)));
        beta0=beta0-beta(i,1)*mean(training_data(:,1).^i);
    end
    beta=[beta0;beta];
    FullDataSetTrain1=[ones(rowtrain,1) FullDataSetTrain];
    CostFunctionTrain(lambda+1,1)=sum((training_data(:,2)-FullDataSetTrain1*beta).^2);
    CostFunctionCrossValid(lambda+1,1)=sum((crossValidation_data(:,2)-FullDataSetCrossValidation*beta).^2);
end
scatter(linspace(0,30,31),CostFunctionTrain)
title('Train Cost Function')
xlabel('Polynomial Degree')
ylabel('Sum of Squared Errors')
shg
scatter(linspace(0,30,31),CostFunctionCrossValid)
title('Cross Validation Cost Function')
xlabel('Polynomial Degree')
ylabel('Sum of Squared Errors')
shg
[minimum,index]=min(CostFunctionCrossValid);
lambda=index-1;
beta=inv(FullDataSetTrainNormal.'*FullDataSetTrainNormal+lambda)*FullDataSetTrainNormal.'*((training_data(:,2)-mean(training_data(:,2)))/std(training_data(:,2)));
for i=1:10
    beta(i,1)=beta(i,1)*(std(training_data(:,1).^i)/std(training_data(:,2)));
    beta0=beta0-beta(i,1)*mean(training_data(:,1).^i);
end
beta=[beta0;beta];
CostFunctionTest=sum((testing_data(:,2)-FullDataSetTest*beta).^2);
