# ddeint

[![Build Status](https://travis-ci.org/Zulko/ddeint.svg?branch=master)](https://travis-ci.org/Zulko/ddeint)

Scipy-based delay differential equation (DDE) solver. See the docstrings and examples for more infos.

## Examples


```python
from pylab import cos, linspace, subplots
from ddeint import ddeint

# We solve the following system:
# Y(t) = 1 for t < 0
# dY/dt = -Y(t - 3cos(t)**2) for t > 0

def values_before_zero(t):
    return 1

def model(Y, t):
    return -Y(t - 3 * cos(Y(t)) ** 2)

tt = linspace(0, 30, 2000)
yy = ddeint(model, values_before_zero, tt)

fig, ax = subplots(1, figsize=(4, 4))
ax.plot(tt, yy)
ax.figure.savefig("variable_delay.jpeg")
```

![screenshot](https://github.com/Zulko/ddeint/raw/master/examples/variable_delay.jpeg)

```python
from pylab import array, linspace, subplots
from ddeint import ddeint

# We solve the following system:
# X(t) = 1 (t < 0)
# Y(t) = 2 (t < 0)
# dX/dt = X * (1 - Y(t-d)) / 2
# dY/dt = -Y * (1 - X(t-d)) / 2


def model(Y, t, d):
    x, y = Y(t)
    xd, yd = Y(t - d)
    return array([0.5 * x * (1 - yd), -0.5 * y * (1 - xd)])


g = lambda t: array([1, 2])
tt = linspace(2, 30, 20000)

fig, ax = subplots(1, figsize=(4, 4))

for d in [0, 0.2]:
    print("Computing for d=%.02f" % d)
    yy = ddeint(model, g, tt, fargs=(d,))
    # WE PLOT X AGAINST Y
    ax.plot(yy[:, 0], yy[:, 1], lw=2, label="delay = %.01f" % d)

ax.figure.savefig("lotka.jpeg")
```

![screenshot](https://github.com/Zulko/ddeint/raw/master/examples/lotka.jpeg)

## Licence


Public domain. Everyone is welcome to contribute !

## Installation

ddeint can be installed by unzipping the source code in one directory and using this command: ::

    (sudo) python setup.py install

You can also install it directly from the Python Package Index with this command: ::

    (sudo) pip install ddeint 
