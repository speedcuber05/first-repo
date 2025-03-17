import numpy as np
import matplotlib.pyplot as plt
import random as rand

def toss(n):     # this is a simulation of a coin toss, n represent the number of times we coin toss per experiment
    i=0    
    coinData=np.empty(n,dtype=str)
    coin=["heads","tails"]
    while i<n:
        result=rand.choice(coin)
        coinData[i]=result
        i+=1
        
    return coinData

def iterations(n,N):    #this is the number of times we are repeating the experiment 
    j=0
    data=np.empty(N*n, dtype=str).reshape(N,n)
    while j<N:
        coinData=toss(n)
        data[j]=coinData    
        j+=1
        for w in range(10,101,10):
            if j==N*w/100:
                print(w,'% of the iternations done')
    return data

def count(n,N):       #this counts the number of heads in each experiment
    print("starting iterations")
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


def graph(n,N):    #this analyses the number of heads in each experiment and plots the graph
    headCount=count(n,N)
    graphData=np.unique(headCount,return_counts=True)
    headPercent=(graphData[0]/n)*100
    headfrequency=graphData[1]
    fig, ax=plt.subplots()

    bar_width = (headPercent[-1] - headPercent[0]) / len(headPercent)
    ax.bar(headPercent,headfrequency,width=bar_width,edgecolor='black')
    ax.set_xlabel("percentage of heads ")
    ax.set_ylabel("frequency of that percentage")    
    ax.set_title("Devansh")
    print('showing graph')
    plt.show()
    print('done')

N=10000  #no of iterations
n=100   #no of coin tosses in one iterations

graph(n,N)