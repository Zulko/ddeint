# ddeint

[![Build Status](https://travis-ci.org/Zulko/ddeint.svg?branch=master)](https://travis-ci.org/Zulko/ddeint)

Scipy-based delay differential equation (DDE) solver. See the docstrings and examples for more infos.

## Examples


```python
from pylab import cos, linspace, subplots
from ddeint import ddeint


def model(Y, t):
    return -Y(t - 3 * cos(Y(t)) ** 2)


def values_before_zero(t):
    return 1


tt = linspace(0, 30, 2000)
yy = ddeint(model, values_before_zero, tt)

fig, ax = subplots(1, figsize=(4, 4))
ax.plot(tt, yy)
ax.figure.savefig("variable_delay.jpeg")
```

![screenshot](https://github.com/Zulko/ddeint/raw/master/examples/variable_delay.jpeg)


## Licence


Public domain. Everyone is welcome to contribute !

##Installation

ddeint can be installed by unzipping the source code in one directory and using this command: ::

    (sudo) python setup.py install

You can also install it directly from the Python Package Index with this command: ::

    (sudo) pip install ddeint 
