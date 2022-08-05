import marketsimcode as MSC
import StrategyLearner as SL
import ManualStrategy as ML
import matplotlib as plt
class Experiment2(object):
    def __init__(self):    
        pass
    def run():
        MarketSimulator=MSC.MarketSim()
        StrategyNoImpact=SLStrategyLearner(impact=0.0, commission=0.0)
        StrategyNoImpact.add_evidence(symbol="JPM",                                                                                                                                        
        sd=dt.datetime(2008, 1, 1),                                                                                                                                          
        ed=dt.datetime(2009, 1, 1),                                                                                                                                          
        sv=10000)
        StrategyNoImpactTrades=StrategyNoImpact.testPolicy(symbol="JPM",                                                                                                                                        
        sd=dt.datetime(2009, 1, 1),                                                                                                                                          
        ed=dt.datetime(2010, 1, 1),                                                                                                                                          
        sv=10000)
        StrategyNoImpactResults=MarketSimulator.compute_portvals(StrategyNoImpactTrades,                                                                                                                                           
        start_val=100000,                                                                                                                                           
        commission=0,                                                                                                                                         
        impact=0)
        StrategyHighImpact=SLStrategyLearner(impact=0.2, commission=0.0)
        StrategyHighImpact.add_evidence(symbol="JPM",                                                                                                                                        
        sd=dt.datetime(2008, 1, 1),                                                                                                                                          
        ed=dt.datetime(2009, 1, 1),                                                                                                                                          
        sv=10000)
        StrategyHighImpactTrades=StrategyHighImpact.testPolicy(symbol="JPM",                                                                                                                                        
        sd=dt.datetime(2009, 1, 1),                                                                                                                                          
        ed=dt.datetime(2010, 1, 1),                                                                                                                                          
        sv=10000)
        StrategyHighImpactResults=MarketSimulator.compute_portvals(StrategyHighImpactTrades,                                                                                                                                           
        start_val=100000,                                                                                                                                           
        commission=0,                                                                                                                                         
        impact=0)
        StrategyMidImpact=SLStrategyLearner(impact=0.1, commission=0.0)
        StrategyMidImpact.add_evidence(symbol="JPM",                                                                                                                                        
        sd=dt.datetime(2008, 1, 1),                                                                                                                                          
        ed=dt.datetime(2009, 1, 1),                                                                                                                                          
        sv=10000)
        StrategyMidImpactTrades=StrategyMidImpact.testPolicy(symbol="JPM",                                                                                                                                        
        sd=dt.datetime(2009, 1, 1),                                                                                                                                          
        ed=dt.datetime(2010, 1, 1),                                                                                                                                          
        sv=10000)
        StrategyMidImpactResuts=MarketSimulator.compute_portvals(StrategyMidImpactTrades,                                                                                                                                           
        start_val=100000,                                                                                                                                           
        commission=0,                                                                                                                                         
        impact=0)
        plt.clf()
        plt.plot(StrategyNoImpactResults.index,StrategyNoImpactResults[0]/100000,'b',label='Cumulative return no impact Strategy Learner')
        plt.plot(StrategyMidImpactResuts.index,StrategyMidImpactResuts[0]/100000,'r',label='Cumulative Return 10 percent Strategy Learner')
        plt.plot(StrategyHighImpactResults.index,StrategyHighImpactResults[0]/100000,'m',label='Cumulative Return 20 percent Strategy Learner')
        plt.xlabel('Date')
        plt.ylabel('Total Value')
        plt.title('In sample cumulative return')
        plt.legend()
        plt.show()
        plt.savefig('In Sample impact Differing.png')
        plt.clf()
        plt.bar('No Impact',StrategyNoImpactResults.std())
        plt.bar('10 percent impact',StrategyMidImpactResuts.std())
        plt.bar('20 percent impact',StrategyHighImpactResults.std())
        plt.xlabel('Impact')
        plt.ylabel('Standard Deviation')
        plt.title('Standard deviation varying impact')
        plt.legend()
        plt.show()
        plt.savefig('In Sample Impact Differing.png')
    def author():
        return 'jgolden36'
