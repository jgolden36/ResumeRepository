import numpy as np                                                                                                                                           
                                                                                                                                         
                                                                                                                                         
class QLearner(object):                                                                                                                                          
    """                                                                                                                                          
    This is a Q learner object.                                                                                                                                          
                                                                                                                                         
    :param num_states: The number of states to consider.                                                                                                                                         
    :type num_states: int                                                                                                                                        
    :param num_actions: The number of actions available..                                                                                                                                        
    :type num_actions: int                                                                                                                                           
    :param alpha: The learning rate used in the update rule. Should range between 0.0 and 1.0 with 0.2 as a typical value.                                                                                                                                           
    :type alpha: float                                                                                                                                           
    :param gamma: The discount rate used in the update rule. Should range between 0.0 and 1.0 with 0.9 as a typical value.                                                                                                                                           
    :type gamma: float                                                                                                                                           
    :param rar: Random action rate: the probability of selecting a random action at each step. Should range between 0.0 (no random actions) to 1.0 (always random action) with 0.5 as a typical value.                                                                                                                                           
    :type rar: float                                                                                                                                         
    :param radr: Random action decay rate, after each update, rar = rar * radr. Ranges between 0.0 (immediate decay to 0) and 1.0 (no decay). Typically 0.99.                                                                                                                                        
    :type radr: float                                                                                                                                        
    :param dyna: The number of dyna updates for each regular update. When Dyna is used, 200 is a typical value.                                                                                                                                          
    :type dyna: int                                                                                                                                          
    :param verbose: If “verbose” is True, your code can print out information for debugging.                                                                                                                                         
    :type verbose: bool                                                                                                                                          
    """                                                                                                                                          
    def __init__(                                                                                                                                        
        self,                                                                                                                                        
        num_states=100,                                                                                                                                          
        num_actions=100,                                                                                                                                           
        alpha=0.1,                                                                                                                                           
        gamma=0.95,                                                                                                                                           
        rar=0.5,                                                                                                                                         
        radr=.9,                                                                                                                                           
        dyna=0,                                                                                                                                          
        verbose=False,                                                                                                                                           
    ):                                                                                                                                           
        """                                                                                                                                          
        Constructor method                                                                                                                                           
        """                                                                                                                                          
        self.verbose = verbose                                                                                                                                           
        self.num_actions = num_actions  
        self.Q=np.zeros((num_states,num_actions))                                                                                                                                         
        self.s = 0                                                                                                                                           
        self.a = 0 
        self.gamma=gamma
        self.rar=rar 
        self.radr=radr
        self.dyna=dyna
        self.alpha=alpha 
        self.priorExperiences=[]                                                                                                                                      
                                                                                                                                         
    def querysetstate(self, s):                                                                                                                                          
        """                                                                                                                                          
        Update the state without updating the Q-table                                                                                                                                        
                                                                                                                                         
        :param s: The new state                                                                                                                                          
        :type s: int                                                                                                                                         
        :return: The selected action                                                                                                                                         
        :rtype: int                                                                                                                                          
        """                                                                                                                                          
        self.s = s
        GreedyDecision=np.random.random()
        if GreedyDecision<=self.rar:                                                                                                                                    
            action = np.random.randint(0, self.num_actions - 1)
        else:
            action=np.argmax(self.Q[s])
        self.a=action                                                                                                                                                                                                                                                                         
        return action                                                                                                                                        
                                                                                                                                         
    def query(self, s_prime, r):                                                                                                                                         
        """                                                                                                                                          
        Update the Q table and return an action                                                                                                                                          
                                                                                                                                         
        :param s_prime: The new state                                                                                                                                        
        :type s_prime: int                                                                                                                                           
        :param r: The immediate reward                                                                                                                                           
        :type r: float                                                                                                                                           
        :return: The selected action                                                                                                                                         
        :rtype: int                                                                                                                                          
        """    
        GreedyDecision=np.random.random()  
        self.priorExperiences.append((self.s, self.a, s_prime, r))
        if self.dyna>0:
            self.Dyna()  
        if GreedyDecision<=self.rar:                                                                                                                                  
            action = np.random.randint(0, self.num_actions - 1)
        else:
            action=np.argmax(self.Q[s_prime])
        if self.verbose:                                                                                                                                         
            print(f"s = {s_prime}, a = {action}, r={r}")  
        self.Q[self.s,self.a]=self.Q[self.s,self.a]+self.alpha*(r+self.gamma*self.Q[s_prime,action]-self.Q[self.s,self.a])   
        self.s=s_prime
        self.a=action
        self.rar=self.rar*self.radr 
        return action
    def author(self):
        return 'jgolden36'
    def Dyna(self):
        for i in range(self.dyna):
            r=np.random.randint(0,len(self.priorExperiences))-1
            HallucinatedExperience=self.priorExperiences[r]
            self.Q[HallucinatedExperience[0],HallucinatedExperience[1]]=self.Q[HallucinatedExperience[0],HallucinatedExperience[1]]+self.alpha*(HallucinatedExperience[3]+self.gamma*self.Q[HallucinatedExperience[2],np.argmax(self.Q[HallucinatedExperience[2]])]-self.Q[HallucinatedExperience[0],HallucinatedExperience[1]])

n=2
mu=.3
alpha=np.linspace(3,5,n)
alpha0=1.0
MarginalCostDict=np.random.uniform(size=n)
beta=.99
PriceGridSize=50
AgentDictionary={}
ProfitDictionary={}
DemandDictionary={}
PriceGrid=np.linspace(0,3,PriceGridSize)
#RegulationGrid=np.linspace(0,3,int(float(PriceGridSize)/2))
for i in range(n):
    AgentDictionary[i] = QLearner(num_states=PriceGridSize**(n)*50,num_actions=PriceGridSize)

#RegulatoryAgent=QLearner(num_states=1+PriceGridSize**(n+1)*10,num_actions=PriceGridSize+1)
ActionDictionary={}
PriceDictionary={}
for i in range(n):
    ActionDictionary[i]=AgentDictionary[i].querysetstate(0)
    PriceDictionary[i]=PriceGrid[ActionDictionary[i]]

#RegulationAction=RegulatoryAgent.querysetstate(1)
#if RegulationAction==0:
    #Regulation=0
#else:
    #if RegulationAction<26:
        #Regulation=RegulationGrid[RegulationAction-1]
    #else:
        #Regulation=RegulationGrid[RegulationAction-26]

socialWelfare=0
logitsum=0
for i in range(n):
    #if (RegulationAction>0 and RegulationAction<25 and PriceDictionary[i]<Regulation) or (RegulationAction>25 and PriceDictionary[i]>Regulation):
        #PriceDictionary[i]=Regulation
    logitsum=(logitsum+alpha[i]-PriceDictionary[i])

for i in range(n):
    DemandDictionary[i]=np.exp(alpha[i]-PriceDictionary[i])/(logitsum+alpha0/mu)
    ProfitDictionary[i]=PriceDictionary[i]*DemandDictionary[i]-MarginalCostDict[i]*DemandDictionary[i]
    socialWelfare=socialWelfare+ProfitDictionary[i]+mu*(np.exp(alpha0))*np.log((np.exp(.5*(logitsum+PriceDictionary[i]-alpha[i])/mu)+np.exp(alpha[i]/mu))*np.exp(PriceDictionary[i]/mu)+np.exp(alpha0/mu))/(np.exp(.5*(logitsum+PriceDictionary[i]-alpha[i])/mu)+np.exp(alpha0/mu))

#if RegulationAction<10:
        #Action='0'+str(RegulationAction)
#elif RegulationAction<100:
    #Action='0'+str(RegulationAction)

newState=''+str(Action)
for i in range(n):
    if ActionDictionary[i]<10:
        Action='0'+str(ActionDictionary[i])
    #elif ActionDictionary[i]<100:
     #   Action='0'+str(ActionDictionary[i])
    newState=newState+str(Action)

newState=int(newState)

socialWelfareOverTime1=[]
PricesOverTime3=[]
PricesOverTime4=[]
for j in range(100000):
    socialWelfareOverTime1.append(socialWelfare)
    PricesOverTime3.append(PriceDictionary[0])
    PricesOverTime4.append(PriceDictionary[1])
    MarginalCostDict=np.random.uniform(size=n)
    for i in range(n):
        ActionDictionary[i]=AgentDictionary[i].query(newState,ProfitDictionary[i])
        PriceDictionary[i]=PriceGrid[ActionDictionary[i]]
    #RegulationAction=RegulatoryAgent.query(newState,socialWelfare)
    socialWelfare=0
    #if RegulationAction<10:
    #        Action='0'+str(RegulationAction)
    #elif RegulationAction<100:
        #Action='0'+str(RegulationAction)
    newstate=''+str(Action)
    for i in range(n):
        if ActionDictionary[i]<10:
            Action='0'+str(ActionDictionary[i])
        #elif ActionDictionary[i]<100:
            #Action='0'+str(ActionDictionary[i])
        newstate=newstate+str(Action)
    newstate=int(newstate)
    #if RegulationAction==0:
     #   Regulation=0
    #else:
     #   if RegulationAction<26:
      #      Regulation=RegulationGrid[RegulationAction-1]
       # else:
        #    Regulation=RegulationGrid[RegulationAction-26]
    socialWelfare=0
    logitsum=0
    for i in range(n):
        #if (RegulationAction>0 and RegulationAction<25 and PriceDictionary[i]<Regulation) or (RegulationAction>25 and PriceDictionary[i]>Regulation):
        #    PriceDictionary[i]=Regulation
        logitsum=(logitsum+alpha[i]-PriceDictionary[i])
    for i in range(n):
        DemandDictionary[i]=np.exp(alpha[i]-PriceDictionary[i])/(logitsum+alpha0/mu)
        ProfitDictionary[i]=PriceDictionary[i]*DemandDictionary[i]-MarginalCostDict[i]*DemandDictionary[i]
        socialWelfare=socialWelfare+(ProfitDictionary[i]+mu*(np.exp(alpha0))*np.log((np.exp(.5*(logitsum+PriceDictionary[i]-alpha[i])/mu)+np.exp(alpha[i]/mu))*np.exp(PriceDictionary[i]/mu)+np.exp(alpha0/mu))/(np.exp(.5*(logitsum+PriceDictionary[i]-alpha[i])/mu)+np.exp(alpha0/mu)))

import matplotlib.pyplot as plt
T=np.linspace(1,100,100)
plt.plot(T,socialWelfareOverTime[9900:10000],label='With Regulator')
plt.plot(T,socialWelfareOverTime1[9900:10000],label='Without Regulator')
plt.plot()
plt.ylabel('social Welfare')
plt.xlabel('Period')
plt.legend()
plt.show()
plt.plot(T,PricesOverTime1[9900:10000],label='Price 1 With Regulator')
plt.plot(T,PricesOverTime3[9900:10000],label='Price 1 Without Regulator')
plt.plot()
plt.ylabel('Prices')
plt.xlabel('Period')
plt.legend()
plt.show()
#plt.plot(T,PricesOverTime1[9900:10000],label='Price 1 With Regulator')
plt.plot(T,PricesOverTime2[9900:10000],label='Price 2 With Regulator')
#plt.plot(T,PricesOverTime3[9900:10000],label='Price 1 Without Regulator')
plt.plot(T,PricesOverTime4[9900:10000],label='Price 2 Without Regulator')
plt.plot()
plt.ylabel('Prices')
plt.xlabel('Period')
plt.legend()
plt.show()
print((sum(socialWelfareOverTime)-sum(socialWelfareOverTime1))/sum(socialWelfareOverTime1))
print((sum(PricesOverTime1)-sum(PricesOverTime3))/sum(PricesOverTime3))
print((sum(PricesOverTime2)-sum(PricesOverTime4))/sum(PricesOverTime4))