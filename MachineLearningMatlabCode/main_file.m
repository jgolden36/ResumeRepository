%%% Data Science, Problem Set 5 Solutions Dana Golden

clear all; close all; clc; 

%% Problem 1
load('datasetPS5.mat');
data=[x y];
[CostFunctionTrain,CostFunctionCrossValid,CostFunctionTest,beta]=PolynomialRegressions(data);

%A polynomial of the third degree minimizes the cost function on the
%cross-validation data. The beta value and cost on the test function are
%below:

beta

CostFunctionTest

%% Problem 2
[CostFunctionTrain,CostFunctionCrossValid,CostFunctionTest,beta,lambda] = PolynomialRegressionRegularized(data);
% The regularization parameter that minimized the cost function on the
% cross-validation data is reported below alsngside the cost function on
% the testing data and the discovered beta values.
lambda
CostFunctionTest
beta