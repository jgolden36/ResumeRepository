import os
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
#os.chdir("C:/Users/Dana Annie/Downloads/Textbooks Spring 2022/OMS Analytics/Computational Data Analysis/homework2-7")
def ReshapeImage(file="yalefaces/subject01.glasses.gif"):
    from skimage.measure import block_reduce
    from PIL import Image
    import numpy as np
    image=Image.open(file)
    imageArray=np.array(image, dtype='int32')
    NewImage=block_reduce(imageArray, block_size=(4,4))
    return NewImage

Subject1Train=['data/yalefaces/subject01.glasses.gif','data/yalefaces/subject01.happy.gif','data/yalefaces/subject01.leftlight.gif','data/yalefaces/subject01.noglasses.gif','data/yalefaces/subject01.normal.gif','data/yalefaces/subject01.rightlight.gif','data/yalefaces/subject01.sad.gif','data/yalefaces/subject01.sleepy.gif','data/yalefaces/subject01.surprised.gif','data/yalefaces/subject01.wink.gif']
Subject1Test=['data/yalefaces/subject01-test.gif']
Subject2Train=['data/yalefaces/subject02.glasses.gif','data/yalefaces/subject02.happy.gif','data/yalefaces/subject02.leftlight.gif','data/yalefaces/subject02.noglasses.gif','data/yalefaces/subject02.normal.gif','data/yalefaces/subject02.rightlight.gif','data/yalefaces/subject02.sad.gif','data/yalefaces/subject02.sleepy.gif','data/yalefaces/subject02.wink.gif']
Subject2Test=['data/yalefaces/subject02-test.gif']

def Eigenface(fileList=Subject1Train):
    import numpy as np
    FileMatrix=ReshapeImage(fileList[0])
    dataMatrix=FileMatrix.flatten()
    print(dataMatrix.shape)
    for file in range(1,len(fileList)):
        FileMatrix=ReshapeImage(fileList[file])
        FlatVector=FileMatrix.flatten()
        dataMatrix = np.vstack([dataMatrix, FlatVector])
    u, s, vh=np.linalg.svd(np.transpose(dataMatrix))
    Eigenvectors=u[:,0:6]
    mean=np.mean(dataMatrix)
    Eigenvalues=s**2
    return Eigenvectors,FileMatrix.shape

x,y=Eigenface()
z,w=Eigenface(fileList=Subject2Train)
for i in range(6):
    NewImage=np.reshape(x[:,i],y)
    plt.imshow(NewImage)
    plt.show()
    NewImage=np.reshape(z[:,i],w)
    plt.imshow(NewImage)
    plt.show()

def FacialRecognition(eigenvalues=x,testImageList=Subject1Test):
    import numpy as np
    Eigenface1=eigenvalues[:,0]
    Eigenface2=eigenvalues[:,1]
    FileMatrix=ReshapeImage(Subject1Test[0])
    dataMatrix=FileMatrix.flatten()
    EigenfaceDecomposition1=np.dot(np.dot(Eigenface1,np.transpose(Eigenface1)),dataMatrix)
    EigenfaceDecomposition2=np.dot(np.dot(Eigenface2,np.transpose(Eigenface2)),dataMatrix)
    DistanceMatrix1=dataMatrix-EigenfaceDecomposition1
    DistanceMatrix2=dataMatrix-EigenfaceDecomposition2
    Distance1=np.linalg.norm(DistanceMatrix1,ord=2)**2
    Distance2=np.linalg.norm(DistanceMatrix2,ord=2)**2
    return Distance1,Distance2

Distance1,Distance2=FacialRecognition()
Distance3,Distance4=FacialRecognition(eigenvalues=z,testImageList=Subject2Test)
print(Distance1,Distance2,Distance3,Distance4)
