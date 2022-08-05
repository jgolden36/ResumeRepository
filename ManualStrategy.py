import numpy as np
import pandas as pd
import datetime as dt
from util import get_data, plot_data  
import indicators as Indc
import marketsimcode as MSC
import indicators as indc
import matplotlib.pyplot as plt
class ManualStrategy(object):
    def __init__(self, symbol=['JPM'],sd=dt.datetime(2008, 1, 1),ed=dt.datetime(2009,12,31),sv=100000):
        #pass # move along, these aren't the drones you're looking for
        self.symbol=symbol
        self.ed=ed
        self.sd=sd
        self.sv=sv
    def testPolicy(self,symbol=['JPM'],sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = 100000):
        IndicatorRun=indc.Indicator(symbol=self.symbol,sd=self.sd,ed=self.ed)
        PricesofStock=get_data(self.symbol, pd.date_range(self.sd, self.ed),addSPY=False)
        PricesofStock=PricesofStock.ffill(axis = 0)
        PricesofStock=PricesofStock.bfill(axis = 0)
        BollingerBands=IndicatorRun.BollingerBands()
        CCI=IndicatorRun.CCI()
        StochasticIndicator=IndicatorRun.StochasticIndicator()
        Momentum=IndicatorRun.Momentum()
        MACD,signal=IndicatorRun.MACD()
        i=0
        rowvalue1=0
        rowvalue2=0
        orders_df=PricesofStock*0
        orders_df=orders_df.rename(columns = {symbol[0]:'Shares'})
        orders_df['Shares'][0]=0
        signalList=[]
        j=0
        self.BuydateList=[]
        self.SelldateList=[]
        for index in PricesofStock.index:
            BuysignalCounter=0
            SellsignalCounter=0
            try:
                if BollingerBands[index]>1:
                    SellsignalCounter=SellsignalCounter+1
                elif  BollingerBands[index]<-1:
                    BuysignalCounter=BuysignalCounter+1
                if CCI[index]>100:
                    SellsignalCounter=SellsignalCounter+1
                elif CCI[index]<-100:
                    BuysignalCounter=BuysignalCounter+1
                if MACD[index]-signal[index]>.2:
                    SellsignalCounter=SellsignalCounter+1
                elif MACD[index]-signal[index]<-.2:
                    BuysignalCounter=BuysignalCounter+1
                #if Momentum[j-6]>.2:
                    #SellsignalCounter=SellsignalCounter+1
                #elif Momentum[j-6]<-.2:
                    #BuysignalCounter=BuysignalCounter+1
                #if StochasticIndicator[j-15]>1.5:
                    #SellsignalCounter=SellsignalCounter+1
                #elif StochasticIndicator[j-15]<.5:
                    #BuysignalCounter=BuysignalCounter+1
            except KeyError:
                pass
            if SellsignalCounter==3 and orders_df['Shares'].sum()>-1000:
                orders_df['Shares'][j]=-1000-orders_df['Shares'].sum()
                self.SelldateList.append(index)
            elif BuysignalCounter>=2 and orders_df['Shares'].sum()<1000:
                orders_df['Shares'][j]=1000-orders_df['Shares'].sum()
                self.BuydateList.append(index)
            else:
                orders_df['Shares'][j]=0
            j=j+1
        return orders_df
    def createGraph(self,title,orders_df,symbol=['JPM'],sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = 100000):
        benchmark=get_data(symbol, pd.date_range(sd, ed)).mul(0)
        benchmark=benchmark.rename(columns = {symbol[0]:'Shares'})
        benchmark['Shares'][0]=1000
        MarketSim=MSC.MarketSim()
        BenchmarkPerformance=MarketSim.compute_portvals(                                                                                                                                        
            benchmark,                                                                                                                                           
            start_val=100000,                                                                                                                                           
            commission=0,                                                                                                                                         
            impact=0)
        ManualPerformance=MarketSim.compute_portvals(                                                                                                                                        
        orders_df,                                                                                                                                           
        start_val=100000,                                                                                                                                           
        commission=0,                                                                                                                                         
        impact=0)
        plt.clf()
        plt.plot(ManualPerformance.index,ManualPerformance[0]/100000,'r',label='Indicator Performance')
        plt.plot(BenchmarkPerformance.index,BenchmarkPerformance[0]/100000,'m',label='Benchmark')
        plt.xlabel('Date')
        plt.ylabel('Total Value')
        plt.title('Benchmark vs Indicator Traded')
        plt.legend()
        for i in self.SelldateList:
            plt.axvline(i, color='b')
        for i in self.BuydateList:
            plt.axvline(i, color='k')
        PlotTitle=title+'.png'
        plt.savefig(PlotTitle)
    def author(self):
        return 'jgolden36'