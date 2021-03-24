import numpy as np
import matplotlib.pyplot as plt

from plotting import *



plt.style.use('dark_background')
fig, ax = plt.subplots(2, 2, \
                       figsize=(8, 10), dpi=200)


plot(ax[0,0], np.linspace(-10,10,200), np.sin(np.linspace(-10,10,200)), \
     title='Title or LaTeX: $\\pi^{xx}=2$', xlabel='x-axis', ylabel='y-axis', \
     descrip='b.', label='1')

plot(ax[1,1], np.linspace(-10,10,200), np.cos(np.linspace(-10,10,200)), \
     title='Title or LaTeX: $\\pi^{xx}=2$', xlabel='x-axis', ylabel='y-axis', \
     descrip='g.', label='2')

ax[0,0].legend()
ax[1,1].legend()
plt.show()