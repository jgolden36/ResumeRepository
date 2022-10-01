import numpy as np
import pandas as pd
import datetime as dt
from util import get_data, plot_data  
import matplotlib.pyplot as plt
class Indicator(object):
    def __init__(self, symbol=['JPM'],sd=dt.datetime(2008, 1, 1),ed=dt.datetime(2009,12,31)):
        self.symbol=symbol
        self.sd=sd
        self.ed=ed
    def BollingerBands(self):
        PricesofStock=get_data(self.symbol, pd.date_range(self.sd, self.ed))
        SMA=np.convolve(PricesofStock[self.symbol[0]], np.ones(10), 'valid')/10
        StandardDeviation=[]
        for i in range(len(PricesofStock[self.symbol[0]])-9):
            StandardDeviation.append(np.std(PricesofStock[self.symbol[0]][i:9+i]))
        #StandardDeviation=[PricesofStock[self.symbol[0]][:x].std() for x in range(1,len(PricesofStock)+1)]
        bb_valueTop=SMA+2*np.array(StandardDeviation)
        bb_valueBottom=SMA-2*np.array(StandardDeviation)
        return (PricesofStock[self.symbol[0]][9:]-SMA)/2*np.array(StandardDeviation)
    def CCI(self):
        PricesofStock=get_data(self.symbol, pd.date_range(self.sd, self.ed))
        SMA=np.convolve(PricesofStock[self.symbol[0]], np.ones(20), 'valid')/20
        MeanDeviation=[]
        for i in range(len(PricesofStock)-19):
            MeanDeviation.append(np.sum(np.absolute(np.array(PricesofStock[self.symbol[0]][i:19+i])-SMA[i]))/20)
        CCI=(PricesofStock[self.symbol[0]][19:]-SMA)/(np.array(MeanDeviation)*.015)
        return CCI
    def StochasticIndicator(self):
        PricesofStock=get_data(self.symbol, pd.date_range(self.sd, self.ed))
        StochasticIndicator=[]
        for i in range(len(PricesofStock)-14):
            Low14=np.min(PricesofStock[self.symbol[0]][i:13+i])
            High14=np.max(PricesofStock[self.symbol[0]][i:13+i])
            StochasticIndicator.append((PricesofStock[self.symbol[0]][i+14]-Low14)/(High14-Low14))
        return StochasticIndicator
    def MACD(self):
        PricesofStock=get_data(self.symbol, pd.date_range(self.sd, self.ed))
        MovingAverage26=PricesofStock[self.symbol[0]].ewm(span=26, adjust=False).mean()
        MovingAverage12=PricesofStock[self.symbol[0]].ewm(span=12, adjust=False).mean()
        MACD=MovingAverage12-MovingAverage26
        MovingAverage9=MACD.ewm(span=9, adjust=False).mean()
        return MACD,MovingAverage9
    def Momentum(self):
        N=5
        PricesofStock=get_data(self.symbol, pd.date_range(self.sd, self.ed))
        Price=PricesofStock[self.symbol[0]][N:]
        PriceDaysAgo=PricesofStock[self.symbol[0]][:-5]
        Momentum=np.array(Price)/np.array(PriceDaysAgo)-1
        return Momentum
    def run(self):
        self.BollingerBands()
        self.CCI()
        self.StochasticIndicator()
        self.MACD()
        self.Momentum()
    def author(): 
        return 'jgolden36'
