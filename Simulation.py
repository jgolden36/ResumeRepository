def GamePlayed(Player1Start=4,Player2Start=4,PotStart=2):
	import numpy as np 
	import math
	Turn=1
	Player1Coins=Player1Start
	Player2Coins=Player2Start
	Pot=PotStart
	GameOver=False
	TurnCount=0
	RoundCount=0
	while GameOver is not True:
		if Turn==2:
			RoundCount=RoundCount+1
		SimulatedDieRoll=np.random.uniform()
		TurnCount=TurnCount+1
		if SimulatedDieRoll<=1.0/6.0:
			pass
		elif SimulatedDieRoll<=2.0/6.0:
			Pot=0
			if Turn==1:
				Player1Coins=Player1Coins+Pot
			else:
				Player2Coins=Player2Coins+Pot
		elif SimulatedDieRoll<=3.0/6.0:
			CoinsTakenHalf=math.floor(Pot/2)
			Pot=Pot-CoinsTakenHalf
			if Turn==1:
				Player1Coins=Player1Coins+CoinsTakenHalf
			else:
				Player2Coins=Player2Coins+CoinsTakenHalf
		else:
			Pot=Pot+1
			if Turn==1:
				Player1Coins=Player1Coins-1
			else:
				Player2Coins=Player2Coins-1
		if Player1Coins<0 or Player2Coins<0:
			GameOver=True
			if Turn==1:
				RoundCount=RoundCount+1
		else:
			if Turn==1:
				Turn=2
			else:
				Turn=1
	if Turn==1:
		Winner=2
	else:
		Winner=1
	return (RoundCount,Winner)

def RepeatSims(NumberofIterations=1000,P1S=4,P2S=4,PS=2):
	import matplotlib.pyplot as plt
	import numpy as np
	StartingValue=GamePlayed()
	ListofCounts=[StartingValue[0]]
	WinnerList=[0,0]
	WinnerList[StartingValue[1]-1]=1
	for i in range(NumberofIterations-1):
		PlayTuple=GamePlayed(P1S,P2S,PS)
		ListofCounts.append(PlayTuple[0])
		WinnerList[PlayTuple[1]-1]+=1
	print(np.mean(ListofCounts))
	print(np.std(ListofCounts))
	HistogramTitle='Distribution of total rounds for '+str(NumberofIterations)+' Iterations'
	BarchartTitle='Victory by Player for '+str(NumberofIterations)+' Iterations'
	plt.hist(ListofCounts)
	plt.title(HistogramTitle)
	plt.xlabel("Number of Rounds")
	plt.ylabel("Count")
	plt.show()
	plt.bar(["Player 1 wins","Player 2 wins"],WinnerList)
	plt.xlabel("Player")
	plt.ylabel("Wins")
	plt.title(BarchartTitle)
	plt.show()

RepeatSims(NumberofIterations=100)
RepeatSims()
RepeatSims(NumberofIterations=10000)
RepeatSims(NumberofIterations=1000000)
RepeatSims(NumberofIterations=1000,P1S=8,P2S=8,PS=4)
RepeatSims(NumberofIterations=1000,P1S=16,P2S=16,PS=8)
RepeatSims(NumberofIterations=1000,P1S=32,P2S=32,PS=16)
RepeatSims(NumberofIterations=1000,P1S=64,P2S=64,PS=32)
RepeatSims(NumberofIterations=1000,P1S=128,P2S=128,PS=64)