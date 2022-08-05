""""""                                                                                                                                           
"""Assess a betting strategy.                                                                                                                                        
                                                                                                                                         
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
                                                                                                                                         
Student Name: Dana Golden (replace with your name)                                                                                                                                           
GT User ID: jgolden36 (replace with your User ID)                                                                                                                                        
GT ID: 903190767 (replace with your GT ID)                                                                                                                                           
"""                                                                                                                                          
                                                                                                                                         
import numpy as np                                                                                                                                           
                                                                                                                                         
                                                                                                                                         
def author():                                                                                                                                        
    """                                                                                                                                          
    :return: The GT username of the student                                                                                                                                          
    :rtype: str                                                                                                                                          
    """                                                                                                                                          
    return "jgolden36"  # replace tb34 with your Georgia Tech username.                                                                                                                                          
                                                                                                                                         
                                                                                                                                         
def gtid():                                                                                                                                          
    """                                                                                                                                          
    :return: The GT ID of the student                                                                                                                                        
    :rtype: int                                                                                                                                          
    """                                                                                                                                          
    return 903190767  # replace with your GT ID number                                                                                                                                           
                                                                                                                                         
                                                                                                                                         
def get_spin_result(win_prob):                                                                                                                                           
    """                                                                                                                                          
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.                                                                                                                                          
                                                                                                                                         
    :param win_prob: The probability of winning                                                                                                                                          
    :type win_prob: float                                                                                                                                        
    :return: The result of the spin.                                                                                                                                         
    :rtype: bool                                                                                                                                         
    """                                                                                                                                          
    result = False                                                                                                                                           
    if np.random.random() <= win_prob:                                                                                                                                           
        result = True                                                                                                                                        
    return result                                                                                                                                        
                                                                                                                                         
                                                                                                                                         
def test_code():                                                                                                                                         
    """                                                                                                                                          
    Method to test your code                                                                                                                                         
    """                                                                                                                                          
    win_prob = 0.4637  # set appropriately to the probability of a win                                                                                                                                         
    np.random.seed(gtid())  # do this only once                                                                                                                                          
    print(get_spin_result(win_prob))  # test the roulette spin                                                                                                                                           
    # add your code here to implement the experiments
    import matplotlib.pyplot as plt
    winningsListOverall=[] 
    episodes=np.arange(300)
    j=0
    for i in range(10):
        k=0
        winningsListBet=np.zeros(300)
        episode_winnings=0
        winningsListBet[0]=0
        while episode_winnings<80:
            won=False
            bet=1
            while won!=True:
                k=k+1
                won=get_spin_result(win_prob)
                if won==True:
                    episode_winnings = episode_winnings + bet
                    winningsListBet[k]=winningsListBet[k]+episode_winnings
                else:
                    episode_winnings = episode_winnings - bet
                    winningsListBet[k]=winningsListBet[k]+episode_winnings
                    bet = bet * 2
        if k>300:
            winningsListBet=winningsListBet[0:299]
        if k<300:
            addon=np.ones(300-k)*winningsListBet[k]
            winningsListBet[k:300]=winningsListBet[k:300]+addon
        plt.plot(episodes,winningsListBet)
        if j==0:
            winningsListOverall=winningsListBet
            j=j+1
        else:
            winningsListOverall=np.vstack((winningsListOverall,winningsListBet))
    plt.ylabel('Winnings')
    plt.xlabel('Time')
    plt.ylim([-256, 100])
    plt.title("Winnings 10 Episodes")
    plt.savefig("Winnings 10 Episodes")
    j=1
    for i in range(1000):
        winningsListBet=np.zeros(1000)
        episode_winnings=0
        i=0
        winningsListBet[i]=winningsListBet[i]+episode_winnings
        while episode_winnings<80:
            won=False
            bet=1
            while won!=True:
                i=i+1
                won=get_spin_result(win_prob)
                if won==True:
                    episode_winnings = episode_winnings + bet
                    winningsListBet[i]=winningsListBet[i]+episode_winnings
                else:
                    episode_winnings = episode_winnings - bet
                    winningsListBet[i]=winningsListBet[i]+episode_winnings
                    bet = bet * 2
        if i<1000:
            addon=np.ones(1000-i)*winningsListBet[i]
            winningsListBet[i:1000]=winningsListBet[i:1000]+addon
        if j==1:
            winningsListOverall=winningsListBet
            j=j+1
        else:
            winningsListOverall=np.vstack((winningsListOverall,winningsListBet))
    WinningListMean=np.mean(winningsListOverall,axis=0)
    WinningListPlusSTD=WinningListMean+np.std(winningsListOverall,axis=0)
    WinningListMinusSTD=WinningListMean-np.std(winningsListOverall,axis=0)
    print(np.mean(winningsListOverall[:,999]))
    print(np.sum(winningsListOverall[:,999]<80))
    episodes=np.arange(1000)
    plt.plot(episodes,WinningListMean,label="Mean Winnings")
    plt.plot(episodes,WinningListPlusSTD,label="Mean Winnings plus Standard deviation")
    plt.plot(episodes,WinningListMinusSTD,label="Mean Winnings minus Standard deviation")
    plt.ylabel('Winnings')
    plt.xlabel('Time')
    plt.title("Winnings Mean 1000 Episodes without loss limit")
    plt.ylim([-256, 100])
    plt.legend()
    plt.savefig("Winnings Mean 1000 Episodes without loss limit")
    WinningListMedian=np.median(winningsListOverall,axis=0)
    WinningListMedianPlusSTD=WinningListMedian+np.std(winningsListOverall,axis=0)
    WinningListMedianMinusSTD=WinningListMedian-np.std(winningsListOverall,axis=0)
    plt.plot(episodes,WinningListMedian, label="Median Winnings")
    plt.plot(episodes,WinningListPlusSTD, label="Median Winnings plus Standard Deviation")
    plt.plot(episodes,WinningListMinusSTD, label="Median Winnings Minus Standard Deviation")
    plt.ylabel('Winnings')
    plt.xlabel('Time')
    plt.title("Winnings Median 1000 Episodes without loss limit")
    plt.ylim([-256, 100])
    plt.legend()
    plt.savefig("Winnings Median 1000 Episodes without loss limit")
    j=1
    for i in range(1000):
        winningsListBet=np.zeros(1000)
        episode_winnings=0
        i=0
        winningsListBet[i]=winningsListBet[i]+episode_winnings
        while episode_winnings<80 and episode_winnings>-256:
            won=False
            bet=1
            while won!=True:
                if episode_winnings-bet<-256:
                    bet=(episode_winnings+256)
                i=i+1
                won=get_spin_result(win_prob)
                if won==True:
                    episode_winnings = episode_winnings + bet
                    winningsListBet[i]=winningsListBet[i]+episode_winnings
                else:
                    episode_winnings = episode_winnings - bet
                    winningsListBet[i]=winningsListBet[i]+episode_winnings
                    bet = bet * 2
        if i<1000:
            addon=np.ones(1000-i)*winningsListBet[i]
            winningsListBet[i:1000]=winningsListBet[i:1000]+addon
        if j==1:
            winningsListOverall=winningsListBet
            j=j+1
        else:
            winningsListOverall=np.vstack((winningsListOverall,winningsListBet))
    WinningListMean=np.mean(winningsListOverall,axis=0)
    WinningListPlusSTD=WinningListMean+np.std(winningsListOverall,axis=0)
    WinningListMinusSTD=WinningListMean-np.std(winningsListOverall,axis=0)
    print(np.mean(winningsListOverall[:,999]))
    print(np.sum(winningsListOverall[:,999]<80))
    episodes=np.arange(1000)
    plt.plot(episodes,WinningListMean,label="Mean Winnings")
    plt.plot(episodes,WinningListPlusSTD,label="Mean Winnings plus Standard deviation")
    plt.plot(episodes,WinningListMinusSTD,label="Mean Winnings minus Standard deviation")
    plt.ylabel('Winnings')
    plt.xlabel('Time')
    plt.title("Winnings Mean 1000 Episodes with loss limit")
    plt.ylim([-256, 100])
    plt.legend()
    plt.savefig("Winnings Mean 1000 Episodes with loss limit")
    WinningListMedian=np.median(winningsListOverall,axis=0)
    WinningListMedianPlusSTD=WinningListMedian+np.std(winningsListOverall,axis=0)
    WinningListMedianMinusSTD=WinningListMedian-np.std(winningsListOverall,axis=0)
    plt.plot(episodes,WinningListMedian, label="Median Winnings")
    plt.plot(episodes,WinningListPlusSTD, label="Median Winnings plus Standard Deviation")
    plt.plot(episodes,WinningListMinusSTD, label="Median Winnings Minus Standard Deviation")
    plt.ylabel('Winnings')
    plt.xlabel('Time')
    plt.title("Winnings Median 1000 Episodes with loss limit")
    plt.ylim([-256, 100])
    plt.legend()
    plt.savefig("Winnings Median 1000 Episodes with loss limit")
if __name__ == "__main__":                                                                                                                                           
    test_code()                                                                                                                                          
