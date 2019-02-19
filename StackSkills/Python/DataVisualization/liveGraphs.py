import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.animation as animation

style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):
    pull_data = open("myData.txt", "r").read()
    data_list = pull_data.split('\n')
    xs = []
    ys = []

    for line in data_list:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(int(x))
            ys.append(int(y))

    ax1.clear()
    ax1.plot(xs, ys)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
