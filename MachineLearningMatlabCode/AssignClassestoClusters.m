function classVector= AssignClassestoClusters(Predicted,Actual)
%This function takes the outputs of KMeans and assigns them to classes
%based on the actual data.
NumberofClasses=max(Actual);
[numRows,numCols] = size(Actual);
PredictionAccuracy=zeros(NumberofClasses,1);
CountValues=zeros(NumberofClasses,1);
[ConfusionMatrix,precision,recall,F1,Accuracy123] = AccuracyChecker(Predicted,Actual,1);
Predicted123=Predicted;
Mask1=Predicted==1;
Mask2=Predicted==2;
Mask3=Predicted==3;
Predicted(Mask1)=2;
Predicted(Mask2)=1;
Predicted213=Predicted;
Predicted(Mask2)=3;
Predicted(Mask3)=1;
Predicted231=Predicted;
Predicted(Mask2)=3;
Predicted(Mask3)=2;
Predicted(Mask1)=1;
Predicted132=Predicted;
Predicted(Mask1)=3;
Predicted(Mask2)=2;
Predicted(Mask3)=1;
Predicted321=Predicted;
Predicted(Mask1)=3;
Predicted(Mask3)=2;
Predicted(Mask2)=1;
Predicted312=Predicted;
[ConfusionMatrix,precision,recall,F1,Accuracy213] = AccuracyChecker(Predicted213,Actual,1);
[ConfusionMatrix,precision,recall,F1,Accuracy231] = AccuracyChecker(Predicted231,Actual,1);
[ConfusionMatrix,precision,recall,F1,Accuracy132] = AccuracyChecker(Predicted132,Actual,1);
[ConfusionMatrix,precision,recall,F1,Accuracy321] = AccuracyChecker(Predicted321,Actual,1);
[ConfusionMatrix,precision,recall,F1,Accuracy312] = AccuracyChecker(Predicted312,Actual,1);
if Accuracy123>Accuracy213 & Accuracy123>Accuracy231 & Accuracy123>Accuracy132 &Accuracy123>Accuracy321&Accuracy123>Accuracy312
    classVector=Predicted123;
    return
elseif Accuracy213>Accuracy231 & Accuracy213>Accuracy132 &Accuracy213>Accuracy321&Accuracy213>Accuracy312
    classVector=Predicted213;
    return
elseif Accuracy231>Accuracy132 &Accuracy231>Accuracy321&Accuracy231>Accuracy312
    classVector=Predicted231;
    return
elseif Accuracy132>Accuracy321&Accuracy132>Accuracy312
    classVector=Predicted132;
    return
elseif Accuracy321>Accuracy312
    classVector=Predicted321;
    return
else
    classVector=Predicted312;
    return
end