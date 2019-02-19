import matplotlib.pyplot as plt
from matplotlib import style

# Created own personal styling for plots
style.use('mystyle')

xs = []
ys = []

for i in range(3, 15):
    x = i
    y = (2 * x ^ 2) / (x + 1.1)

    xs.append(x)
    ys.append(y)

plt.plot(xs, ys)

font = {'family': 'serif',
        'color': 'darkred',
        'size': 18}
# Adding/placing the text
plt.text(xs[-1] / 2, ys[-1] / 2, '(2 * x ^ 2) / (x + 1.1)', fontdict=font)

plt.show()
