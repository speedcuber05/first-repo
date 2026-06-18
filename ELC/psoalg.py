import numpy as np

# f = the whole space/area
# N = number of particles
# S = some subspace in the area f

def pso(f,N,S,a,b,bhat,c):
    
    x = random(-S,S) #initialization of particles in the subspace  
    v = random(-1,1) #giving them initial velocity      
    p = x # local minima, initially x        
    phat = argmin f(p)   #takes the min value from the matrix f(p), f(p) is the matrix of points on the coordinates from matrix p


    Loop

    v = a*v + b*r*(p-x) + bhat*rhat*(phat - x) # the velocity is updated based on the previous velocity, local minima and the global minima with 
    #the random parameter r and rhat and tuning parameters a, b and bhat
    x = x + c*v # position is updated with another tuning parameter c
    update p and phat

    return phat


# r, rhat, x, v, p are NxD matrix,ie N = number of particles with D dimensions
# phat is a vector of D dimensions
# a,b,bhat,c scalers