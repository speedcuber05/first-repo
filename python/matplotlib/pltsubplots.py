import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
d1,d2,d3,d4=np.random.randn(4,100)
fig,ax=plt.subplots(2,2,figsize=(6.4,4.8),facecolor="green",sharex=True,sharey=False,constrained_layout=True,layout="tight") 
ax[0,0].scatter(d1,d2,s=10,marker="x")
ax[0,1].scatter(d1,d2,s=10,marker="d")
print("showing graph")
plt.show()
print("done")


#sharex and sharey basically means there will only be 1 label
#constrained_layout=True makes sure there is no overlapping of texts and stuff
#layout are just different layouts, negligible difference in simple graphs


#matplotlib.pyplot.subplots(nrows=1, ncols=1, *, sharex=False, sharey=False, squeeze=True, width_ratios=None,
#height_ratios=None, subplot_kw=None, gridspec_kw=None, **fig_kw)

#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots
