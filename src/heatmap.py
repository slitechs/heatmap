import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
plt.style.use("seaborn-v0_8")
from  matplotlib.colors import LinearSegmentedColormap

# Generate a 40 by 40 random int matrix (sample data)
data = np.random.rand(40,40)
print(data)

# Color palette
c = ["darkgreen","green","chartreuse","yellow","orange","red","darkred"]
v = [0,.2,.4,.5,.6,.8,1.]
l = list(zip(v,c))
cmap=LinearSegmentedColormap.from_list('rg',l, N=256)

# Plot
heat_map = sns.heatmap( data, linewidths = 0 , annot = False, cmap=cmap)
plt.title( "Heatmap" )
plt.show()