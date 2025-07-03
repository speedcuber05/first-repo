import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,4*np.pi,2500)
y=np.cos(x)
fig, ax = plt.subplots()
ax.plot(x,y)
ax.annotate('local min',xy=(3.14,-1), xytext=(4,1.5),arrowprops=dict(facecolor='blue'))
print("showing graph")
arr=np.arange(0,4*np.pi,(np.pi)/4)
ax.set_xticks(arr)
plt.xlim(0,10)
plt.ylim(-2,2)
plt.grid(True)
plt.show()
print('done')