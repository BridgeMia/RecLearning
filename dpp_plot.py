import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
fig = plt.figure()
ax = fig.gca(projection='3d')

a = np.linspace(-1, 1, 100)
b = np.linspace(-1, 1, 100)
# c = np.linspace(-1, 1, 100)
c = 0.5

a, b = np.meshgrid(a, b)
y = 1 + 2 * a * b * c - np.square(a) - np.square(b) - np.square(c)

ax.plot_surface(b, a, y, cmap=plt.get_cmap('rainbow'))
plt.show()
