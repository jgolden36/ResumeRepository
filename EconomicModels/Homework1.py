import numpy as np 
import pandas as pd
import os
import math
import statsmodels.api as sm
#from statsmodels.sandbox.regression.gmm import IV2SLS
from linearmodels.iv import IV2SLS
os.chdir("C:\\Users\\bnhas\\OneDrive\\Desktop\\Classes\\Classes Spring 2023\\Industrial Organization 2\\Homework\\Data")
df=pd.read_csv('PS1_Data.csv')
df=pd.get_dummies(df,columns=['sgmnt'],drop_first=True)
df=df.fillna(0)
originalData=df.to_numpy()
#originalData = np.loadtxt("PS1_Data.csv",delimiter=",", dtype=str)
originalData[:49,3]=originalData[:49,3]-float(originalData[50,3])
originalData=np.nan_to_num(originalData)
originalData[:,6]=originalData[:,6]*.01
originalData[:,7]=originalData[:,7]*.01
sigma=np.linalg.cholesky(np.identity(51))
predictedShare=np.zeros(51)
delta0=np.zeros(51)+.5
delta1=np.zeros(51)
while np.max(np.absolute(delta1-delta0))>10**(-1):
    print(np.max(np.absolute(delta1-delta0)))
    SharePrediction=np.zeros(51)
    delta0=delta1
    for j in range(0,51):
        RandomDrawMatrix=np.random.standard_normal(size=(10000,6))
        for r in range(0,10000):
            addedLogit=.0001*np.divide(np.exp((delta0[j]+np.sum(RandomDrawMatrix[r,1:]*originalData[j,7:])-RandomDrawMatrix[r,0]*originalData[j,3]).astype(np.float64)),(1+np.sum(np.exp((delta0+np.sum(RandomDrawMatrix[r,1:]*originalData[:,7:],axis=1)-RandomDrawMatrix[r,0]*originalData[:,3]).astype(np.float64)))))
            #while isinstance(addedLogit, np.floating)==True:
                #RandomDrawMatrix=np.random.standard_normal(size=(1000,6))
                #addedLogit=.001*np.exp(delta0[j]+np.sum(RandomDrawMatrix[r,1:]*originalData[j,7:])-RandomDrawMatrix[r,0]*originalData[j,3])/(1+np.sum(np.exp((delta0+np.sum(RandomDrawMatrix[r,1:]*originalData[:,7:],axis=1)-RandomDrawMatrix[r,0]*originalData[:,3]).astype(float))))
            SharePrediction[j]=SharePrediction[j]+addedLogit
    delta1=delta0+np.log(originalData[:,6].astype(float))-np.log(SharePrediction.astype(float))

originalData[:,7]=originalData[:,7]*100
originalDataConstant = sm.add_constant(originalData[:,7:])
OLSresults = sm.OLS(endog=delta1, exog=(np.column_stack((originalData[:,3],originalDataConstant))).astype(float)).fit()
print(OLSresults.summary().as_latex())
AverageCharacteristicsOtherBrands=(np.sum(originalData[:,7:],axis=0)-originalData[:,7:])/50
AverageCharacteristicsSameManufacturer=np.zeros((51,5))
AverageCharacteristicsRivals=np.zeros((51,5))
for j in range(0,50):
    AverageCharacteristicsSameManufacturer[j]=(np.sum(originalData[:,7:],axis=0)-np.sum(originalData[originalData[:,1]!=originalData[j,1]][:,7:],axis=0)-originalData[j,7:])/(np.shape(originalData[originalData[:,1]!=originalData[j,1]])[0]-1.0)
    AverageCharacteristicsRivals[j]=(np.sum(originalData[:,7:],axis=0)-np.sum(originalData[originalData[:,1]==originalData[j,1]][:,7:],axis=0))/np.shape(originalData[originalData[:,1]==originalData[j,1]][:,7:])[0]

AverageCharacteristicsSameManufacturer[50]=originalData[50,7:]
AverageCharacteristicsSameManufacturer=AverageCharacteristicsSameManufacturer.astype(float)
AverageCharacteristicsRivals[50]=(np.sum(originalData[:,7:],axis=0)-np.sum(originalData[originalData[:,2]==originalData[50,2]][:,7:],axis=0))/np.shape(originalData[originalData[:,2]==originalData[50,2]][:,7:])[0]
#TwoSLSresultsSameManufacturer=IV2SLS(endog=delta1,exog=originalData[:,3].astype(float),instrument=((np.column_stack((originalDataConstant,AverageCharacteristicsSameManufacturer))).astype(float))).fit()
#TwoSLSresultsRivals=IV2SLS(endog=delta1,exog=originalData[:,3].astype(float),instrument=((np.column_stack((originalDataConstant,AverageCharacteristicsRivals))).astype(float))).fit()
#TwoSLSresultsOtherBrands=IV2SLS(endog=delta1,exog=originalData[:,3].astype(float),instrument=((np.column_stack((originalDataConstant,AverageCharacteristicsOtherBrands))).astype(float))).fit()
#print(TwoSLSresultsSameManufacturer.summary().as_latex())
#print(TwoSLSresultsRivals.summary().as_latex())
#print(TwoSLSresultsOtherBrands.summary().as_latex())
TwoSLSresultsSameManufacturer=IV2SLS(delta1, exog=originalDataConstant.astype(float), endog=originalData[:,3].astype(float), instruments=AverageCharacteristicsSameManufacturer.astype(float)).fit()
TwoSLSresultsRivals=IV2SLS(delta1, exog=originalDataConstant.astype(float), endog=originalData[:,3].astype(float), instruments=AverageCharacteristicsRivals.astype(float)).fit()
TwoSLSresultsOtherBrands=IV2SLS(delta1, exog=originalDataConstant.astype(float),endog=originalData[:,3].astype(float), instruments=AverageCharacteristicsOtherBrands[:,4].astype(float)).fit()
print(TwoSLSresultsSameManufacturer.summary.as_latex())
print(TwoSLSresultsRivals.summary.as_latex())
print(TwoSLSresultsOtherBrands.summary.as_latex())
originalData[:49,3]=originalData[:49,3]+float(originalData[50,3])
MarginalCost=originalData[:,3]-(originalData[:,6]/.6197)
Markup=(originalData[:,3]-MarginalCost)/originalData[:,3]