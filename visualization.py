'''At the center of most matplotlib scripts is pyplot. The pyplot module
is stateful and tracks changes to a figure. All pyplot functions
revolve around creating or manipulating the state of a figure.'''

import matplotlib.pyplot as plt
import numpy as np

plt.plot([1, 2, 3, 4, 5])
plt.xlabel('x values')
plt.ylabel('y value')
plt.title('First matplot')

#plot()
x = np.arange(5)
rng = np.random.default_rng()
y = rng.integers(1, 10, 5)
plt.plot(x, y)
#Or you can add these parameters
plt.plot(x, y, color='green', marker='o',
linestyle='dashed', linewidth=2,
markersize=12)

# evenly sampled time at .2 intervals
t = np.arange(0., 5., 0.2)
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.axis([0, 6, 0, 150]) # x and y range of axis

