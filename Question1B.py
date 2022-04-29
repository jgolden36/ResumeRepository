def CumSUMstatPlot(n=100,mean1=0,mean2=1.5,var1=1,var2=1.5):
	import numpy as np
	import matplotlib.pyplot as plt
	import pandas as pd
	import math
	FirstVector=np.random.normal(mean1,math.sqrt(var1),n)
	SecondVector=np.random.normal(mean2,math.sqrt(var2),n)
	combined=np.vstack((FirstVector,SecondVector)).reshape(FirstVector.shape[0]+SecondVector.shape[0])
	series=pd.Series(combined)
	cumsum=series.cumsum()
	print(cumsum)
	plt.plot(cumsum)
	plt.show()
	#sequential=np.arange(0,200,1,dtype=int)
	#WithTimes=np.hstack(sequential,combined)

CumSUMstatPlot()