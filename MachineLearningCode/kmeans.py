import os
import numpy as np
#os.chdir('C:/Users/Dana Annie/Downloads/Homework1')
def getPixels(file='Data/football.bmp'):
    from PIL import Image
    import numpy as np
    im=Image.open(file)
    imageArray = np.array(im, dtype='int32')
    h, w=im.size
    im.close()
    size=h*w
    pixels=np.reshape(imageArray,newshape=(size,3),order="C")
    return pixels

def L2Norm(pixels,centers):
    import numpy as np
    m=len(pixels)
    n=len(centers)
    distancer=np.empty((m,n))
    for i in range(m):
        distancer[i,:]=np.linalg.norm(pixels[i,:]-centers, ord=2, axis=1)**2
    return distancer

def manhattanNorm(pixels,centers):
    import numpy as np
    m=len(pixels)
    n=len(centers)
    distancer=np.empty((m,n))
    for i in range(m):
        distancer[i,:]=np.linalg.norm(pixels[i,:]-centers, ord=1, axis=1)
    return distancer

x=getPixels()
def kmeans(pixels,k,distnaceType="L2"):
    # I used some of the implementation I wrote for K-means from CSE 6040 for this. I used my implementation, not the professor's though
    import time
    import random
    import math
    import numpy as np
    t1_start=time.perf_counter()
    i=0
    #initialize Centers
    sample=np.random.randint(0,len(pixels), size=k)
    initialCenters=pixels[sample,:]
    convergence=0
    Newcenters=initialCenters
    while convergence!=1:
        initialCenters=Newcenters
        #computeDistance
        if distnaceType=="L2":
            distanceMatrix=L2Norm(pixels,Newcenters)
        elif distnaceType=="Manhattan":
            distanceMatrix=manhattanNorm(pixels,Newcenters)
        #assignClusterLabels
        labelAssignment=np.argmin(distanceMatrix,axis=1)
        #UpdateCenters
        Newcenters = np.empty((k, 3))
        for j in range(k):
            Newcenters[j,:]=np.mean(pixels[labelAssignment==j,:],axis=0)
        #convergenceCheck
        if set([tuple(x) for x in initialCenters]) == set([tuple(x) for x in Newcenters]):
            convergence=1
        print("iteration number")
        print(i)
        i=i+1
    t1_stop=time.perf_counter()
    print("Elapsed time:", t1_stop-t1_start)
    return labelAssignment,Newcenters

labels2,centers2=kmeans(x,2)
clusterImage2 = np.array([centers2[j] for j in labels2])
labels4,centers4=kmeans(x,4)
clusterImage4 = np.array([centers4[j] for j in labels4])
labels8,centers8=kmeans(x,8)
clusterImage8 = np.array([centers8[j] for j in labels8])
labels16,centers16=kmeans(x,16)
clusterImage16 = np.array([centers16[j] for j in labels16])
labels2l1,centers2l1=kmeans(x,2,distnaceType="Manhattan")
clusterImage2l1 = np.array([centers2l1[j] for j in labels2l1])
labels4l1,centers4l1=kmeans(x,4,distnaceType="Manhattan")
clusterImage4l1 = np.array([centers4l1[j] for j in labels4l1])
labels8l1,centers8l1=kmeans(x,8,distnaceType="Manhattan")
clusterImage8l1 = np.array([centers8l1[j] for j in labels8l1])
labels16l1,centers16l1=kmeans(x,16,distnaceType="Manhattan")
clusterImage16l1 = np.array([centers16l1[j] for j in labels16l1])


def showImage(file,dataInput):
    from PIL import Image
    from matplotlib.pyplot import imshow
    im=Image.open(file)
    Array1 = np.array(im, dtype='int32')
    r, c, l = Array1.shape
    img_disp = np.reshape(dataInput, (r, c, l), order="C")
    img = Image.fromarray(img_disp, 'RGB')
    img.show()

showImage('Data/football.bmp',clusterImage2)
showImage('Data/football.bmp',clusterImage4)
showImage('Data/football.bmp',clusterImage8)
showImage('Data/football.bmp',clusterImage16)
showImage('Data/football.bmp',clusterImage2l1)
showImage('Data/football.bmp',clusterImage4l1)
showImage('Data/football.bmp',clusterImage8l1)
showImage('Data/football.bmp',clusterImage16l1)
y=getPixels('Data/GeorgiaTech.bmp')
labels2,centers2=kmeans(y,2)
clusterImage2 = np.array([centers2[j] for j in labels2])
labels4,centers4=kmeans(y,4)
clusterImage4 = np.array([centers4[j] for j in labels4])
labels8,centers8=kmeans(y,8)
clusterImage8 = np.array([centers8[j] for j in labels8])
labels16,centers16=kmeans(y,16)
clusterImage16 = np.array([centers16[j] for j in labels16])
labels2l1,centers2l1=kmeans(y,2,distnaceType="Manhattan")
clusterImage2l1 = np.array([centers2l1[j] for j in labels2l1])
labels4l1,centers4l1=kmeans(y,4,distnaceType="Manhattan")
clusterImage4l1 = np.array([centers4l1[j] for j in labels4l1])
labels8l1,centers8l1=kmeans(y,8,distnaceType="Manhattan")
clusterImage8l1 = np.array([centers8l1[j] for j in labels8l1])
labels16l1,centers16l1=kmeans(y,16,distnaceType="Manhattan")
clusterImage16l1 = np.array([centers16l1[j] for j in labels16l1])
showImage('Data/GeorgiaTech.bmp',clusterImage2)
showImage('Data/GeorgiaTech.bmp',clusterImage4)
showImage('Data/GeorgiaTech.bmp',clusterImage8)
showImage('Data/GeorgiaTech.bmp',clusterImage16)
showImage('Data/GeorgiaTech.bmp',clusterImage2l1)
showImage('Data/GeorgiaTech.bmp',clusterImage4l1)
showImage('Data/GeorgiaTech.bmp',clusterImage8l1)
showImage('Data/GeorgiaTech.bmp',clusterImage16l1)
z=getPixels('Data/heart.bmp')
labels2,centers2=kmeans(z,2)
clusterImage2 = np.array([centers2[j] for j in labels2])
labels4,centers4=kmeans(z,4)
clusterImage4 = np.array([centers4[j] for j in labels4])
labels8,centers8=kmeans(z,8)
clusterImage8 = np.array([centers8[j] for j in labels8])
labels16,centers16=kmeans(z,16)
clusterImage16 = np.array([centers16[j] for j in labels16])
labels2l1,centers2l1=kmeans(z,2,distnaceType="Manhattan")
clusterImage2l1 = np.array([centers2l1[j] for j in labels2l1])
labels4l1,centers4l1=kmeans(z,4,distnaceType="Manhattan")
clusterImage4l1 = np.array([centers4l1[j] for j in labels4l1])
labels8l1,centers8l1=kmeans(z,8,distnaceType="Manhattan")
clusterImage8l1 = np.array([centers8l1[j] for j in labels8l1])
labels16l1,centers16l1=kmeans(z,16,distnaceType="Manhattan")
clusterImage16l1 = np.array([centers16l1[j] for j in labels16l1])
showImage('Data/heart.bmp',clusterImage2)
showImage('Data/heart.bmp',clusterImage4)
showImage('Data/heart.bmp',clusterImage8)
showImage('Data/heart.bmp',clusterImage16)
showImage('Data/heart.bmp',clusterImage2l1)
showImage('Data/heart.bmp',clusterImage4l1)
showImage('Data/heart.bmp',clusterImage8l1)
showImage('Data/heart.bmp',clusterImage16l1)
