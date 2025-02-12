import numpy as np
import matplotlib.pyplot as plt

d1=np.arange(1,8)
d2=np.array([11,12,8,5,2,10,1])
fig, ax = plt.subplots()
ax.plot(d1,d2,marker="H", c=(0.2,0.75,0.8),linestyle='-.',linewidth=2,markeredgecolor='y',markerfacecolor='r',markeredgewidth='2')
plt.xlim(0,15)
plt.ylim(0,15)
plt.show()

#linestyles

#'-' solid line style
#'--' dashed line style
#'-.' dash-dot line style
#':' dotted line style

#a lot of parameters for plt.plot()
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot
