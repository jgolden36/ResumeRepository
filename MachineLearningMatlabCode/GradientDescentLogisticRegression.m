function theta1=GradientDescentLogisticRegression(y,X,alpha)
[m,n]=size(X);
ones=zeros(m,1)+1;
X=[ones X];
theta0=zeros(n+1,1)+1;
CostFunction=LogisticCostFunction(y,X,theta0);
theta1=zeros(n+1,1)+100;
while sum(abs(theta0-theta1))>.00001
    theta1=theta0;
        for j=1:n+1
            Sum1=0;
            for i=1:m
                Sum1=Sum1+sum((HypothesisFunction(X(i,:),theta0)-y(i,:))*X(i,j));
            end
        theta0(j)=theta0(j)-alpha*(1/m)*Sum1;
        end
    CostFunction=LogisticCostFunction(y,X,theta0);
end
end