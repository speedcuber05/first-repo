import matplotlib.pyplot as plt
import numpy as np

# make data:
np.random.seed(10)
D = np.random.normal((3, 5, 4), (1.25, 1.00, 1.25), (10, 3))
print(D)
# plot
fig, ax = plt.subplots()
VP = ax.boxplot(D, positions=[2, 4, 6], widths=1, patch_artist=True,
                showmeans=True, showfliers=True,
                medianprops={"color": "white", "linewidth": 0.5},
                meanprops={"color" : "green","linewidth":5},
                boxprops={"facecolor": "C0", "edgecolor": "black",
                          "linewidth": 0.5},
                whiskerprops={"color": "C0", "linewidth": 0.5},
                capprops={"color": "C0", "linewidth": 2})

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()