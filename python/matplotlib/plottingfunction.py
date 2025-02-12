import numpy as np
import matplotlib.pyplot as plt

def plotline(d1,d2,parameterDict):
    fig, ax=plt.subplots()
    ax.plot(d1,d2,**parameterDict)
    print("showing graph")
    plt.show()
    print("done")

def plotdots(d1,d2,parameterDict):
    fig, ax=plt.subplots()
    ax.scatter(d1,d2,**parameterDict)
    print("showing graph")
    plt.show()
    print("done")