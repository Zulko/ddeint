""" DDE where the delay depends on y. """

from pylab import *
from ddeint import ddeint

model = lambda Y,t:  -Y( t-3*cos( Y(t) )**2 )
tt = linspace(0, 30, 2000)
yy = ddeint(model, lambda t:1, tt)

fig, ax = subplots(1,figsize=(4,4))
ax.plot(tt, yy)
    
show()