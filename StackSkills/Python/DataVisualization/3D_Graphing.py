import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure()

ax1 = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 5, 7, 9, 2, 7, 8, 1, 1, 5]
z = [5, 2, 8, 7, 4, 3, 5, 2, 9, 10]

ax1.plot(x, y, z)

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

plt.show()
