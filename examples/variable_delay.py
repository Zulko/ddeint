""" DDE where the delay depends on Y(t). """

from pylab import cos, linspace, subplots, show
from ddeint import ddeint


def model(Y, t):
    return -Y(t - 3 * cos(Y(t)) ** 2)


tt = linspace(0, 30, 2000)
yy = ddeint(model, lambda t: 1, tt)

fig, ax = subplots(1, figsize=(4, 4))
ax.plot(tt, yy)

show()
