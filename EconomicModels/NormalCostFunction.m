function [LogLikelihoodNeg] = NormalCostFunction(x)
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
cd 'C:\Users\bnhas\OneDrive\Desktop\Classes\Classes Spring 2023\Industrial Organization 2\Homework\Data';
T = readtable('PS2_Data.csv');
Xvars=T(:,3:end);
Xvars=table2array(Xvars);
Yvar=T(:,2);
Yvar=table2array(Yvar);
Yvars=size(Yvar);
LogLikelihood=0;
for i=1:Yvars
    if Yvar(i,1)<5
        TaoThreshold=Yvar(i,1);
    else
        TaoThreshold=5;
    end
   Size=Xvars(i,1)+x(1)*Xvars(i,2)+x(2)*Xvars(i,3)+x(3)*Xvars(i,4)+x(4)*Xvars(i,5);
   if TaoThreshold==0
       FixedCost=x(14)+x(15)*Xvars(i,6);
       VariableProfit=x(5)+x(6)*Xvars(i,7)+x(7)*Xvars(i,8)+x(8)*Xvars(i,9)+x(9)*Xvars(i,10);
       TaoMinusProfit=VariableProfit*Size-FixedCost;
       NormalTaoMinusProfit=normcdf(TaoMinusProfit);
       LogLikelihood=LogLikelihood+log(1-NormalTaoMinusProfit);
   elseif TaoThreshold==1
       FixedCost=x(14)+x(15)*Xvars(i,6);
       VariableProfit=x(5)+x(6)*Xvars(i,7)+x(7)*Xvars(i,8)+x(8)*Xvars(i,9)+x(9)*Xvars(i,10);
       TaoMinusProfit=VariableProfit*Size-FixedCost;
       NormalTaoMinusProfit=normcdf(TaoMinusProfit);
       TaoMinusProfitBelow=(VariableProfit-x(10))*Size-(FixedCost-x(16));
       NormalTaoMinusProfitBelow=normcdf(TaoMinusProfitBelow);
       LogLikelihood=LogLikelihood+log(NormalTaoMinusProfit-NormalTaoMinusProfitBelow);
   elseif TaoThreshold==2
       FixedCost=x(14)+x(15)*Xvars(i,6)-x(16);
       VariableProfit=x(5)+x(6)*Xvars(i,7)+x(7)*Xvars(i,8)+x(8)*Xvars(i,9)+x(9)*Xvars(i,10)-x(10);
       TaoMinusProfit=VariableProfit*Size-FixedCost;
       NormalTaoMinusProfit=normcdf(TaoMinusProfit);
       TaoMinusProfitBelow=(VariableProfit-x(11))*Size-(FixedCost-x(17));
       NormalTaoMinusProfitBelow=normcdf(TaoMinusProfitBelow);
       LogLikelihood=LogLikelihood+log(NormalTaoMinusProfit-NormalTaoMinusProfitBelow);
   elseif TaoThreshold==3
       FixedCost=x(14)+x(15)*Xvars(i,6)-x(16)-x(17);
       VariableProfit=x(5)+x(6)*Xvars(i,7)+x(7)*Xvars(i,8)+x(8)*Xvars(i,9)+x(9)*Xvars(i,10)-x(10)-x(11);
       TaoMinusProfit=VariableProfit*Size-FixedCost;
       NormalTaoMinusProfit=normcdf(TaoMinusProfit);
       TaoMinusProfitBelow=(VariableProfit-x(12))*Size-(FixedCost-x(18));
       NormalTaoMinusProfitBelow=normcdf(TaoMinusProfitBelow);
       LogLikelihood=LogLikelihood+log(NormalTaoMinusProfit-NormalTaoMinusProfitBelow);
   elseif TaoThreshold==4
       FixedCost=x(14)+x(15)*Xvars(i,6)-x(16)-x(17)-x(18);
       VariableProfit=x(5)+x(6)*Xvars(i,7)+x(7)*Xvars(i,8)+x(8)*Xvars(i,9)+x(9)*Xvars(i,10)-x(10)-x(11)-x(12);
       TaoMinusProfit=VariableProfit*Size-FixedCost;
       NormalTaoMinusProfit=normcdf(TaoMinusProfit);
       TaoMinusProfitBelow=(VariableProfit-x(13))*Size-(FixedCost-x(19));
       NormalTaoMinusProfitBelow=normcdf(TaoMinusProfitBelow);
       LogLikelihood=LogLikelihood+log(NormalTaoMinusProfit-NormalTaoMinusProfitBelow);
   else
       VariableProfit=x(5)+x(6)*Xvars(i,7)+x(7)*Xvars(i,8)+x(8)*Xvars(i,9)+x(9)*Xvars(i,10)-x(10)-x(11)-x(12)-x(13);
       FixedCost=x(14)+x(15)*Xvars(i,6)-x(16)-x(17)-x(18)-x(19);
       TaoMinusProfit=VariableProfit*Size-FixedCost;
       NormalTaoMinusProfit=normcdf(TaoMinusProfit);
       LogLikelihood=LogLikelihood+log(NormalTaoMinusProfit);
   end
end
LogLikelihoodNeg=LogLikelihood*-1;
LogLikelihoodNeg
end