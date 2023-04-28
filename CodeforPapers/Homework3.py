import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
os.chdir('C:\\Users\\bnhas\\OneDrive\\Desktop\\Classes\\Classes Spring 2023\\Industrial Organization 2\\Homework\\Data')
def ValueIteration(RC=11.7257,theta11=2.4569,theta31=.4475,theta32=.4459,theta34=.1064,beta=.9999,ProbabilityReplacement=.18):
    LL=-3393.991
    epsilon=.0001
    N=100
    MaxMilage=345000
    ValueFunction1=np.zeros((100,2))
    ValueFunction0=np.ones((100,2))
    #ProbabilityReplacement=1-.82
    Grid=np.linspace(0,MaxMilage,N)
    diff=np.ndarray.max(np.absolute(ValueFunction1-ValueFunction0))
    while diff>epsilon:
        ValueFunction1=ValueFunction0
        V0=ValueFunction0
        for i in range(N):
            Value=.5772156+np.log(np.abs(np.sum(V0,axis=0)))
            expectedValueFunction=np.hstack((Value[0]*ProbabilityReplacement,Value[1]*(1-ProbabilityReplacement)))
            Utility0=-1*theta11*Grid[i]
            Utility1=-1*RC-Grid[i]
            ValueFunction0[i,0]=Utility0+beta*np.asarray(expectedValueFunction[0])
            ValueFunction0[i,1]=Utility1+beta*np.asarray(expectedValueFunction[1])
        diff=np.ndarray.max(np.absolute(ValueFunction1-ValueFunction0))
    return ValueFunction1

ValueFunction=ValueIteration()

plt.plot(np.linspace(0,345000,100), ValueFunction[:,0], label='Keep Value Function')
plt.plot(np.linspace(0,345000,100), ValueFunction[:,1], label='Replace Value Function')
plt.xlabel("Mileage")
plt.ylabel("Value Function")
plt.title("Value Function Keep and Replace")
plt.show()

buses=100
weeks=100


def SimulateHZ(valueFunction,buses,weeks,beta=.9999):
    theta11=2.4569
    theta31=.4475
    theta32=.4459
    theta34=.1064
    RC=11.7257
    import scipy.stats as stats
    lower, upper = 0, 15000
    mu, sigma = 6000, 4000
    mileage_dist = stats.truncnorm((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
    xVector=np.zeros((buses,weeks))
    MaxMilage=345000
    Grid=np.linspace(0,MaxMilage,buses)
    iVector=np.zeros((buses,weeks))
    EpsilonUniform=np.random.uniform(low=0.0, high=1.0, size=(2*buses,weeks))
    EpsilonVector=-1*np.log(-1*np.log(EpsilonUniform))+.577
    Value1=np.zeros((buses,weeks))
    Value0=np.zeros((buses,weeks))
    for i in range(buses):
        for t in range(weeks):
            Utility0=-1*theta11*xVector[i,t]
            Utility1=-1*RC
            State=np.floor(np.divide(xVector,345000/100)).astype(int)
            State[State>99]=99
            Value1[i,t]=(Utility1+EpsilonUniform[i,t]+valueFunction[State][1])[0][1]
            Value0[i,t]=(Utility0+EpsilonUniform[i+buses,t]+valueFunction[State][1])[0][0]
            if Value1[i,t]>Value0[i,t]:
                iVector[i,t]=1
                xVector[i,t+1]=0
            else:
                iVector[i,t]=0
                TransitionValue=np.random.uniform(0,1)
                k=False
                while k!=True:
                    TransitionDraw=mileage_dist.rvs()
                    if TransitionValue<theta31 and TransitionDraw<5000:
                        k=True 
                    elif TransitionValue<(theta31+theta32) and TransitionDraw>5000 and TransitionValue<10000:
                        k=True 
                    elif TransitionValue>(theta31+theta32) and TransitionDraw>10000:
                        k=True 
                    else:
                        k=False
                print(TransitionDraw)
                if t<98:
                    xVector[i,t+1]=xVector[i,t]+TransitionDraw
    return (xVector,iVector)

xVec,IVec=SimulateHZ(ValueFunction,buses,weeks,beta=.9999)
df_xVec= pd.DataFrame(xVec)
df_IVec= pd.DataFrame(IVec)
print(df_xVec.describe)
print(df_IVec.describe)
print(sum(sum(IVec)/(100*100)))
print(sum(sum(xVec)/(100*100)))

#def EstimateModelNFP(data,alpha):
#   ReplacementDecisions=data
#   Mileage=data
#   while np.maximum(np.absolute(theta1-theta0))>.001&np.maximum(np.absolute(beta1-beta0))>.001:
#       theta1=theta0
#       beta1=beta0
#       for i in range(np.shape(data)[0]):
#           for j in range(np.shape(data)[1]):
#               logLikelihood=ReplacementDecisions[i,j]*np.log(ProbabilityReplacement(Mileage[i,j]))+(1-ReplacementDecisions[i,j])*np.log(ProbabilityReplacement(Mileage[i,j]))
#               GradientTheta=GradientTheta+Gradient(Mileage,ReplacementDecisions,theta0,Beta0)
#               GradientBeta=GradientBeta+Gradient(Mileage,ReplacementDecisions,theta0,Beta1)
#
#       theta0(j)=theta0(j)-alpha*(1.0/(np.shape(data)[0]+np.shape(data)[1]))*GradientTheta
#       beta0(j)=beta0(j)-alpha*(1.0/(np.shape(data)[0]+np.shape(data)[1]))*GradientTheta
#   return (beta1,theta1,logLikelihood)
dataDF=pd.read_csv('bus1234.csv')
Investment=dataDF['replace']
State=dataDF['miles']
State=State.to_numpy()
Investment=Investment.to_numpy()
def LogLikelihood(theta,InvestmentData,StateData):
    RC=theta[0]
    theta11=theta[1]
    beta=theta[2]
    state=np.floor(np.divide(State,345000/100)).astype(int)
    state[state>99]=99
    ProbabilityReplacement=theta[3]
    theta31=theta[4]
    theta32=theta[5]
    theta33=theta[6]
    Vbar = ValueIteration(RC,theta11,theta31,theta32,theta33,beta,ProbabilityReplacement)
    EP = np.divide(np.exp(.001*Vbar[:,1]),(np.exp(.001*Vbar[:,0]) + np.exp(.001*Vbar[:,1])))
    logL = sum(np.log(EP[state[InvestmentData==1]])) + sum(np.log(1 - EP[state[InvestmentData==0]]))
    return -1*logL

def LogLikelihoodHM(theta,InvestmentData,StateData,CCP,TransitionMatrix):
    RC=theta[0]
    theta11=theta[1]
    beta=theta[2]
    State=np.floor(np.divide(StateData,345000/100)).astype(int)
    Utility=ComputeUtility(theta11,RC)
    EV= HMinversion(CCP, TransitionMatrix, Utility, beta)
    EP= EPCalculator(EV,TransitionMatrix,Utility,beta)
    logL = sum(np.log(EP[state[InvestmentData==1]])) + sum(np.log(1 - EP[state[InvestmentData==0]]))
    return -1*LogL

thetaZero=[1,1,1,1,1,1,1]
from scipy.optimize import minimize
FinalTheta=minimize(LogLikelihood, thetaZero,args=(Investment,State), method='nelder-mead')
print(FinalTheta.x)
def CCP(Investment,State):
    State=np.floor(np.divide(State,345000/100)).astype(int)
    StateDF=pd.DataFrame(np.transpose(np.array([Investment,State])),columns=['Investment', 'State'])
    P=StateDF.groupby('State')['Investment'].mean()
    P=P.values
    x=1-P
    print(x)
    x=x.reshape(len(x),1)
    P=P.reshape(len(P),1)
    CCP=np.concatenate((x,P),axis=1)
    print(CCP)
    return CCP

def HMinversion(CCP,TransitionMatrix,Utility,beta):
    leftSide=np.ones((100,100,2)) - beta*(np.multiply(CCP[:,0],TransitionMatrix[:,:,1]) + np.multiply(CCP[:,1],TransitionMatrix[:,:,1]))
    rightSide =.577+ sum(np.multiply(CCP,(Utility-np.log(CCP))),axis=1)
    HMInversion=np.linalg.inverse(leftSide*rightSide)
    return HMInversion

def EPCalculator(EV,TransitionMatrix,Utility,beta):
    E = np.exp(Utility+ beta*np.hstack(((TransitionMatrix[:,:,1]*EV),(TransitionMatrix[:,:,2] *EV)) ))
    EP= E[:,2]/sum(E,axis=1)
    return EP

def ComputeUtility(theta11,RC):
    MaxMilage=345000
    Grid=np.linspace(0,MaxMilage,100)
    Utility0=-1*theta11*Grid
    Utility1=-1*RC-Grid
    Utility=np.hstack((Utility0,Utility1))
    return Utility

def ComputeTransitionMatrix(n=100,ProbabilityReplacement=.18):
    TransitionMat=np.zeros((n,n,2))
    TransitionMat[n-1,n-1,1] = 1
    for i in range(n-1):
        TransitionMat[i,i,0]=1-ProbabilityReplacement
        TransitionMat[i,i+1,0]=ProbabilityReplacement
    TransitionMat[:,1,1]=1-ProbabilityReplacement
    TransitionMat[:,2,1]=ProbabilityReplacement
    return TransitionMat

def ComputeHotzMiller(InvestmentData,StateData):
    thetaZero=[0,0,0,0,0,0,0]
    TransitionMatrix=ComputeTransitionMatrix(n=100,ProbabilityReplacement=.18)
    CCP1=CCP(InvestmentData,StateData)
    ThetaHotzMiller=minimize(LogLikelihoodHM, thetaZero,args=(InvestmentData,StateData,CCP1,TransitionMatrix), method='nelder-mead')
    return ThetaHotzMiller

ThetaHotz=ComputeHotzMiller(Investment,State)

print(ThetaHotz.x)