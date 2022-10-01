function [CostFunctionTrain,CostFunctionCrossValid,CostFunctionTest,beta] = PolynomialRegressions(data)
[training_data,testing_data,crossValidation_data] = split_data(data);
[rowtrain columntrain] = size(training_data);
[rowcrossValid columntrain] = size(crossValidation_data);
[rowTest columntrain] = size(testing_data);
PolynomialData=training_data(:,1);
y=training_data(:,2);
betaMatrix=zeros(12,13);
CostFunctionTrain=zeros(10,1);
PolynomialDataCrossValidation=crossValidation_data(:,1);
PolynomialData=[ones(rowtrain,1) training_data(:,1)];
PolynomialDataCrossValidation=[ones(rowcrossValid,1) crossValidation_data(:,1)];
PolynomialDataTest=[ones(rowTest,1) testing_data(:,1)];
betaValue=inv(PolynomialData.'*PolynomialData)*PolynomialData.'*y;
CostFunctionTrain(1,:)=sum((y-PolynomialData*betaValue).^2);
CostFunctionCrossValid(1,:)=sum((crossValidation_data(:,2)-PolynomialDataCrossValidation*betaValue).^2);
betaMatrix(1:2,1)=betaMatrix(1:2,1)+betaValue;
for i=2:10
    PolynomialData=[PolynomialData,training_data(:,1).^i];
    PolynomialDataCrossValidation=[PolynomialDataCrossValidation crossValidation_data(:,1).^i];
    PolynomialDataTest=[PolynomialDataTest testing_data(:,1).^i];
    betaValue=inv(PolynomialData.'*PolynomialData)*PolynomialData.'*y;
    CostFunctionTrain(i,:)=sum((y-PolynomialData*betaValue).^2);
    CostFunctionCrossValid(i,:)=sum((crossValidation_data(:,2)-PolynomialDataCrossValidation*betaValue).^2);
    betaMatrix(1:i+1,i)=betaMatrix(1:i+1,i)+betaValue;
end
scatter(linspace(1,10,10),CostFunctionTrain)
title('Train Cost Function')
xlabel('Polynomial Degree')
ylabel('Sum of Squared Errors')
shg
scatter(linspace(1,10,10),CostFunctionCrossValid)
title('Cross Validation Cost Function')
xlabel('Polynomial Degree')
ylabel('Sum of Squared Errors')
shg
[minimum,index]=min(CostFunctionCrossValid);
beta=betaMatrix(1:index+1,index);
CostFunctionTest=sum((y-PolynomialData(:,1:index+1)*beta).^2);
end