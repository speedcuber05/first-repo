import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0, 2*np.pi, 100)
b = np.sin(a)
fig, ax = plt.subplots(2,2)  
print("done")
ax[1,0].plot(x,y)
plt.show()

"""
fig is the main canvas of the graph we are going to make
axes (not be confused by axis) are the basically the graphs we make, in this example we are making 4 graphs in a 2x2 grid
plt.subplots makes a tuple with 2 elements, the figure and the axes (axes is not axis btw)
subplot is an axes that is a part of a given figure. subplot = axes but axes is just more general, 
ax.plot(a,b) makes the graph with a being the x axis and b being the y axis 
"""