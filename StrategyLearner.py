""""""                                                                                                                                           
"""                                                                                                                                          
Template for implementing StrategyLearner  (c) 2016 Tucker Balch                                                                                                                                         
                                                                                                                                         
Copyright 2018, Georgia Institute of Technology (Georgia Tech)                                                                                                                                           
Atlanta, Georgia 30332                                                                                                                                           
All Rights Reserved                                                                                                                                          
                                                                                                                                         
Template code for CS 4646/7646                                                                                                                                           
                                                                                                                                         
Georgia Tech asserts copyright ownership of this template and all derivative                                                                                                                                         
works, including solutions to the projects assigned in this course. Students                                                                                                                                         
and other users of this template code are advised not to share it with others                                                                                                                                        
or to make it available on publicly viewable websites including repositories                                                                                                                                         
such as github and gitlab.  This copyright statement should not be removed                                                                                                                                           
or edited.                                                                                                                                           
                                                                                                                                         
We do grant permission to share solutions privately with non-students such                                                                                                                                           
as potential employers. However, sharing with other current or future                                                                                                                                        
students of CS 7646 is prohibited and subject to being investigated as a                                                                                                                                         
GT honor code violation.                                                                                                                                         
                                                                                                                                         
-----do not edit anything above this line---                                                                                                                                         
                                                                                                                                         
Student Name: Dana Annalise Golden (replace with your name)                                                                                                                                          
GT User ID: jgolden36 (replace with your User ID)                                                                                                                                         
GT ID: 903190767 (replace with your GT ID)                                                                                                                                           
"""                                                                                                                                          
                                                                                                                                         
import datetime as dt                                                                                                                                        
import random                                                                                                                                        
                                                                                                                                         
import pandas as pd                                                                                                                                          
import util as ut
import QLearner as QL
import marketsimcode as MSC
import indicators as indic                                                                                                                                          
                                                                                                                                         
QlearnerTrader=QL.QLearner(num_states=3000,num_actions=3,alpha=0.9,gamma=.9,rar=0.6,radr=0.7,dyna=200,verbose=False)                                                                                                                                         
class StrategyLearner(object):                                                                                                                                           
    """                                                                                                                                          
    A strategy learner that can learn a trading policy using the same indicators used in ManualStrategy.                                                                                                                                         
                                                                                                                                         
    :param verbose: If “verbose” is True, your code can print out information for debugging.                                                                                                                                         
        If verbose = False your code should not generate ANY output.                                                                                                                                         
    :type verbose: bool                                                                                                                                          
    :param impact: The market impact of each transaction, defaults to 0.0                                                                                                                                        
    :type impact: float                                                                                                                                          
    :param commission: The commission amount charged, defaults to 0.0                                                                                                                                        
    :type commission: float                                                                                                                                          
    """                                                                                                                                          
    # constructor                                                                                                                                        
    def __init__(self, verbose=False, impact=0.0, commission=0.0):                                                                                                                                           
        """                                                                                                                                          
        Constructor method                                                                                                                                           
        """                                                                                                                                          
        self.verbose = verbose                                                                                                                                           
        self.impact = impact                                                                                                                                         
        self.commission = commission                                                                                                                                         
                                                                                                                                         
    # this method should create a QLearner, and train it for trading                                                                                                                                         
    def add_evidence(                                                                                                                                        
        self,                                                                                                                                        
        symbol="IBM",                                                                                                                                        
        sd=dt.datetime(2008, 1, 1),                                                                                                                                          
        ed=dt.datetime(2009, 1, 1),                                                                                                                                          
        sv=10000):                                                                                                                                           
        """                                                                                                                                          
        Trains your strategy learner over a given time frame.                                                                                                                                        
                                                                                                                                         
        :param symbol: The stock symbol to train on                                                                                                                                          
        :type symbol: str                                                                                                                                        
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008                                                                                                                                        
        :type sd: datetime                                                                                                                                           
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009                                                                                                                                          
        :type ed: datetime                                                                                                                                           
        :param sv: The starting value of the portfolio                                                                                                                                           
        :type sv: int                                                                                                                                        
        """                                                                                                                                          
                                                                                                                                         
        # add your code to do learning here                                                                                                                                          
                                                                                                                                         
        # example usage of the old backward compatible util function                                                                                                                                         
        syms = [symbol]                                                                                                                                          
        dates = pd.date_range(sd, ed)                                                                                                                                        
        prices_all = ut.get_data(syms, dates)  # automatically adds SPY                                                                                                                                          
        prices = prices_all[syms]  # only portfolio symbols                                                                                                                                          
        prices_SPY = prices_all["SPY"]  # only SPY, for comparison later                                                                                                                                         
        if self.verbose:                                                                                                                                         
            print(prices)
        indicatorClass=indic.Indicator([symbol],sd,ed)
        BollingerValues=indicatorClass.BollingerBands()
        MACDValues=indicatorClass.MACD()
        CCIValues=indicatorClass.CCI()
        StateList=[]
        for index in prices.index:
            try:
                if BollingerValues[index]<-2:
                    BV=0
                elif BollingerValues[index]>-2 and BollingerValues[index]<-1.5:
                    BV=1
                elif BollingerValues[index]>-1.5 and BollingerValues[index]<-1:
                    BV=2
                elif BollingerValues[index]>-1 and BollingerValues[index]<-.5:
                    BV=3
                elif BollingerValues[index]>-.5 and BollingerValues[index]<0:
                    BV=4
                elif BollingerValues[index]>0 and BollingerValues[index]<.5:
                    BV=5
                elif BollingerValues[index]>.5 and BollingerValues[index]<1:
                    BV=6
                elif BollingerValues[index]>1 and BollingerValues[index]<1.5:
                    BV=7
                elif BollingerValues[index]>1.5 and BollingerValues[index]<2:
                    BV=8
                elif BollingerValues[index]>2:
                    BV=9
                if MACDValues[0][index]<-2:
                    MAD=0
                elif MACDValues[0][index]>-2 and MACDValues[0][index]<-1.5:
                    MAD=1
                elif MACDValues[0][index]>-1.5 and MACDValues[0][index]<-1:
                    MAD=2
                elif MACDValues[0][index]>-1 and MACDValues[0][index]<-.5:
                    MAD=3
                elif MACDValues[0][index]>-.5 and MACDValues[0][index]<0:
                    MAD=4
                elif MACDValues[0][index]>0 and MACDValues[0][index]<.5:
                    MAD=5
                elif MACDValues[0][index]>.5 and MACDValues[0][index]<1:
                    MAD=6
                elif MACDValues[0][index]>1 and MACDValues[0][index]<1.5:
                    MAD=7
                elif MACDValues[0][index]>1.5 and MACDValues[0][index]<2:
                    MAD=8
                elif MACDValues[0][index]>2:
                    MAD=9
                if CCIValues[index]<-400:
                    CC=0
                elif CCIValues[index]>-400 and CCIValues[index]<-300:
                    CC=1
                elif CCIValues[index]>-300 and CCIValues[index]<-200:
                    CC=2
                elif CCIValues[index]>-200 and CCIValues[index]<-100:
                    CC=3
                elif CCIValues[index]>-100 and CCIValues[index]<0:
                    CC=4
                elif CCIValues[index]>0 and CCIValues[index]<100:
                    CC=5
                elif CCIValues[index]>100 and CCIValues[index]<200:
                    CC=6
                elif CCIValues[index]>200 and CCIValues[index]<300:
                    CC=7
                elif CCIValues[index]>300 and CCIValues[index]<400:
                    CC=8
                elif CCIValues[index]>400:
                    CC=9
                StateList.append(str(BV)+str(MAD)+str(CC))
            except KeyError:
                StateList.append(000)
        cash=sv
        TotalValue=cash
        stockHoldings=0
        HoldingValue=0
        NextState=str(HoldingValue)+str(StateList[0])
        for k in range(30):
            j=0
            for i in prices.index:
                TotalValue=cash+prices[symbol][i]*stockHoldings
                NextAction=QlearnerTrader.query(int(NextState), TotalValue)
                if NextAction==2 and stockHoldings!=1000:
                    cash=cash+(stockHoldings-1000)*prices[symbol][i]+self.impact*(stockHoldings-1000)*prices[symbol][i]-self.commission
                    stockHoldings=1000
                    HoldingValue=1
                elif NextAction==0 and stockHoldings!=-1000:
                    cash=cash+(stockHoldings+1000)*prices[symbol][i]-self.impact*(stockHoldings+1000)*prices[symbol][i]-self.commission
                    stockHoldings=-1000
                    HoldingValue=2
                NextState=str(HoldingValue)+str(StateList[j])
                j=j+1                                                                                                                     
        # example use with new colname                                                                                                                                           
        volume_all = ut.get_data(                                                                                                                                        
            syms, dates, colname="Volume"                                                                                                                                        
        )  # automatically adds SPY                                                                                                                                          
        volume = volume_all[syms]  # only portfolio symbols                                                                                                                                          
        volume_SPY = volume_all["SPY"]  # only SPY, for comparison later                                                                                                                                         
        if self.verbose:                                                                                                                                         
            print(volume)                                                                                                                                        
                                                                                                                                         
    # this method should use the existing policy and test it against new data                                                                                                                                        
    def testPolicy(                                                                                                                                          
        self,                                                                                                                                        
        symbol="IBM",                                                                                                                                        
        sd=dt.datetime(2009, 1, 1),                                                                                                                                          
        ed=dt.datetime(2010, 1, 1),                                                                                                                                          
        sv=10000):                                                                                                                                           
        """                                                                                                                                          
        Tests your learner using data outside of the training data                                                                                                                                           
                                                                                                                                         
        :param symbol: The stock symbol that you trained on on                                                                                                                                           
        :type symbol: str                                                                                                                                        
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008                                                                                                                                        
        :type sd: datetime                                                                                                                                           
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009                                                                                                                                          
        :type ed: datetime                                                                                                                                           
        :param sv: The starting value of the portfolio                                                                                                                                           
        :type sv: int                                                                                                                                        
        :return: A DataFrame with values representing trades for each day. Legal values are +1000.0 indicating                                                                                                                                           
            a BUY of 1000 shares, -1000.0 indicating a SELL of 1000 shares, and 0.0 indicating NOTHING.                                                                                                                                          
            Values of +2000 and -2000 for trades are also legal when switching from long to short or short to                                                                                                                                        
            long so long as net holdings are constrained to -1000, 0, and 1000.                                                                                                                                          
        :rtype: pandas.DataFrame                                                                                                                                         
        """                                                                                                                                          
                                                                                                                                         
        # here we build a fake set of trades                                                                                                                                         
        # your code should return the same sort of data 
        dates = pd.date_range(sd, ed)                                                                                                                                        
        prices_all = ut.get_data([symbol], dates)  # automatically adds SPY                                                                                                                                          
        trades = prices_all[[symbol,]]  # only portfolio symbols                                                                                                                                         
        trades_SPY = prices_all["SPY"]  # only SPY, for comparison later                                                                                                                                         
        trades.values[:, :] = 0  # set them all to nothing
        indicatorClass=indic.Indicator([symbol],sd,ed)
        BollingerValues=indicatorClass.BollingerBands()
        MACDValues=indicatorClass.MACD()
        CCIValues=indicatorClass.CCI()
        StateList=[]
        for index in trades.index:
            try:
                if BollingerValues[index]<=-1:
                    BV=1
                elif BollingerValues[index]>-2 and BollingerValues[index]<-1.5:
                    BV=1
                elif BollingerValues[index]>-1.5 and BollingerValues[index]<-1:
                    BV=2
                elif BollingerValues[index]>-1 and BollingerValues[index]<-.5:
                    BV=3
                elif BollingerValues[index]>-.5 and BollingerValues[index]<0:
                    BV=4
                elif BollingerValues[index]>0 and BollingerValues[index]<.5:
                    BV=5
                elif BollingerValues[index]>.5 and BollingerValues[index]<1:
                    BV=6
                elif BollingerValues[index]>1 and BollingerValues[index]<1.5:
                    BV=7
                elif BollingerValues[index]>1.5 and BollingerValues[index]<2:
                    BV=8
                elif BollingerValues[index]>1:
                    BV=9
                if MACDValues[0][index]<-2:
                    MAD=0
                elif MACDValues[0][index]>-2 and MACDValues[0][index]<-1.5:
                    MAD=1
                elif MACDValues[0][index]>-1.5 and MACDValues[0][index]<-1:
                    MAD=2
                elif MACDValues[0][index]>-1 and MACDValues[0][index]<-.5:
                    MAD=3
                elif MACDValues[0][index]>-.5 and MACDValues[0][index]<0:
                    MAD=4
                elif MACDValues[0][index]>0 and MACDValues[0][index]<.5:
                    MAD=5
                elif MACDValues[0][index]>.5 and MACDValues[0][index]<1:
                    MAD=6
                elif MACDValues[0][index]>1 and MACDValues[0][index]<1.5:
                    MAD=7
                elif MACDValues[0][index]>1.5 and MACDValues[0][index]<2:
                    MAD=8
                elif MACDValues[0][index]>2:
                    MAD=9
                if CCIValues[index]<-400:
                    CC=0
                elif CCIValues[index]>-400 and CCIValues[index]<-300:
                    CC=1
                elif CCIValues[index]>-300 and CCIValues[index]<-200:
                    CC=2
                elif CCIValues[index]>-200 and CCIValues[index]<-100:
                    CC=3
                elif CCIValues[index]>-100 and CCIValues[index]<0:
                    CC=4
                elif CCIValues[index]>0 and CCIValues[index]<100:
                    CC=5
                elif CCIValues[index]>100 and CCIValues[index]<200:
                    CC=6
                elif CCIValues[index]>200 and CCIValues[index]<300:
                    CC=7
                elif CCIValues[index]>300 and CCIValues[index]<400:
                    CC=8
                elif CCIValues[index]>400:
                    CC=9
                StateList.append(str(BV)+str(MAD)+str(CC))
            except KeyError:
                StateList.append(000)                                                                                                                                         
        HoldingValue=0
        NewState=str(HoldingValue)+str(StateList[0])
        j=0
        for i in trades.index:
            NextAction=QlearnerTrader.querysetstate(int(NewState))
            if NextAction==2 and HoldingValue==2:
                trades[symbol][i]=2000
                HoldingValue=1
            elif NextAction==2 and HoldingValue==0:
                trades[symbol][i]=1000
                HoldingValue=1
            elif NextAction==1:
                trades[symbol][i]=0
            elif NextAction==0 and HoldingValue==1:
                trades[symbol][i]=-2000
                HoldingValue=2
            elif NextAction==0 and HoldingValue==0:
                trades[symbol][i]=-1000
                HoldingValue=2
            NewState=str(HoldingValue)+str(StateList[j])
            j=j+1                                                                                                                                  
        if self.verbose:                                                                                                                                         
            print(type(trades))  # it better be a DataFrame!                                                                                                                                         
        if self.verbose:                                                                                                                                         
            print(trades)                                                                                                                                        
        if self.verbose:                                                                                                                                         
            print(prices_all)
        trades.rename(columns={symbol: "Shares"})                                                                                                                                        
        return trades                                                                                                                                        
                                                                                                                                         
                                                                                                                                         
if __name__ == "__main__":                                                                                                                                           
    print("One does not simply think up a strategy")                                                                                                                                         
