import numpy as np
import matplotlib.pyplot as plt
import random as rand

def toss(n):
    i=0    
    coinData=np.empty(n,dtype=str)
    coin=["heads","tails"]
    while i<n:
        result=rand.choice(coin)
        coinData[i]=result
        i+=1
        
    return coinData

def iterations(n,N):    
    j=0
    data=np.empty(N*n, dtype=str).reshape(N,n)
    while j<N:
        coinData=toss(n)
        data[j]=coinData    
        j+=1
        if j==N/2:
            print('50%  of the iternations done')
    print('iterations done')
    
    return data

def count(n,N):
    data=iterations(n,N)
    headCount=np.empty(N,dtype=int)
    k=0
    while k<N:
        uni=np.unique(data[k],return_counts=True)
        heads=uni[1][0]
        headCount[k]=heads
        k+=1
    print("head count done")
    
    return headCount


def graph(n,N):
    headCount=count(n,N)
    graphData=np.unique(headCount,return_counts=True)
    headPercent=(graphData[0]/n)*100
    headfrequency=graphData[1]
    fig, ax=plt.subplots(layout='constrained')

    ax.bar(headPercent,headfrequency,width=0.1)
    ax.set_xlabel("percentage of heads ")
    ax.set_ylabel("frequency of that percentage")    
    ax.set_title("coin toss")

    print('showing graph')
    
    plt.show()
    print('done')

N=50000   #no of iterations
n=1000   #no of coin tosses in one iterations

graph(n,N)