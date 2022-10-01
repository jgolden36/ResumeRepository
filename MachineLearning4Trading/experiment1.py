import marketsimcode as MSC
import StrategyLearner as SL
import ManualStrategy as ML
import matplotlib as plt
class Experiment1(object):
    def __init__(self):    
        pass
    def run():
        MarketSim=MSC.MarketSim()
        Manual=ML.ManualStrategy()
        ManualInSample=Manual.testPolicy(symbol=['JPM'],sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = 100000)
        ManualOutofSample=Manual.testPolicy(symbol=['JPM'],sd=dt.datetime(2009, 1, 1),ed=dt.datetime(2010, 1, 1), sv = 100000)
        Strategem=SL.StrategyLearner()
        Strategem.add_evidence(symbol="JPM",sd=dt.datetime(2008, 1, 1),ed=dt.datetime(2009, 1, 1),sv=10000)
        TradesInSample=Strategem.testPolicy(symbol="JPM",sd=dt.datetime(2008, 1, 1),ed=dt.datetime(2009, 1, 1),sv=10000)
        TradesOutOfSample=Strategem.testPolicy(symbol="JPM",sd=dt.datetime(2009, 1, 1),ed=dt.datetime(2010, 1, 1),sv=10000)
        StrategyOOS=MarketSim.compute_portvals(orders_df=TradesOutOfSample,commission=9.95,impact=.005)
        StrategyIS=MarketSim.compute_portvals(orders_df=TradesInSample,commission=9.95,impact=.005)
        ManualIS=MarketSim.compute_portvals(orders_df=ManualOutofSample,commission=9.95,impact=.005)
        ManualOOS=MarketSim.compute_portvals(orders_df=ManualInSample,commission=9.95,impact=.005)
        sd1=dt.datetime(2008, 1, 1)
        ed1=dt.datetime(2009,1,1)
        sd2=dt.datetime(2009, 1, 1)
        ed2=dt.datetime(2010,1,1)
        benchmarkIS=get_data(symbol, pd.date_range(sd1, ed1)).mul(0)
        benchmarkIS=benchmarkIS.rename(columns = {'JPM':'Shares'})
        benchmarkIS['Shares'][0]=1000
        benchmarkOOS=get_data(symbol, pd.date_range(sd1, ed1)).mul(0)
        benchmarkOOS=benchmarkOOS.rename(columns = {'JPM':'Shares'})
        benchmarkOOS['Shares'][0]=1000
        BenchMarkISValue=MarketSim.compute_portvals(orders_df=benchmarkIS,commission=9.95,impact=.005)
        BenchMarkOOSValue=MarketSim.compute_portvals(orders_df=benchmarkOOS,commission=9.95,impact=.005)
        plt.clf()
        plt.plot(StrategyIS.index,StrategyIS[0]/100000,'r',label='In Sample Indicator Performance Strategy Learner')
        plt.plot(ManualIS.index,ManualIS[0]/100000,'r',label='In Sample Indicator Performance Manual Learner')
        plt.plot(BenchMarkISValue.index,BenchMarkISValue[0]/100000,'m',label=' In Sample Performance Benchmark')
        plt.xlabel('Date')
        plt.ylabel('Total Value')
        plt.title('Out of sample Benchmark vs Indicator Traded vs Strategy')
        plt.legend()
        plt.savefig('Out_of_SAMPLE_GRAPH_INDICATORS_experiment1.png')
        plt.clf()
        plt.plot(StrategyOOS.index,StrategyOOS[0]/100000,'r',label='Out of Sample Indicator Performance Strategy Learner')
        plt.plot(ManualOOS.index,ManualOOS[0]/100000,'r',label='Out of Sample Indicator Performance Manual Learner')
        plt.plot(BenchMarkOOSValue.index,BenchMarkOOSValue[0]/100000,'m',label=' Out of Sample Performance Benchmark')
        plt.xlabel('Date')
        plt.ylabel('Total Value')
        plt.title('Out of sample Benchmark vs Indicator Traded vs Strategy')
        plt.legend()
        plt.savefig('Out_of_SAMPLE_GRAPH_INDICATORS_experiment1.png')
    def author():
        return 'jgolden36'
