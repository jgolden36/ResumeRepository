cd 'C:\Users\bnhas\OneDrive\Desktop\Classes\Classes Spring 2023\Industrial Organization 2\Homework\Data';
T = readtable('PS2_Data.csv');
Xvars=T(:,3:end);
tireshops=T(:,2);
T=table2array(T);
CoefficientMatrix0=zeros(19,1);
NormalCostFunction=@NormalCostFunction;
CoefficientMatrix1=fminsearch(NormalCostFunction,CoefficientMatrix0);
CoefficientMatrix1(CoefficientMatrix1>1)=0;
CoefficientMatrix1(CoefficientMatrix1<-1)=0;
Xvars=table2array(Xvars);
TLessThan4=T(T(:,2)<4,:);
tireshops4=TLessThan4(:,2);
Xvars4=TLessThan4(:,3:end);
Yvars=size(tireshops4);
AverageTotalSize=zeros(Yvars(1),1);
%CoefficientMatrix1=[2.25 .34 .23 -.53 .86 -.49 -.02 -.03 .004 .86 .03 .15 .08 .53 .76 .46 .6 .12];
for j=1:Yvars
    Errors=normrnd(0,1,[1000,4]);
    AverageSizeVector=zeros(1000,1);
    for i=1:1000
        FirmCount=0;
        entry=1;
        Size=Xvars4(j,1)+CoefficientMatrix1(1)*Xvars4(j,2)+CoefficientMatrix1(2)*Xvars4(j,3)+CoefficientMatrix1(3)*Xvars4(j,4)+CoefficientMatrix1(4)*Xvars4(j,5);
        FixedCost=CoefficientMatrix1(14)+CoefficientMatrix1(15)*Xvars4(j,10);
        VariableProfit=CoefficientMatrix1(5)+CoefficientMatrix1(6)*Xvars4(j,7)+CoefficientMatrix1(7)*Xvars4(j,8)+CoefficientMatrix1(8)*Xvars4(j,9)+CoefficientMatrix1(9)*Xvars4(j,10);
        while entry==1 && FirmCount<4
            if FirmCount~=0
                FixeCost=FixedCost-CoefficientMatrix1(15+FirmCount);
                VariableProfit=VariableProfit-CoefficientMatrix1(9+FirmCount);
            end
            if -1*Size*VariableProfit+FixedCost<Errors(i,FirmCount+1)
                entry=0;
            else
                FirmCount=FirmCount+1;
            end
        end
        AverageSizeVector(i)=FirmCount;
    end
    AverageTotalSize(j)=mean(AverageSizeVector);
end
Yvars=size(tireshops4);
AverageTotalSizeInterDependent=zeros(Yvars(1),1);
Sigma = [1 .5 .5 .5; .5 1 .5 .5; .5 .5 1 .5; .5 .5 .5 1];
DecomposedSigma=chol(Sigma);
for j=1:Yvars
    ErrorsIndependent=normrnd(0,1,[1000,4]);
    ErrorsInterdependent=DecomposedSigma*ErrorsIndependent.';
    ErrorsInterdependent=ErrorsInterdependent.';
    AverageSizeVectorInterdependent=zeros(1000,1);
    for i=1:1000
        FirmCount=0;
        entry=1;
        Size=Xvars4(j,1)+CoefficientMatrix1(1)*Xvars4(j,2)+CoefficientMatrix1(2)*Xvars4(j,3)+CoefficientMatrix1(3)*Xvars4(j,4)+CoefficientMatrix1(4)*Xvars4(j,5);
        FixedCost=CoefficientMatrix1(14)+CoefficientMatrix1(15)*Xvars4(j,6);
        VariableProfit=CoefficientMatrix1(5)+CoefficientMatrix1(6)*Xvars4(j,7)+CoefficientMatrix1(7)*Xvars4(j,8)+CoefficientMatrix1(8)*Xvars4(j,9)+CoefficientMatrix1(9)*Xvars4(j,10);
        while entry==1 && FirmCount<4
            if FirmCount~=0
                FixeCost=FixedCost-CoefficientMatrix1(15+FirmCount);
                VariableProfit=VariableProfit-CoefficientMatrix1(9+FirmCount);
            end
            if -1*Size*VariableProfit+FixedCost<ErrorsInterdependent(i,FirmCount+1)
                entry=0;
            else
                FirmCount=FirmCount+1;
            end
        end
        AverageSizeVectorInterdependent(i)=FirmCount;
    end
    AverageTotalSizeInterDependent(j)=mean(AverageSizeVectorInterdependent);
end
