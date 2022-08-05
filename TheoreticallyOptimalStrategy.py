import numpy as np
import pandas as pd
import datetime as dt
from util import get_data, plot_data  
class TheoreticallyOptimalStrategy(object):
    def __init__(self, symbol=['JPM'],sd=dt.datetime(2008, 1, 1),ed=dt.datetime(2009,12,31),sv=100000):
        #pass # move along, these aren't the drones you're looking for
        self.symbol=symbol
        self.ed=ed
        self.sd=sd
        self.sv=sv
    def testPolicy(self,symbol=['JPM'],sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = 100000):
        PricesofStock=get_data(self.symbol, pd.date_range(self.sd, self.ed),addSPY=False)
        PricesofStock=PricesofStock.ffill(axis = 0)
        PricesofStock=PricesofStock.bfill(axis = 0)
        i=0
        rowvalue1=0
        rowvalue2=0
        orders_df=PricesofStock*0
        orders_df=orders_df.rename(columns = {symbol[0]:'Shares'})
        orders_df['Shares'][0]=0
        for index, row in PricesofStock.iterrows():
            rowvalue2=PricesofStock[symbol[0]][index]
            if rowvalue2>rowvalue1:
                if orders_df['Shares'].sum()<1000:
                    orders_df['Shares'][i-1]=1000-orders_df['Shares'].sum()
                else:
                    orders_df['Shares'][i-1]=0
            elif rowvalue2<rowvalue1:
                if orders_df['Shares'].sum()>-1000:
                    orders_df['Shares'][i-1]=-1000-orders_df['Shares'].sum()
                else:
                    orders_df['Shares'][i-1]=0
            else:
                orders_df['Shares'][i-1]=0
            i=i+1
            rowvalue1=PricesofStock[symbol[0]][index]
        return orders_df
    def author(self):
        return 'jgolden36'