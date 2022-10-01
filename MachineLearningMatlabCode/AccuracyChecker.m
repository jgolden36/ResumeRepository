function [ConfusionMatrix,precision,recall,F1,Accuracy] = AccuracyChecker(Predicted,Actual,PositiveClass)
[numRows,numCols] = size(Predicted);
TruePositive=0;
FalsePositive=0;
FalseNegative=0;
AccuracySum=0;
ConfusionMatrix=zeros(max(Actual));
for i=1:numRows
    ConfusionMatrix(Predicted(i,:),Actual(i,:))=ConfusionMatrix(Predicted(i,:),Actual(i,:))+1;
end
TruePositive=ConfusionMatrix(PositiveClass,PositiveClass);
FalsePositive=sum(ConfusionMatrix(PositiveClass,:),"all");
FalseNegative=sum(ConfusionMatrix(:,PositiveClass),"all");
for i=1:max(Actual)
    AccuracySum=AccuracySum+ConfusionMatrix(i,i);
end
precision=TruePositive/(TruePositive+FalsePositive);
recall=TruePositive/(TruePositive+FalseNegative);
Accuracy=AccuracySum/sum(ConfusionMatrix,'all');
F1=precision*recall/(precision+recall);
end