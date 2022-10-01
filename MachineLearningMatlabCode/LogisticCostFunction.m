function cost = LogisticCostFunction(y,X,theta)
[m,n]=size(X);
cost=0;
for i=1:m
cost=cost+y(i,:)*(-log(HypothesisFunction(X(i,:),theta)))+(1-y(i,:))*(-log(1-HypothesisFunction(X(i,:),theta)));
end
return
end