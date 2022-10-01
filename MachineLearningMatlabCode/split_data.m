function [training_data,testing_data,crossValidation_data] = split_data(data)
[row column] = size(data);
TestingSize=floor(.2*row);
CrossValidationSize=floor(.2*row);
TrainingSize=ceil(.6*row);
ShuffledData=data(randperm(size(data, 1)), :);
training_data=ShuffledData(1:TrainingSize,:);
crossValidation_data=ShuffledData(TrainingSize+1:TrainingSize+CrossValidationSize,:);
testing_data=ShuffledData(TrainingSize+CrossValidationSize+1:end,:);
end