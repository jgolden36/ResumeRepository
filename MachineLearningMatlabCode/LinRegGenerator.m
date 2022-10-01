function LinRegGenerator(n,p)
% n: Observations
% p = Variables
sigma = (p+1)/10;
%Generate random variables
X=[ones(n,1) randn(n,p)];
Theta=-1 + (2)*rand(p+1,1);
mat2str(size(Theta));
mat2str(size(X));
Epsilon=randn(n,1)*sigma;
Y=X*Theta+Epsilon;
%Generate OLS Estimate and Error
OLSEstimate=inv((X.'*X))*X.'*Y;
OLSPredictionsSSE=sum((X*OLSEstimate-Y).^2)
%Generate Gradient Descent Estimate and Error
Theta0GD=500;
Theta1GD=rand(p+1,1);
alpha=.00001;
while abs(sum(Theta1GD-Theta0GD)) >.0001 
    Theta0GD=Theta1GD;
    Theta1GD=Theta1GD-alpha*2*(X.'*X*Theta1GD-X.'*Y);
end
GDPredictionsSSE=sum((X*Theta1GD-Y).^2)
%Generate Newton's method Estimate and Error
Theta0NM=500;
Theta1NM=rand(p+1,1);
while abs(sum(Theta1NM-Theta0NM)) >.0001 
    Theta0NM=Theta1NM;
    Hessian=2*X.'*X;
    Theta1NM=Theta1NM-2*inv(Hessian)*(X.'*X*Theta1NM-X.'*Y);
end
NMPredictionsSSE=sum((X*Theta1NM-Y).^2)
end