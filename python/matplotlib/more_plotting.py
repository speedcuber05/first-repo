import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0, 2*np.pi, 10)
b = np.sin(a)
fig, ax = plt.subplots(2,2)  
print("done")
ax[0,0].text(75, .025, r'$\mu=115,\ \sigma=15$')
ax.text(75, .025, r'$\mu=115,\ \sigma=15$')
ax.axis([55, 175, 0, 0.03])
ax[1,0].plot(a,b)
ax[0,1].scatter(a,b,s=50,marker='^',alpha=0.7,c='green')   #alpha is transparancy and s is size
plt.show()



#fig is the main canvas of the graph we are going to make
#axes (not be confused by axis) are the basically the graphs we make, in this example we are making 4 graphs in a 2x2 grid
#plt.subplots makes a tuple with 2 elements, the figure and the axes (axes is not axis btw)
#subplot is an axes that is a part of a given figure. subplot = axes but axes is just more general, 
#ax.plot(a,b) makes the graph with a being the x axis and b being the y axis 

# List of Matplotlib marker styles:

# '.'  : Point marker
# ','  : Pixel marker
# 'o'  : Circle marker
# 'v'  : Triangle_down marker
# '^'  : Triangle_up marker
# '<'  : Triangle_left marker
# '>'  : Triangle_right marker
# '1'  : Tri_down marker
# '2'  : Tri_up marker
# '3'  : Tri_left marker
# '4'  : Tri_right marker
# 's'  : Square marker
# 'p'  : Pentagon marker
# '*'  : Star marker
# 'h'  : Hexagon1 marker
# 'H'  : Hexagon2 marker
# '+'  : Plus marker
# 'x'  : X marker
# 'D'  : Diamond marker
# 'd'  : Thin diamond marker
# '|'  : Vertical line marker
# '_'  : Horizontal line marker


# Different ways to specify colors in Matplotlib:

# 1. Named colors (common color names)
# 'red', 'blue', 'green', 'yellow', 'black', 'white', 'cyan', 'magenta', etc.

# 2. Shorthand color codes (single-letter)
# 'r' -> red
# 'g' -> green
# 'b' -> blue
# 'c' -> cyan
# 'm' -> magenta
# 'y' -> yellow
# 'k' -> black
# 'w' -> white

# 3. Hexadecimal color codes (similar to HTML/CSS)
# '#FF5733' -> Orange-red
# '#00FF00' -> Bright green
# '#1E90FF' -> Dodger blue
# '#800080' -> Purple

# 4. RGB and RGBA tuples (values between 0 and 1)
# (1, 0, 0)       -> Pure red
# (0, 1, 0)       -> Pure green
# (0, 0, 1)       -> Pure blue
# (1, 1, 0)       -> Yellow
# (0.5, 0.5, 0.5) -> Gray
# (1, 0, 0, 0.5)  -> Semi-transparent red (RGBA)