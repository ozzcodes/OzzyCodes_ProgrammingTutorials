import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig = plt.figure()

ax1 = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 5, 7, 9, 2, 7, 8, 1, 1, 5]
z = np.zeros(10)

dx = np.ones(10)
dy = np.ones(10)
dz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ax1.bar3d(x, y, z, dx, dy, dz)

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')
plt.legend()
plt.show()
