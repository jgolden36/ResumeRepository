import os
os.chdir('C:/Users/bnhas/Downloads/SCF_PRICES')
def getDataForAnalysis(file='SCF_PRICES.csv'):
    import pandas as pd
    tableOfData=pd.read_csv(file)
    tableOfData['date']=pd.to_datetime(tableOfData['date'], format='%Y-%m-%d')
    mask1=tableOfData['date'].dt.year>2000
    RecentDates=tableOfData[mask1]
    RecentDates.to_csv('recent.csv') 
    return tableOfData

def CreateLists(file1,file2):
    import pandas as pd
    leadershipDict={}
    sectorlist=[1,2,3,4]
    recentDataFrame=pd.read_csv(file1)
    dataframeSectors=pd.read_csv(file2,header=0)
    for sector in sectorlist:
        #print(sector)
        leaderlist=[]
        sectorMask=recentDataFrame['Sector Code']==sector
        Datelistlist=recentDataFrame[sectorMask].date.unique()
        datelist=list(Datelistlist)
        commoditylist=recentDataFrame[sectorMask].symbol.unique()
        for date in datelist:
            print(date)
            dateMask=recentDataFrame['date']==date
            dateList=[]
            for commodity in commoditylist:
                commodityMask=recentDataFrame['symbol']==commodity
                if 1 in recentDataFrame[commodityMask&dateMask]['Movement Greater than 4 percent'].unique():
                    dateList.append(1)
                else:
                    dateList.append(0)
            leaderlist.append(dateList)
        leadershipDict[sector]={'CommodityWentUp5Percent':leaderlist}
    print(leadershipDict)
    sectors=['Financial','Energy','Metals','Agriculture']
    for sector in sectorlist:
        leadershipSector=dataframeSectors[str(sector)]
        leadershipDict[sector]['SectorWentUp5Percent']=list(leadershipSector)
    for sector in sectorlist:
        label=findLeader(leadershipDict[sector]['CommodityWentUp5Percent'],leadershipDict[sector]['SectorWentUp5Percent'])
        print(label)
def GrangerCausalityTestofCommodities(commoditySeries1,commoditySeries2):
    from statsmodels.tsa.stattools import grangercausalitytests
    import numpy as np
    grangercausalitytests(df[['column1', 'column2']], maxlag=[5])

def findLeader(CommodityWentUp5Percent, SectorWentUp5Percent):
    import numpy as np
    hypothesisClass=[]
    label=''
    for i in range(len(CommodityWentUp5Percent[0])):
        Hypothesis1=np.zeros(len(CommodityWentUp5Percent[0]))
        Hypothesis1[i]+=1
        hypothesisClass.append(Hypothesis1)
    for case in range(len(CommodityWentUp5Percent)):
        hx=[]
        for hypothesis in hypothesisClass:
            LeaderLocation=np.where(hypothesis == 1)[0][0]
            if CommodityWentUp5Percent[case][LeaderLocation]==1:
                hx.append(1)
            else:
                hx.append(0)
        if sum(hx)==0:
            label=label+'No leadership'
        elif sum(hx)==len(hx):
            label=label+'Market leaders lead'
        else:
            label=label+'Cannot say '
            fightLabel=SectorWentUp5Percent[case]
            k=0
            for i in hx:
                if i!=fightLabel:
                    hypothesisClass.pop(k)
                    k=k-1
                k=k+1
    print(hypothesisClass)
    return label

CreateLists(file1='recent1.csv',file2='recent2.csv')
