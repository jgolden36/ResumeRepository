function cost = LogisticCostFunctioninTermsofTheta(theta)
y=[0;0;0;0;0;1;0;1;0;1;0;1;1;1;1;1;1;1;1;1];
X=[.5;.75;1;1.25;1.5;1.75;2;2.25;2.5;2.75;3;3.25;3.5;3.75;4;4.25;4.5;4.75;5;5.5];
[m,n]=size(X);
ones=zeros(m,1)+1;
X=[ones X];
cost=0;
for i=1:m
cost=cost+y(i,:)*(-log(HypothesisFunction(X(i,:),theta)))+(1-y(i,:))*(-log(1-HypothesisFunction(X(i,:),theta)));
end
cost=cost(:,1);
return
end