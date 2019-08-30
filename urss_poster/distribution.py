import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

def F(s):
    return 4*np.pi*np.arcsin(np.sqrt(s) - 0.5)

def dist(s):
    conds = [s < 0.25, (s > 0.25) & (s < 2.25), s > 2.25]
    funcs = [lambda s: 0, lambda s: F(s), lambda s: 1]
    return np.piecewise(s, conds, funcs)

xx = np.linspace(0, 2.5, 100000)
yy = []

for x in xx:
    if x <= 0.25:
        yy.append(0)
    elif (x > 0.25) & (x < 2.25):
        yy.append(F(x))
    else:
        yy.append(4*np.pi*np.pi)

plt.axis([0, 3, -0.5, 4*np.pi*np.pi + 0.5])
plt.plot(xx, yy)
plt.show()
